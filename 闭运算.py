import cv2
import numpy as np

img = cv2.imread('images/bi01.jpeg')

# 定义开运算的卷积核
k = np.ones((9, 9), np.uint8)
# 闭运算，先膨胀后腐蚀
close_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
# 展示
cv2.imshow('a', img)
cv2.imshow('b', close_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
