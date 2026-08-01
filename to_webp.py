from pathlib import Path
import io

import fitz
from PIL import Image

# ==========================
# Settings
# ==========================

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf"}

# Output WebP quality (0-100)
# 100 = Highest quality, largest file
# 90  = Recommended (default)
# 80  = Recommended for websites
# 70  = Smaller file, slight quality loss
QUALITY = 90

# Use lossless compression
# True  = No quality loss, larger file
# False = Smaller file (recommended for photos)
LOSSLESS = False

# Input / Output folders
BEFORE_DIR = Path("before")
AFTER_DIR = Path("after")


def convert_to_webp(image_path: Path) -> bool:
    """Convert a single image to WebP."""

    output_path = AFTER_DIR / f"{image_path.stem}.webp"

    with open_image(image_path) as image:
        image.save(
            output_path,
            "WEBP",
            quality=QUALITY,
            lossless=LOSSLESS,
        )

    return True

def open_image(path: Path) -> Image.Image:
    """Open an image or the first page of a PDF."""

    if path.suffix.lower() != ".pdf":
        return Image.open(path)

    document = fitz.open(path)

    if len(document) != 1:
        document.close()
        raise ValueError("Only single-page PDFs are supported.")

    page = document.load_page(0)

    pixmap = page.get_pixmap(
        dpi=300,
        alpha=False,
    )

    image = Image.open(io.BytesIO(pixmap.tobytes("png")))

    document.close()

    return image

def main():

    print("=" * 40)
    print("Image Converter - WebP")
    print("=" * 40)

    BEFORE_DIR.mkdir(exist_ok=True)
    AFTER_DIR.mkdir(exist_ok=True)

    images = [
        file
        for file in BEFORE_DIR.iterdir()
        if file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not images:
        print("No supported images found.")
        return

    success = 0

    print(f"Found {len(images)} image(s).\n")

    for index, image in enumerate(images, start=1):

        print(f"[{index}/{len(images)}] {image.name}")

        try:

            convert_to_webp(image)

            print("    ✓ Success\n")

            success += 1

        except Exception as ex:

            print(f"    ✗ Failed: {ex}\n")

    print("=" * 40)
    print("Finished")
    print("=" * 40)

    print(f"Success : {success}")
    print(f"Failed  : {len(images) - success}")
    print(f"Output  : {AFTER_DIR.resolve()}")


if __name__ == "__main__":
    main()