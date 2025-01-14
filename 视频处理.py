import cv2

# 0:开启摄像头,参数如果视频路径是开启
cap = cv2.VideoCapture(0)
# 创建窗口函数，image窗口名称，cv2.WINDOW_NORMAL允许手动调整窗口大小（方便调试）
cv2.namedWindow('name', cv2.WINDOW_NORMAL)
# 设置窗口大小，image窗口名称，和namedWindow的窗口名称一致
cv2.resizeWindow('name', 500, 300)
while True:
    # 读取视频,ret 是否读取到视频，frame：图片（帧）

    ret, frame = cap.read()
    if ret:
        cv2.imshow('name', frame)
        #
    if cv2.waitKey(2) == 27:
        break
cv2.destroyAllWindows()
