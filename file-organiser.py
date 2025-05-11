import os
import shutil
import argparse
import textwrap

RED = "\033[31m"
RESET = "\033[0m"

EXTENSIONS_DEFAULT = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".raw", ".heif", ".svg", ".ico", ".jfif"],
    "documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt", ".ods", ".rtf", ".html", ".epub", ".md", ".tex", ".xml"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpg", ".mpeg", ".3gp", ".m4v", ".h264", ".ogv"],
    "music": [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a", ".wma", ".alac", ".aiff", ".opus", ".amr", ".mp2"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".tar.gz", ".tar.bz2", ".tar.xz", ".cab", ".iso", ".dmg"]
}

def move_file(file, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(file, os.path.join(destination_folder, os.path.basename(file)))

def organize_folder(path, categories):
    files = os.listdir(path)
    extensions = {cat: EXTENSIONS_DEFAULT[cat] for cat in categories}

    for file_name in files:
        file_path = os.path.join(path, file_name)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file_name)[1].lower()
        categorized = False

        for cat, exts in extensions.items():
            if file_extension in exts:
                destination_folder = os.path.join(path, cat.capitalize())
                move_file(file_path, destination_folder)
                print(f"✔  - {file_name} → {cat.capitalize()}/")
                categorized = True
                break

        if not categorized:
            other_folder = os.path.join(path, "Others")
            move_file(file_path, other_folder)
            print(f"→ {file_name} → Others/")

def main():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent('''\
            Organizes files in a folder by type (images, documents, videos, etc.).
            Available categories:
                - images
                - documents
                - videos
                - music
                - archives
            Use the --categories option to specify which categories you want to organize.
        '''),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "path", 
        help="Path to the folder to organize"
    )
    parser.add_argument(
        "--categories", 
        nargs="+", 
        choices=EXTENSIONS_DEFAULT.keys(),
        default=list(EXTENSIONS_DEFAULT.keys()),
        help=textwrap.dedent('''\
            Categories to organize (default: all).
            You can specify one or more categories. Available categories are:
                - images
                - documents
                - videos
                - music
                - archives   
        ''')
    )

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"{RED}Folder not found.{RESET}")
        return

    organize_folder(args.path, args.categories)

if __name__ == "__main__":
    main()
