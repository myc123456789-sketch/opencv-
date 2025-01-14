import cv2
import numpy as np

img = cv2.imread('images/ceshi02.jpg')
# 定义腐蚀参数
k = np.ones((3, 3), np.uint8)
# 腐蚀次数
num = 3
# 腐蚀操作
e_img = cv2.erode(img, k, iterations=num)
cv2.imshow('img', img)
cv2.imshow('E', e_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
