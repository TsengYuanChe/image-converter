from pathlib import Path

from common import clear_directory

def main() -> None:
    """Clear all files in the before folder."""

    deleted, failed = clear_directory(Path("after"))
    
    print("=" * 40)
    print("Clear Before")
    print("=" * 40)
    print(f"Deleted : {deleted}")
    print(f"Failed  : {failed}")

if __name__ == "__main__":
    main()