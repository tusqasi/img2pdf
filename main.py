import os
import sys
from pathlib import Path
from PIL import Image


def save_to_pdf(pdf_file_path: Path, images: list[Image.Image]) -> None:
    images[0].save(
        pdf_file_path / "pdf_export_file.pdf",
        "PDF",
        resolution=100.0,
        save_all=True,
        append_images=images[1:],
    )


def main():
    extensions: list[str] = [
        ".jpg",
        ".jpeg",
        ".png",
    ]
    # if has 2 args out put is set
    # if has 1 arg out put is not set
    images_folder: Path = Path.cwd()
    pdf_export_path: Path = Path.cwd()
    if len(sys.argv) >= 2:
        images_folder = Path(sys.argv[1])
    if len(sys.argv) == 3:
        pdf_export_path = Path(sys.argv[2])

    # finds the image files with extensions in the list extensions
    imgs = list()
    for file in Path.iterdir(images_folder):
        if file.suffix.lower() in extensions:
            imgs.append(Image.open(f"{file}").convert("RGB"))
    if len(imgs) == 0:
        print(f"No images in {images_folder}\nExiting")
        return 0

    save_to_pdf(pdf_export_path, imgs)
    print("Done")


if __name__ == "__main__":
    main()
