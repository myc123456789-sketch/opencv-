import cv2
import numpy as np

img = np.zeros((300, 500, 3), dtype=np.uint8) + 255

d = 0


def mytest01(event, x, y, flag, param):
    global d
    if event == cv2.EVENT_LBUTTONDOWN:
        d = True
    elif event == cv2.EVENT_LBUTTONUP:
        d = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if d :
            cv2.circle(img, (x, y), 10, (0, 0, 255), -1)


cv2.namedWindow('name')

# 设置执行鼠标操作的回调函数
cv2.setMouseCallback('name', mytest01)
while True:

    cv2.imshow('name', img)

    # 按ESC退出
    if cv2.waitKey(20) == 27:
        break
    # q Q 键保存
    elif cv2.waitKey(20) == 113 or cv2.waitKey(20) == 81:
        cv2.imwrite('save_image/car02.png', img)
        print('保存成功')

cv2.destroyAllWindows()
