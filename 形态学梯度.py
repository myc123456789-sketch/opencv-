import cv2
import numpy as np

img = cv2.imread('images/shenfen03.jpg')

# 定义卷积核
# import cv2
# import numpy as np
#
# img = cv2.imread('images/bi01.jpeg')
#
# # 定义开运算的卷积核
# k = np.ones((9, 9), np.uint8)
# # 闭运算，先膨胀后腐蚀
# close_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
# # 展示
# cv2.imshow('a', img)
# cv2.imshow('b', close_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
k = np.ones((3, 3), np.uint8)
# 形态学梯度
close_img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)
# 展示
cv2.imshow('a', img)
cv2.imshow('b', close_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
