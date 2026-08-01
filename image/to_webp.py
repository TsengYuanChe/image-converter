import io
from pathlib import Path

import fitz
from PIL import Image

from common import (
    AFTER_DIR,
    BEFORE_DIR,
    IMAGE_EXTENSIONS,
    PDF_EXTENSIONS,
    ensure_directories,
    get_files,
    print_header,
)

# ==========================
# Settings
# ==========================

SUPPORTED_EXTENSIONS = IMAGE_EXTENSIONS | PDF_EXTENSIONS

# Output WebP quality (0-100)
# 100 = Highest quality, largest file
# 90  = Recommended for hero / portfolio images
# 80  = Recommended for general website images
# 70  = Smaller file, slight quality loss
QUALITY = 90

# Use lossless compression
# True  = No quality loss, larger file
# False = Smaller file, recommended for photos
LOSSLESS = False

# PDF rendering quality
PDF_DPI = 300


def open_image(path: Path) -> Image.Image:
    """Open an image or render a single-page PDF as an image."""

    if path.suffix.lower() != ".pdf":
        return Image.open(path)

    with fitz.open(path) as document:
        if len(document) != 1:
            raise ValueError("Only single-page PDFs are supported.")

        page = document.load_page(0)

        pixmap = page.get_pixmap(
            dpi=PDF_DPI,
            alpha=False,
        )

        image_data = pixmap.tobytes("png")

    image = Image.open(io.BytesIO(image_data))
    image.load()

    return image


def convert_to_webp(file_path: Path) -> None:
    """Convert a supported image or single-page PDF to WebP."""

    output_path = AFTER_DIR / f"{file_path.stem}.webp"

    with open_image(file_path) as image:
        image.save(
            output_path,
            format="WEBP",
            quality=QUALITY,
            lossless=LOSSLESS,
        )


def main() -> None:
    print_header("Image Converter - WebP")

    ensure_directories()

    files = get_files(
        BEFORE_DIR,
        SUPPORTED_EXTENSIONS,
    )

    if not files:
        print("No supported files found.")
        return

    success = 0

    print(f"Found {len(files)} file(s).\n")

    for index, file_path in enumerate(files, start=1):
        print(f"[{index}/{len(files)}] {file_path.name}")

        try:
            convert_to_webp(file_path)

            print("    ✓ Success\n")
            success += 1

        except Exception as error:
            print(f"    ✗ Failed: {error}\n")

    print_header("Finished")

    print(f"Success : {success}")
    print(f"Failed  : {len(files) - success}")
    print(f"Output  : {AFTER_DIR}")


if __name__ == "__main__":
    main()