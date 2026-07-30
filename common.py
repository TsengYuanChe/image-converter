from pathlib import Path


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