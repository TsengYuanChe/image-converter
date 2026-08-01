from pathlib import Path

# ==========================
# Paths
# ==========================

ROOT_DIR = Path(__file__).resolve().parent

BEFORE_DIR = ROOT_DIR / "before"
AFTER_DIR = ROOT_DIR / "after"

# ==========================
# Supported Formats
# ==========================

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".m4v",
    ".webm",
}

PDF_EXTENSIONS = {
    ".pdf",
}

def ensure_directories() -> None:
    """Create required directories."""

    BEFORE_DIR.mkdir(exist_ok=True)
    AFTER_DIR.mkdir(exist_ok=True)
    
def get_files(
    directory: Path,
    extensions: set[str],
) -> list[Path]:

    return [
        file
        for file in directory.iterdir()
        if file.is_file()
        and file.suffix.lower() in extensions
    ]
    
def print_header(title: str) -> None:

    print("=" * 40)
    print(title)
    print("=" * 40)

def clear_directory(directory: Path) -> tuple[int, int]:
    """Delete all files in the specified directory.

    Returns:
        tuple[int, int]: (deleted_count, failed_count)
    """

    directory.mkdir(exist_ok=True)

    deleted = 0
    failed = 0
    
    IGNORE_FILES = {
        "README.md",
    }

    for item in directory.iterdir():

        if not item.is_file():
            continue
        
        if item.name in IGNORE_FILES:
            continue

        try:
            item.unlink()
            deleted += 1

        except Exception:
            failed += 1

    return deleted, failed