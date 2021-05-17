import os
from PIL import Image

all_files = os.listdir("./")
imgs = [x for x in all_files if x[-3:] == "jpg"]
from PIL import Image

im1 = Image.open(imgs[0])
imgs.remove(0)
im_list = [ Image.open(f"./{x}") for x in imgs]
pdf1_filename = "new.pdf"

im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
# makePdf("test_pdf.pdf", imgs, )

