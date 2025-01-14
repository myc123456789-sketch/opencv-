import cv2

# event是鼠标事件，x，y是鼠标所在区域的坐标
# flag 是标识
# param 参数
d = 0


def mytest(event, x, y, flag, param):
    # 鼠标左键按下事件
    global d
    if event == cv2.EVENT_LBUTTONDOWN:
        print('鼠标按下')
        d = True
        # cv2.circle(img, (x, y), 10, (0, 0, 255), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        print('鼠标左键释放')
        d = False
    elif event == cv2.EVENT_MOUSEMOVE:
        print('鼠标移动')
        if d:
            cv2.circle(img, (x, y), 10, (0, 0, 255), 1)


img = cv2.imread('images/car.png')
# 定义窗口
cv2.namedWindow('name')

# 设置执行鼠标操作的回调函数
cv2.setMouseCallback('name', mytest)
while True:
    cv2.imshow('name', img)
    # 按ESC退出
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()

#
