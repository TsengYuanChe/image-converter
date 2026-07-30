from pathlib import Path

from common import clear_directory

deleted, failed = clear_directory(Path("before"))

print(f"Deleted: {deleted}")
print(f"Failed : {failed}")