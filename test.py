import os
import sys
from PIL import Image


def main():
    all_files = os.listdir("./hw")
    extensions = [
        "jpg",
        "jpeg",
        "png",
    ]
    imgs = [f"hw/{x}" for x in all_files if x[-3:].lower() in extensions]
    im_list = [Image.open(f"./{x}").convert("RGB") for x in imgs[1:]]
    im1 = Image.open(imgs[0]).convert("RGB")
    pdf1_filename = f"{sys.argv[0]}.pdf"
    print(sys.argv)

    im1.save(
        pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list
    )


if __name__ == "__main__":
    main()
