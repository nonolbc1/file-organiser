import os
import shutil
import argparse
import json
import textwrap
import sys
from pathlib import Path

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

SCRIPT_DIR = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent
EXT_JSON = os.path.join(SCRIPT_DIR, "extensions.json")

DEFAULT_EXTENSIONS = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".raw", ".heif", ".svg", ".ico", ".jfif"],
    "documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt", ".ods", ".rtf", ".html", ".epub", ".md", ".tex", ".xml"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpg", ".mpeg", ".3gp", ".m4v", ".h264", ".ogv"],
    "music": [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a", ".wma", ".alac", ".aiff", ".opus", ".amr", ".mp2"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".tar.gz", ".tar.bz2", ".tar.xz", ".cab", ".iso", ".dmg"]
}


def load_extensions():
    if os.path.exists(EXT_JSON):
        with open(EXT_JSON, "r") as f:
            return json.load(f)
    else:
        with open(EXT_JSON, "w") as f:
            json.dump(DEFAULT_EXTENSIONS, f, indent=4)
        return DEFAULT_EXTENSIONS.copy()


def save_extensions(data):
    with open(EXT_JSON, "w") as f:
        json.dump(data, f, indent=4)


def move_file(file, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(file, os.path.join(destination_folder, os.path.basename(file)))


def organize_folder(path, categories, extension_data):
    files = os.listdir(path)

    for file_name in files:
        file_path = os.path.join(path, file_name)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file_name)[1].lower()
        moved = False

        for category in categories:
            if file_extension in extension_data.get(category, []):
                destination_folder = os.path.join(path, category.capitalize())
                move_file(file_path, destination_folder)
                print(f"✔  - {file_name} → {category.capitalize()}/")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(path, "Others")
            move_file(file_path, other_folder)
            print(f"→ {file_name} → Others/")


def main():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent('''\
            Organize files in a folder by type.
            You can also manage custom categories using:
            --add category .ext1 .ext2 ...
            --remove category [optional .ext1 .ext2 ...]
        '''),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("path", nargs="?", help="Path to the folder to organize")
    parser.add_argument("--categories", nargs="+", help="Specific categories to use")
    parser.add_argument("--add", nargs="+", help="Add a category or extensions to an existing one")
    parser.add_argument("--remove", nargs="+", help="Remove extensions or the category itself if none provided")

    args = parser.parse_args()
    extension_data = load_extensions()

    if args.add:
        category = args.add[0]
        extensions = args.add[1:] if len(args.add) > 1 else []

        if category not in extension_data:
            extension_data[category] = []

        added = 0
        for ext in extensions:
            if ext not in extension_data[category]:
                extension_data[category].append(ext)
                added += 1

        save_extensions(extension_data)
        if added:
            print(f"{GREEN}[✓] Added {added} extension(s) to category '{category}'.{RESET}")
        else:
            print(f"[!] No new extensions to add to '{category}'.")
        return

    if args.remove:
        category = args.remove[0]
        extensions = args.remove[1:] if len(args.remove) > 1 else []

        if category not in extension_data:
            print(f"{RED}[X] Category '{category}' not found.{RESET}")
            return

        if not extensions:
            del extension_data[category]
            print(f"{GREEN}[✓] Category '{category}' completely removed.{RESET}")
        else:
            removed = 0
            for ext in extensions:
                if ext in extension_data[category]:
                    extension_data[category].remove(ext)
                    removed += 1
                else:
                    print(f"{RED}[X] Extension '{ext}' not found in '{category}'.{RESET}")
            if removed:
                print(f"{GREEN}[✓] Removed {removed} extension(s) from '{category}'.{RESET}")

        save_extensions(extension_data)
        return

    if args.path:
        if not os.path.exists(args.path):
            print(f"{RED}[X] Folder not found: {args.path}{RESET}")
            return
        selected_categories = args.categories if args.categories else list(extension_data.keys())
        organize_folder(args.path, selected_categories, extension_data)
    else:
        print(f"{RED}Please specify a folder path or use --add / --remove.{RESET}")


if __name__ == "__main__":
    main()
