from utilities import clear_after, clear_before


def main() -> None:
    """Clear both before and after directories."""

    clear_before.main()
    print()
    clear_after.main()


if __name__ == "__main__":
    main()