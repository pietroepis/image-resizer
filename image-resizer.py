from PIL import Image
import os
import re

im_list = [item for item in os.listdir() if re.search("(.jpg|.jpeg|.png)", item) != None]
print("Found Images: \n")
print("#\tName\n")
for index, item in enumerate(im_list):
    print(str(index) + "\t" + item)

print("Maximum Width: ", end="")
max_w = int(input())

os.mkdir("resized")

for item in im_list:
    im = Image.open(item)
    (w, h) = im.size
    
    if w > max_w:
        res_im = im.resize((max_w, round(max_w * h / w)))
        res_im.save("resized/" + item)      

print("Done!")  