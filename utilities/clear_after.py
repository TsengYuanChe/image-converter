from common import AFTER_DIR, clear_directory, print_header


def main() -> None:
    """Clear all files in the after directory."""

    print_header("Clear After")

    deleted, failed = clear_directory(AFTER_DIR)

    print(f"Deleted : {deleted}")
    print(f"Failed  : {failed}")


if __name__ == "__main__":
    main()