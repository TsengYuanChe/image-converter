from pathlib import Path

from PIL import Image, ImageOps

from common import (
    AFTER_DIR,
    BEFORE_DIR,
    IMAGE_EXTENSIONS,
    ensure_directories,
    get_files,
    print_header,
)

# ==========================
# Settings
# ==========================

SCALES = [100, 50, 25, 16]

OVERWRITE = False


def build_output_path(image_path: Path, scale: int) -> Path:
    """Build the output filename for a resized image."""

    if scale == 100:
        filename = image_path.name
    else:
        filename = f"{image_path.stem}@{scale}{image_path.suffix.lower()}"

    return AFTER_DIR / filename


def resize_image(image_path: Path, scale: int) -> bool:
    """Resize an image to the specified percentage.

    Returns:
        bool: True if an image was generated, False if skipped.
    """

    output_path = build_output_path(image_path, scale)

    if output_path.exists() and not OVERWRITE:
        print(f"    - Skipped: {output_path.name} already exists")
        return False

    with Image.open(image_path) as image:
        image = ImageOps.exif_transpose(image)

        original_width, original_height = image.size

        new_width = max(1, round(original_width * scale / 100))
        new_height = max(1, round(original_height * scale / 100))

        if scale == 100:
            resized_image = image.copy()
        else:
            resized_image = image.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS,
            )

        try:
            resized_image.save(output_path)
        finally:
            resized_image.close()

    print(
        f"    ✓ {output_path.name}: "
        f"{original_width}x{original_height} "
        f"-> {new_width}x{new_height}"
    )

    return True


def main() -> None:
    print_header("Image Converter - Resize")

    ensure_directories()

    images = get_files(
        BEFORE_DIR,
        IMAGE_EXTENSIONS,
    )

    if not images:
        print("No supported images found.")
        return

    succeeded = 0
    skipped = 0
    failed = 0

    print(f"Found {len(images)} image(s).\n")

    for index, image_path in enumerate(images, start=1):
        print(f"[{index}/{len(images)}] {image_path.name}")

        for scale in SCALES:
            try:
                generated = resize_image(image_path, scale)

                if generated:
                    succeeded += 1
                else:
                    skipped += 1

            except Exception as error:
                print(
                    f"    ✗ Failed: "
                    f"{image_path.name} @{scale}% - {error}"
                )
                failed += 1

        print()

    print_header("Finished")

    print(f"Succeeded : {succeeded}")
    print(f"Skipped   : {skipped}")
    print(f"Failed    : {failed}")
    print(f"Output    : {AFTER_DIR}")


if __name__ == "__main__":
    main()