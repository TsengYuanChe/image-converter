from pathlib import Path

from PIL import Image, ImageOps

BEFORE_DIR = Path("before")
AFTER_DIR = Path("after")

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
}

SCALES = [100, 50, 25, 16]

OVERWRITE = False


def build_output_path(image_path: Path, scale: int) -> Path:
    """Build the output filename for a resized image."""

    if scale == 100:
        filename = image_path.name
    else:
        filename = f"{image_path.stem}@{scale}{image_path.suffix.lower()}"

    return AFTER_DIR / filename


def resize_image(image_path: Path, scale: int) -> None:
    """Resize an image to the specified percentage."""

    output_path = build_output_path(image_path, scale)

    if output_path.exists() and not OVERWRITE:
        print(f"Skipped: {output_path.name} already exists")
        return

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

        resized_image.save(output_path)

        print(
            f"✓ {output_path.name}: "
            f"{original_width}x{original_height} "
            f"-> {new_width}x{new_height}"
        )


def main() -> None:
    BEFORE_DIR.mkdir(exist_ok=True)
    AFTER_DIR.mkdir(exist_ok=True)

    images = [
        path
        for path in BEFORE_DIR.iterdir()
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not images:
        print("No supported images found in before/")
        return

    succeeded = 0
    failed = 0

    for image_path in images:
        for scale in SCALES:
            try:
                resize_image(image_path, scale)
                succeeded += 1
            except OSError as error:
                print(f"✗ Failed: {image_path.name} @{scale}% - {error}")
                failed += 1

    print("\nFinished")
    print(f"Succeeded: {succeeded}")
    print(f"Failed   : {failed}")


if __name__ == "__main__":
    main()