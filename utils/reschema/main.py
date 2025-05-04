import datetime
from pathlib import Path
import re
from ruamel.yaml import (
    YAML,
    CommentedMap,
    CommentedSeq,
)  # also requires `pip install ruamel.yaml.string`
import traceback
from tqdm.auto import tqdm

yaml = YAML(typ=["rt", "string"], pure=True)
yaml.default_flow_style = False
yaml.preserve_quotes = True
yaml.sort_base_mapping_type_on_output = False
# yaml.indent(mapping=2, sequence=2, offset=0) # slight majority, also default
# yaml.indent(mapping=2, sequence=4, offset=2) # almost as common as above
# yaml.width = 69420

yaml.representer.add_representer(
    type(None),
    lambda repr, _data: repr.represent_scalar("tag:yaml.org,2002:null", "null"),
)


def reschema(y):
    # # kinda cursed but it minimizes the null edit :3
    # # using regex because otherwise hyphens can occur in e.g. the description and make it non-idempotent
    if re.search(r"\n[a-z-]+/:\n  - ", y):
        yaml.indent(mapping=2, sequence=4, offset=2)
    else:
        yaml.indent(mapping=2, sequence=2, offset=0)

    data = yaml.load(y)

    def rename(old_key, new_key):
        pos = list(data.keys()).index(old_key)
        to_rename = data.pop(old_key)
        data.insert(pos, new_key, to_rename)

    def make_neighbors(anchor_key, move_key):
        to_move = data.pop(move_key)
        pos = list(data.keys()).index(anchor_key)
        data.insert(pos + 1, move_key, to_move)

    # rescheming actions go here
    # comments might be fragile? use helper functions or refer to https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/comments.py

    if "translators" in data:
        data.pop("translators")

    # # 1. translator rework
    # if "translators" in data:
    #     if "authors" in data:
    #         rename("authors", "original-authors")
    #     rename("translators", "authors")
    #     if "original-authors" not in data:
    #         data["original-authors"] = CommentedSeq(["unknown"])
    #         data["original-authors"].yaml_add_eol_comment(
    #             "added automatically during reschema", 0
    #         )
    #     make_neighbors("authors", "original-authors")
    #
    # # 2. date precision rework
    # if "date" in data and "date-precision" not in data:
    #     # looking for date-precision comment
    #     pos = list(data.keys()).index("date")
    #     k = list(data.keys())[pos + 1]
    #     if (
    #         data.ca
    #         and "date" in data.ca.items
    #         and "date-precision:" in data.ca.items["date"][2].value
    #     ):
    #         data["date-precision"] = (
    #             data.ca.items["date"][2].value.split(": ")[-1].strip()
    #         )
    #         data.ca.items["date"][2] = None
    #     else:
    #         match data["date"]:
    #             case None:
    #                 data["date"] = datetime.date(2001, 1, 1)
    #                 data["date-precision"] = "none"
    #             case int():  # seems to not be a thing
    #                 data["date"] = datetime.date(data["date"], 1, 1)
    #                 data["date-precision"] = "year"
    #             case datetime.datetime():
    #                 # do we need to specify day precision?
    #                 pass
    #     if "date-precision" in data:
    #         make_neighbors("date", "date-precision")

    out = yaml.dump_to_string(data)
    return out


for i in tqdm(
    list(Path("../../plaintext").glob("**/*.md"))
):
    try:
        with open(i) as f:
            text = f.read()
        front, contents = text.split("\n---\n", 1)
        front = front[4:]
        new_front = reschema(front)
        if new_front != front:
            with open(i, "w") as f:
                f.write(f"---\n{new_front}\n---\n{contents}")
    except:
        print(i)
        traceback.print_exc()
