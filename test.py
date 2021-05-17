import os
from PIL import Image


def main():
    all_files = os.listdir("./hw")
    extensions = [
        "jpg",
        "jpeg",
        "png",
    ]
    imgs = [x for x in all_files if x[-3:].lower() in extensions]
    im1 = Image.open(imgs[0])
    im_list = [Image.open(f"./hw/{x}").convert("RGB") for x in imgs]
    pdf1_filename = "new.pdf"

    im1.save(
        pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list
    )


if __name__ == "__main__":
    main()
