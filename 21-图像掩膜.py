import cv2
import numpy as np

img = cv2.imread("images/car3.png")
# 把图像转换成HSV空间
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 获取蓝色所在的HSV范围
lower = np.array([100, 100, 90])
height = np.array([140, 255, 255])
# 创建掩膜
# hsv_img 输入的图像是HSV图像
mask = cv2.inRange(hsv_img, lower, height)
cv2.imshow("b", img)
cv2.imshow("a", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
