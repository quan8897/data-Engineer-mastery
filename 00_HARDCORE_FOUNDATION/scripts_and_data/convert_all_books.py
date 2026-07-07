import os
import pathlib
import sys
import time

try:
    import pymupdf4llm
except ImportError:
    print("Error: pymupdf4llm is not installed. Run 'pip install pymupdf4llm' first.")
    sys.exit(1)

# Paths
WORKSPACE_ROOT = pathlib.Path(__file__).parent.parent.parent.resolve()
BOOKS_DIR = WORKSPACE_ROOT / "Data-Engineer-Books-main" / "Data-Engineer-Books-main"
LIBRARY_DIR = WORKSPACE_ROOT / "books_markdown"

# Create output directory
LIBRARY_DIR.mkdir(parents=True, exist_ok=True)

print(f"Workspace root: {WORKSPACE_ROOT}")
print(f"Looking for books in: {BOOKS_DIR}")
print(f"Saving markdown books to: {LIBRARY_DIR}")

# Find all PDFs and EPUBs
supported_extensions = {".pdf", ".epub"}
files_to_convert = []

if BOOKS_DIR.exists():
    for f in BOOKS_DIR.iterdir():
        if f.is_file() and f.suffix.lower() in supported_extensions:
            files_to_convert.append(f)
else:
    print(f"Error: Books directory {BOOKS_DIR} does not exist.")
    sys.exit(1)

files_to_convert.sort()
print(f"Found {len(files_to_convert)} files to process.")

# Also check if we can copy the already converted Kimball book
kimball_md = WORKSPACE_ROOT / "01_DATA_WAREHOUSING_SQL" / "THE_DATA_WAREHOUSE_TOOLKIT.md"

for idx, file_path in enumerate(files_to_convert, 1):
    file_name = file_path.name
    clean_name = file_path.stem.replace(" ", "_").replace("-", "_").lower()
    # Strip non-alphanumeric chars at the beginning
    while clean_name and not clean_name[0].isalnum():
        clean_name = clean_name[1:]
    output_md_path = LIBRARY_DIR / f"{clean_name}.md"

    print(f"\n[{idx}/{len(files_to_convert)}] Processing: {file_name}")
    print(f"Target file: {output_md_path}")

    # Special case: if it's the Kimball book and we already have it in the DW folder, copy it
    if "data_warehouse_toolkit" in clean_name and kimball_md.exists() and not output_md_path.exists():
        print(f"-> Found existing conversion for Kimball book. Copying from {kimball_md.name}...")
        output_md_path.write_text(kimball_md.read_text(encoding="utf-8"), encoding="utf-8")
        print("-> Copied successfully.")
        continue

    if output_md_path.exists():
        print(f"-> Output file already exists. Skipping.")
        continue

    start_time = time.time()
    try:
        print(f"-> Extracting text to markdown using pymupdf4llm...")
        # pymupdf4llm.to_markdown can take a pdf/epub file path
        md_text = pymupdf4llm.to_markdown(str(file_path))
        
        # Write to file
        output_md_path.write_text(md_text, encoding="utf-8")
        elapsed = time.time() - start_time
        size_kb = output_md_path.stat().st_size / 1024
        print(f"-> Done in {elapsed:.2f}s! Output size: {size_kb:.2f} KB")
    except Exception as e:
        print(f"-> ERROR converting {file_name}: {e}")

print("\nAll conversions completed.")
