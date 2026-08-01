from common import BEFORE_DIR, clear_directory, print_header


def main() -> None:
    """Clear all files in the before directory."""

    print_header("Clear Before")

    deleted, failed = clear_directory(BEFORE_DIR)

    print(f"Deleted : {deleted}")
    print(f"Failed  : {failed}")


if __name__ == "__main__":
    main()