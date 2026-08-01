from image import resize, to_webp
from utilities import clear_after, clear_all, clear_before
from video import video_thumbnail


def show_menu() -> None:
    print()
    print("=" * 45)
    print("Image Converter")
    print("=" * 45)
    print("1. Convert images to WebP")
    print("2. Resize images")
    print("3. Generate video thumbnails")
    print("4. Clear before folder")
    print("5. Clear after folder")
    print("6. Clear all folders")
    print("0. Exit")
    print("=" * 45)


def main() -> None:
    actions = {
        "1": to_webp.main,
        "2": resize.main,
        "3": video_thumbnail.main,
        "4": clear_before.main,
        "5": clear_after.main,
        "6": clear_all.main,
    }

    while True:
        show_menu()

        choice = input("Select an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid option. Please try again.")
            continue

        print()

        try:
            action()
        except Exception as error:
            print(f"Execution failed: {error}")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()