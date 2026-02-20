# 📄 Images to PDF Converter

A lightweight Python utility that converts a collection of images into a single PDF file. Designed for batch processing image directories with support for multiple common image formats.

## ✨ Features

- **Batch Conversion** — Automatically scans a directory and converts all images into a single PDF
- **Multi-Format Support** — Handles `.png`, `.jpg`, `.jpeg`, `.gif`, and `.bmp` formats
- **Lossless Conversion** — Uses `img2pdf` for direct embedding without re-encoding, preserving original image quality
- **Simple & Fast** — Minimal setup, single-script execution

## 📋 Prerequisites

- **Python** 3.7 or higher
- **pip** (Python package manager)

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/images-to-pdf-converter.git
   cd images-to-pdf-converter
   ```

2. **Install the required dependency:**

   ```bash
   pip install img2pdf
   ```

## 🔧 Usage

1. Place your images in a directory (e.g., `./images/`).

2. Update the `image_dir` variable in `convert_images.py` to point to your image directory:

   ```python
   image_dir = "path/to/your/images"
   ```

3. Run the script:

   ```bash
   python convert_images.py
   ```

4. The generated PDF will be saved in the current working directory.

## ⚙️ Configuration

| Variable     | Description                            | Default                  |
|-------------|----------------------------------------|--------------------------|
| `image_dir` | Path to the directory containing images | `./Books`               |
| Output file  | Name of the generated PDF              | `Modern Computer Vision with PyTorch.pdf` |

You can modify these directly in `convert_images.py` to suit your needs.

## 📁 Supported Image Formats

| Format | Extension        |
|--------|-----------------|
| PNG    | `.png`          |
| JPEG   | `.jpg`, `.jpeg` |
| GIF    | `.gif`          |
| BMP    | `.bmp`          |

## 🛠️ Dependencies

| Package   | Version | Purpose                        |
|-----------|---------|--------------------------------|
| [img2pdf](https://pypi.org/project/img2pdf/) | Latest  | Lossless image-to-PDF conversion |

## 📝 Example

```bash
$ python convert_images.py
✅ PDF created successfully: Modern Computer Vision with PyTorch.pdf
```

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> **Note:** This tool performs lossless conversion — images are embedded directly into the PDF without re-compression, ensuring maximum quality.
