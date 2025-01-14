import cv2
import numpy as np

# 读取图片
# img = cv2.imread('images/car.png')
img = np.zeros((300, 500, 3), dtype=np.uint8)
# 保存图片，imwrite(保存图片路径，图像矩阵），返回值是布尔
iss = cv2.imwrite('save_image/car01.png', img)
if iss:
    print('保存成功')
else:
    print('保存失败')
