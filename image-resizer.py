from PIL import Image
import os
import re

out_folder = "resized"

# list images in current folder
im_list = [item for item in os.listdir() if re.search("(.jpg|.jpeg|.png)", item) != None]
print("Found Images: \n")
print("#\tName\n")
for index, item in enumerate(im_list):
    print(str(index) + "\t" + item)

print("\n--------------------------------------\n")
print("Maximum Width: ", end="")
max_w = int(input())
print("Maximum Height: ", end="")
max_h = int(input())

# create output folder if it doesn't aready exist
try:
    os.mkdir(out_folder)
except OSError:
    pass

for item in im_list:
    im = Image.open(item)
    (w, h) = im.size

    if w > max_w or h > max_h:
        new_w, new_h = w, h

        if new_w > max_w:
            new_w = min(w, max_w)
            new_h = round(new_w * h / w)
        if new_h > max_h:
            new_w = round(max_h * new_w / new_h)
            new_h = max_h

        res_im = im.resize((new_w, new_h))
        # write resized image
        res_im.save(out_folder + "/" + item) 

print("Done!")  