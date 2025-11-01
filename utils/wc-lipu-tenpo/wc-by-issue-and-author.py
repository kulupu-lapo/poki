import pandas as pd
import re
from pathlib import Path
import yaml

# COLLECTIONS = Path("../poki/collections/lipu-tenpo/")
ROOT = Path("../../")
LT = ROOT / "collections" / "lipu-tenpo"

TOP_N_CONTRIBUTORS = 12


# def get_collections():
#     for collection in sorted(COLLECTIONS.glob("*")):
#         yield collection


def get_paths_from_collection(collection):
    with open(collection) as f:
        if a := yaml.safe_load(f):
            if "items" in a:
                for item in a["items"]:
                    yield ROOT / item


def wc(text):
    matches = re.findall(r"\b\w+\b", text)
    return len(matches)


def aggregate_last_n_rows(df, n):
    # Sum the last N rows
    aggregated_row = df.iloc[-n:].sum()

    # Convert to DataFrame and rename the index to "Other"
    aggregated_df = pd.DataFrame(aggregated_row).T
    aggregated_df.index = ["Other"]

    # Exclude the last N rows and append the aggregated result
    new_df = pd.concat([df.iloc[:-n], aggregated_df])

    return new_df


count = []
# for path in Path("../poki/plaintext/").glob("**/*.md"):

for collection in sorted(LT.glob("*")):
    for path in get_paths_from_collection(collection):
        # print(path)
        with open(path) as f:
            text = f.read()

            # separate text and metadata
            meta = "---".join(text.split("---")[:2]).replace("---\n", "")
            meta = yaml.safe_load(meta)
            author = meta["authors"][0] if "translators" not in meta else meta["translators"][0]

            text = "---".join(text.split("---")[2:])  # filter away metadata
            wc_text = wc(text)

        _, _, _, year, month, name = path.parts
        count.append([collection.stem, wc_text, author])

# A list of articles.
df = pd.DataFrame(count, columns=["issue", "wc", "author"])

# A list of all unique authors, sorted by wc contribution.
authors = (
    df[["wc", "author"]]
    .groupby("author")
    .sum()
    .sort_values("wc", ascending=False)
    .index
)

# Aggregate articles from the same author within the same issue.
df = df.groupby(["issue", "author"], as_index=False).sum()

# Pivot with rows for authors and columns for issues.
df = df.pivot(index="author", columns="issue", values="wc").fillna(0)

# Sort rows by author contribution.
df = df.reindex(authors)

df = aggregate_last_n_rows(df, len(df) - TOP_N_CONTRIBUTORS)

df = df.transpose()

df.to_csv("wc-by-issue-and-author.tsv", sep="\t")
