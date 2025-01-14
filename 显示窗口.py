import cv2
import os


def demo01():
    # 创建窗口函数，image窗口名称，cv2.WINDOW_NORMAL允许手动调整窗口大小（方便调试）
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # 设置窗口大小，image窗口名称，和namedWindow的窗口名称一致
    cv2.resizeWindow('image', 500, 300)
    # 读取图片，imread（图片路径）
    # 1.支持绝对路径和相当路径，2.图片路径不能有中文，
    # 3.路径如果有转义字符，用r""表达式进行
    image = cv2.imread('images/car.png')
    if image is None:
        print('图片不存在')
        return
        # 用窗口显示图片
    cv2.imshow('image', image)
    # 等待键盘操作，0代表无限等待，waitKey返回ASCII值

    cv2.waitKey(0)
    # 释放资源
    cv2.destroyAllWindows()


# demo01()

# 简写：
def demo02():
    # 读取图片，imread（图片路径）
    # 1.支持绝对路径和相当路径，2.图片路径不能有中文，
    # 3.路径如果有转义字符，用r""表达式进行
    image = cv2.imread('images/car.png')
    if image is None:
        print('图片不存在')
        return
        # 用窗口显示图片
    cv2.imshow('image', image)
    # 等待键盘操作，0代表无限等待，waitKey返回ASCII值

    cv2.waitKey(0)
    # 释放资源
    cv2.destroyAllWindows()


demo02()
