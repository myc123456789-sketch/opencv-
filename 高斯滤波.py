import cv2

img = cv2.imread('images/renwu01.jpeg')
# 定义滤波参数
# 高斯核，必须是奇数
k = (3, 3)
# 标准差
d = 2
# 高斯去噪
gs_img = cv2.GaussianBlur(img, k, d)
cv2.imshow('old', img)
cv2.imshow('new', gs_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
