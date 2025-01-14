import cv2
import numpy
import numpy as np


def mytest(event, x, y, flag, param):
    global image
    if event == cv2.EVENT_LBUTTONUP:
        img01 = cv2.circle(image, (x, y), 10, (0, 0, 255), -1)
        iss = cv2.imwrite('save_image/car01.png', img01)
        if iss:
            print('保存成功')
        else:
            print('保存失败')


def test01():
    # 创建图片矩阵
    # 300,是图片高度，500，图片宽度，3，通道（RGB）1是灰色图像
    image = np.zeros((300, 500, 3), dtype=np.uint8) + 255
    print(image)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


test01()
