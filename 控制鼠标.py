import cv2


# event是鼠标事件，x，y是鼠标所在区域的坐标
# flag 是标识
# param 参数

def mytest(event, x, y, flag, param):
    print(f"坐标{(x, y)}")
    print(f"flag={flag}")
    print(f"param={param}")


img = cv2.imread('images/car.png')
# 定义窗口
cv2.namedWindow('name')

# 设置执行鼠标操作的回调函数
cv2.setMouseCallback('name', mytest)
#
