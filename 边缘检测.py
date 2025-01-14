import cv2

img = cv2.imread('images/wenzi01.jpeg')


# 灰度图像
gay_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 定义阈值
lower = 255
upper = 300
# 获取边缘信息
canny_img = cv2.Canny(gay_img, lower, upper)
# c = 15
# # 颜色权重
# color = 25
# # 空间权重
# space = 15
# # 双边滤波
# b_img = cv2.bilateralFilter(canny_img, c, color, space)
k = (3, 3)
# 标准差
d = 1
# 高斯去噪
gs_img = cv2.GaussianBlur(canny_img, k, d)
# 创建窗口函数，image窗口名称，cv2.WINDOW_NORMAL允许手动调整窗口大小（方便调试）
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 设置窗口大小，image窗口名称，和namedWindow的窗口名称一致
cv2.resizeWindow('image', 800, 600)
cv2.imshow('image', gs_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
