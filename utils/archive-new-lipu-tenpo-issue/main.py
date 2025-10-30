import yaml
from pathlib import Path
import datetime as dt


# lipu tenpo publishes a set of markdown files every 1-2 months,
# so it is helpful to do this almost entirely automatically.
# Change the consts to match the current date and issue.
#
# After dumping, make sure to go through manually and check
# the metadata for errors or potential additions (e.g. references
# to original works; list of proofreaders).

# === Usage ===
LIPU_TENPO_TITLE = "lon"
LIPU_TENPO_NANPA = "0034"
DATE = "2025-10-31"

LIPU_TENPO_DIRECTORY = "../../../../liputenpo/liputenpo.org/toki/"
YEAR = int(DATE[:4])
MONTH = int(DATE[5:7])
DAY = int(DATE[8:10])
LAPO_DIRECTORY = Path(f"../../plaintext/{YEAR:02}/{MONTH:02}/")


def main():

    md_files = Path(LIPU_TENPO_DIRECTORY) / f"nanpa-{LIPU_TENPO_TITLE}"

    print(md_files)

    for file in md_files.glob("**/*.md"):
        content = file.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        _, frontmatter, content = parts
        data = yaml.safe_load(frontmatter)
        metadata = {
            "title": data["nimi-suli"],  # throw error if no title
            "description": None,
            "authors": [data["jan-pali"]],  # throw error if no author
            "proofreaders": None,  # manual
            "date": dt.datetime(year=YEAR, month=MONTH, day=DAY),
            "date-precision": "day",
            "original": None,
            "tags": data["tags"],  # throw error if no category
            "license": "CC BY-SA 4.0",
            "sources": [
                f"https://liputenpo.org/lipu/nanpa-{LIPU_TENPO_NANPA}/",
                f"https://liputenpo.org/pdfs/{LIPU_TENPO_NANPA}{LIPU_TENPO_TITLE}.pdf",
                "https://github.com/lipu-tenpo/liputenpo.org/tree/main/toki",
            ],
            "archives": None,
            "preprocessing": None,
            "accessibility-notes": None,
            "notes": None,
        }
        formatted_metadata = (yaml
            .dump(metadata, sort_keys=False)
            .replace("\n- ", "\n  - ")
            .replace(" 00:00:00", "")
        )
        with open(LAPO_DIRECTORY / file.name, "w") as f:
            f.write(f"{formatted_metadata}\n---\n{content}\n")


main()
