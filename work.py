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


d = 0
cap = cv2.VideoCapture(0)

c = (1, 2)
f = cv2.FONT_HERSHEY_PLAIN
size = 2
w = 3
color = (0, 0, 255)
font_path = "font/simhei.ttf"

img = cv2.imread('images/car2.png')


def mytest01(event, x, y, flag, param):
    # 鼠标左键按下事件
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 0, 255), 1)


def mytest(event, x, y, flag, param):
    global d
    if event == cv2.EVENT_LBUTTONDOWN:
        d += 1


cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 500, 300)

while True:
    text = f"感谢老铁，火箭{d}"  # text放到循环里面，实时更新数据
    ret, frame = cap.read()
    c_img = put_text(frame, text, c, font_path, 30, color)
    if ret:
        cv2.imshow('video', c_img)
        cv2.setMouseCallback('video', mytest)
    if cv2.waitKey(2) == 27:
        break
cv2.destroyAllWindows()
