import os 
import math
import cv2

img = cv2.imread("task3.jpg")
h, w = img.shape[:2]
ratio = w/h
print("w, h, ratio", w, h, ratio)
r_w = 600
r_h = math.floor(r_w/ratio)
print("resized w, h", r_w, r_h)
resized_img = cv2.resize(img, dsize=(r_w, r_h), interpolation=cv2.INTER_AREA)

out_file_name = "resized_task3.jpg"
cv2.imwrite(out_file_name, resized_img)
file_size = os.path.getsize(out_file_name)
print("file size", file_size, r_w*r_h)