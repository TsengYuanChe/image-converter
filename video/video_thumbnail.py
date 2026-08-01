from pathlib import Path
import shutil
import subprocess

from common import (
    AFTER_DIR,
    BEFORE_DIR,
    VIDEO_EXTENSIONS,
    ensure_directories,
    get_files,
    print_header,
)

# ==========================
# Settings
# ==========================

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
    print_header("Image Converter - Video Thumbnail")

    if shutil.which("ffmpeg") is None:
        print("FFmpeg is not installed or not available in PATH.")
        print("macOS: brew install ffmpeg")
        return

    ensure_directories()

    videos = get_files(
        BEFORE_DIR,
        VIDEO_EXTENSIONS,
    )

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

    print_header("Finished")

    print(f"Success : {success}")
    print(f"Failed  : {len(videos) - success}")
    print(f"Output  : {AFTER_DIR}")


if __name__ == "__main__":
    main()