import cv2

img = cv2.imread('images/renwu02.png')
# 定义参数
# 像素点直径
c = 15
# 颜色权重
color = 25
# 空间权重
space = 15
# 双边滤波
b_img = cv2.bilateralFilter(img, c, color, space)
cv2.imshow('old', img)
cv2.imshow('new', b_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
