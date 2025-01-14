import cv2
import numpy
import numpy as np

img = np.zeros((200, 500, 3), dtype=np.uint8)
# 定义绘制矩形的左上坐标
left_top = (100, 100)
# 定义绘制矩形的右下角坐标
right_bottom = (200, 200)
# 定义颜色
color = (5, 5, 50)
w = 5
r_img = cv2.rectangle(img, left_top, right_bottom, color, w)
cv2.imshow('a', r_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
