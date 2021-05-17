import os
import sys
from PIL import Image


def main():
    folder = sys.argv[1]
    all_files = os.listdir(f"./{folder}")
    extensions = [
        "jpg",
        "jpeg",
        "png",
        "webp",
        "tiff",
    ]
    imgs = [f"{folder}/{x}" for x in all_files if x[-3:].lower() in extensions]
    im_list = [Image.open(f"./{x}").convert("RGB") for x in imgs[1:]]
    im1 = Image.open(imgs[0]).convert("RGB")
    pdf1_filename = f"{sys.argv[0]}.pdf"

    im1.save(
        pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list
    )
    input("wa9t")

if __name__ == "__main__":
    main()
