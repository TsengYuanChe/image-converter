# Image Converter

A lightweight Python toolkit for image conversion, resizing, PDF processing, and video thumbnail generation.

## Features

- Batch convert images to WebP
- Convert single-page PDF to WebP
- Batch resize images (100%, 50%, 25%, 16%)
- Generate WebP thumbnails from videos
- Quickly clear input/output folders
- Easy to use with an interactive console menu

---

## Requirements

- Python 3.11+

---

## Project Structure

```text
image-converter/
│
├── app.py
├── common.py
│
├── image/
│   ├── to_webp.py
│   └── resize.py
│
├── video/
│   └── thumbnail.py
│
├── utilities/
│   ├── clear_before.py
│   ├── clear_after.py
│   └── clear_all.py
│
├── before/
├── after/
│
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
python -m pip install -r requirements.txt
```

---

## Install New Packages

Example:

```bash
python -m pip install pillow
```

Update `requirements.txt` after installing new packages:

```bash
python -m pip freeze > requirements.txt
```

---

## Run

Launch the application:

```bash
python app.py
```

Select a tool from the interactive menu.

---

## Project Workflow

1. Put your files into the `before` folder.
2. Launch the application.
3. Select the desired tool.
4. Processed files will be saved to the `after` folder.

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
- [x] Single-page PDF → WebP
- [x] Batch image resize
- [x] Video thumbnail generator
- [x] Interactive console menu

### v1.1

- [ ] AI Background Removal

### v1.2

- [ ] WebP → PNG
- [ ] HEIC → WebP
- [ ] AVIF support

### v1.3

- [ ] Image compression
- [ ] Batch rename
- [ ] Metadata viewer

---

## License

MIT