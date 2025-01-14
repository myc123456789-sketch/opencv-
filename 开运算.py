import cv2
import numpy as np

img = cv2.imread('images/kai.jpg')

# 定义开运算的卷积核
k = np.ones((7, 7), np.uint8)
# 开运算，先腐蚀后膨胀
open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, k)
# 展示
cv2.imshow('a', img)
cv2.imshow('b', open_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
