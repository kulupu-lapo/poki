from typing import Generator
import yaml
from pathlib import Path
import re
import json


ROOT = Path("../../")
LT = ROOT / "collections" / "lipu-tenpo"
EXPORT = Path("export")


def get_paths_from_collection(collection: Path) -> Generator[Path]:
    with open(collection) as f:
        if a := yaml.safe_load(f):
            if "items" in a:
                for item in a["items"]:
                    yield ROOT / item


def dump_article(file: Path):
    content = file.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    _, frontmatter, content = parts
    data = yaml.safe_load(frontmatter)
    metadata = {
        "nimi-suli": data["title"],
        "jan-pali": data["authors"][0] if "translators" not in data else data["translators"][0],
        "tags": data["tags"] or ["REPLACE"],
    }
    formatted_metadata = (yaml
        .dump(metadata, sort_keys=False)
        .replace("\n- ", "\n  - ")
    )
    return f"---\n{formatted_metadata}---\n\n{content.strip()}\n"

EXPORT.mkdir(exist_ok=True)
for collection in sorted(LT.glob("*")):
    issue_title = re.search(r"nanpa\-\w+(?=\.yaml)", collection.name).group()
    export_dir: Path = EXPORT / issue_title
    export_dir.mkdir(exist_ok=True)

    for path in get_paths_from_collection(collection):
        _ = (export_dir / path.name).write_text(dump_article(path))

    with open(export_dir / f"{issue_title}.11tydata.json", "w") as f:
        json.dump({"tags": [issue_title.replace("-", " ")], "date": ""}, f, indent=4)
