import cv2 

img = cv2.imread("task1.jpg")
print("img dimensions", img.shape)

print("bgr at 2428, 3688", img[2428][3688])
