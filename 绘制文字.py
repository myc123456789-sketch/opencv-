import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def put_text(image, text, position, font_path, font_size, color):
    # 将 OpenCV 图像转换为 PIL 图像
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(pil_image)

    # 加载字体
    font = ImageFont.truetype(font_path, font_size)

    # 在图像上绘制文本
    draw.text(position, text, fill=color, font=font)

    # 将 PIL 图像转换回 OpenCV 图像
    image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    return image_with_text


img = cv2.imread('images/car.png')
# 定义文字内容和位置
# 定义字体
text = "hello world"
# 起始坐标
c = (1, 2)
# 字体格式
f = cv2.FONT_HERSHEY_PLAIN
# 字体大小
size = 2
# 字体粗细
w = 3
# color
color = (0, 0, 255)
# 写字
# c_img = cv2.putText(img, text=text, org=c, fontScale=size, fontFace=f, color=color, thickness=w)
font_path = "font/simhei.ttf"
c_img = put_text(img, "你好，世界", c, font_path, 30, color)
cv2.imshow('img', c_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
