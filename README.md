# Image Converter

A lightweight Python tool for batch image conversion.

## Features

- Batch convert images to WebP
- Support JPG, JPEG and PNG
- Preserve image quality
- Easy to use with `before/` and `after/` folders

---

## Requirements

- Python 3.11+

---

## Project Structure

```text
image-converter/
│
├── before/
├── after/
│
├── common.py
├── to_webp.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install New Packages

```bash
pip install pillow
```

After installing new packages, update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## Run

```bash
python to_webp.py
```

---

## Project Workflow

1. Put images into the `before` folder.
2. Run the converter.
3. Converted images will be saved to the `after` folder.

---

## Git

Initialize repository:

```bash
git init
```

Add files:

```bash
git add .
```

First commit:

```bash
git commit -m "chore: initialize image converter project"
```

---

## Roadmap

### v1.0

- [x] JPG → WebP
- [x] PNG → WebP

### v1.1

- [ ] AI Background Removal

### v1.2

- [ ] WebP → PNG

### v1.3

- [ ] Resize Images
- [ ] Compress Images

---

## License

MIT