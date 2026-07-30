from pathlib import Path

from common import clear_directory


before_deleted, before_failed = clear_directory(Path("before"))
after_deleted, after_failed = clear_directory(Path("after"))

print("=" * 40)
print("Image Converter - Clear All")
print("=" * 40)

print(f"Before : {before_deleted} deleted")
print(f"After  : {after_deleted} deleted")

if before_failed or after_failed:
    print(f"Failed : {before_failed + after_failed}")

print("\nDone!")