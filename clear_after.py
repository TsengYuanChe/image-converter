from pathlib import Path

from common import clear_directory

deleted, failed = clear_directory(Path("after"))

print(f"Deleted: {deleted}")
print(f"Failed : {failed}")