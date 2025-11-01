from typing import Generator
import yaml
from pathlib import Path
import datetime as dt
import re


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
        "tags": data["tags"],
    }
    formatted_metadata = (yaml
        .dump(metadata, sort_keys=False)
        .replace("\n- ", "\n  - ")
    )
    return f"---\n{formatted_metadata}---\n{content}\n"

EXPORT.mkdir(exist_ok=True)
for collection in sorted(LT.glob("*")):
    for path in get_paths_from_collection(collection):
        article = dump_article(path)

        export_dir: Path = EXPORT / f"nanpa {re.search(r"(?<=nanpa\-)\w+(?=\.yaml)", collection.name).group()}"
        export_dir.mkdir(exist_ok=True)
        _ = (export_dir / path.name).write_text(article)
