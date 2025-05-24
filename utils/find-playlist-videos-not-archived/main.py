import yaml
from pathlib import Path
import yt_dlp
import re
import pandas as pd


# One of the common usecases we might have with poki Lapo is,
# A music playlist is ahead of us in terms of archiving songs.
# To catch up, we'd want a list of all song links that are
# currently not present in poki Lapo.
# This is the script for that. Yes, it's mostly vibe-coded,
# but quick and dirty is better than nothing.


# === Usage ===
PLAYLIST_URL = (
    "https://www.youtube.com/playlist?list=PLc7R2x5fn6AqRFUR9JzGIqh0FMdtsXRnH"
)
MD_DIRECTORY = "../../plaintext/"


# 1. Download all video links from a YouTube playlist
def get_playlist_links(playlist_url):
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "dump_single_json": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        entries = info.get("entries", [])
        return {
            entry["id"]: (
                entry.get("uploader", "Unknown Author"),
                entry.get("title", "Unknown Title")
            ) for entry in entries
        }
        # return set(entry['id'] for entry in entries)


# 2. Extract YouTube links from frontmatter in Markdown files
def extract_youtube_links_from_md_files(directory):

    # Regex pattern to extract YouTube video IDs
    # Matches:
    # - youtube.com/watch?v=VIDEO_ID
    # - youtu.be/VIDEO_ID
    # - optional extra params (ignored)
    youtube_id_pattern = re.compile(
        r"""
        (?:                             # non-capturing group
        (?:https?://)?                # optional protocol
        (?:www\.)?                    # optional www
        (?:youtube\.com/watch\?v=|    # youtube.com/watch?v=VIDEO_ID
            youtube\.com/embed/|       # youtube.com/embed/VIDEO_ID
            youtu\.be/)                # youtu.be/VIDEO_ID
        )
        (?P<id>[a-zA-Z0-9_-]{11})       # video ID (exactly 11 chars)
        """,
        re.VERBOSE
    )

    md_files = Path(directory).glob("**/*.md")
    links = set()

    for file in md_files:
        content = file.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        frontmatter = parts[1]
        data = yaml.safe_load(frontmatter)
        sources = data.get("sources", [])
        if sources is None:
            continue
        for source in sources:
            for match in youtube_id_pattern.finditer(source):
                links.add(match.group("id"))

    return links


# 3. Compare and display links in playlist but not in markdown files
def show_unreferenced_links(playlist_url, md_directory):
    playlist_items = get_playlist_links(playlist_url)
    playlist_ids = set(playlist_items.keys())
    md_ids = extract_youtube_links_from_md_files(md_directory)

    print("Archived links:", len(md_ids))
    print("Playlist links:", len(playlist_ids))

    unreferenced = playlist_ids - md_ids

    df = []
    print(f"Unreferenced links {len(unreferenced)}:")
    for id_ in sorted(unreferenced):
        df.append([
            f"https://youtu.be/{id_}",
            str(playlist_items[id_][0]),
            str(playlist_items[id_][1]),
        ])

    df = pd.DataFrame(df, columns=["link", "uploader", "title"])
    df = df.sort_values("uploader")
    df.to_csv("remaining-videos.csv", index=False)
    print("Created remaining-videos.csv")


show_unreferenced_links(PLAYLIST_URL, MD_DIRECTORY)
