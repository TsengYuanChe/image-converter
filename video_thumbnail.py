from pathlib import Path
import shutil
import subprocess

# ==========================
# Settings
# ==========================

SUPPORTED_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".m4v",
    ".webm",
}

BEFORE_DIR = Path("before")
AFTER_DIR = Path("after")

# 擷取影片第幾秒
THUMBNAIL_TIME = 128.0

# 縮圖寬度；高度自動維持比例
THUMBNAIL_WIDTH = 800

# WebP 品質，範圍 0-100
QUALITY = 85

# 是否覆蓋已存在的縮圖
OVERWRITE = True


def create_thumbnail(video_path: Path) -> None:
    """Extract one video frame and save it as a WebP thumbnail."""

    output_path = AFTER_DIR / f"{video_path.stem}-thumbnail.webp"

    command = [
        "ffmpeg",
        "-ss",
        str(THUMBNAIL_TIME),
        "-i",
        str(video_path),
        "-frames:v",
        "1",
        "-vf",
        f"scale={THUMBNAIL_WIDTH}:-2",
        "-c:v",
        "libwebp",
        "-quality",
        str(QUALITY),
    ]

    if OVERWRITE:
        command.append("-y")
    else:
        command.append("-n")

    command.append(str(output_path))

    subprocess.run(
        command,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )


def main() -> None:
    print("=" * 40)
    print("Image Converter - Video Thumbnail")
    print("=" * 40)

    if shutil.which("ffmpeg") is None:
        print("FFmpeg is not installed or not available in PATH.")
        print("macOS: brew install ffmpeg")
        return

    BEFORE_DIR.mkdir(exist_ok=True)
    AFTER_DIR.mkdir(exist_ok=True)

    videos = [
        file
        for file in BEFORE_DIR.iterdir()
        if file.is_file()
        and file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not videos:
        print("No supported video files found.")
        return

    success = 0

    print(f"Found {len(videos)} video(s).\n")

    for index, video_path in enumerate(videos, start=1):
        print(f"[{index}/{len(videos)}] {video_path.name}")

        try:
            create_thumbnail(video_path)
            print(f"    ✓ {video_path.stem}-thumbnail.webp\n")
            success += 1

        except subprocess.CalledProcessError as error:
            print("    ✗ Failed")

            if error.stderr:
                print(f"      {error.stderr.strip()}\n")

    print("=" * 40)
    print("Finished")
    print("=" * 40)
    print(f"Success : {success}")
    print(f"Failed  : {len(videos) - success}")
    print(f"Output  : {AFTER_DIR.resolve()}")


if __name__ == "__main__":
    main()