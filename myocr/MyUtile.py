import paddlehub as hub
import cv2
import numpy as np


def license_plate_orc(img):
    # 读取图片
    img = cv2.imread(img)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([100, 100, 50])
    upper = np.array([140, 255, 255])
    img3 = cv2.inRange(img2, lower, upper)
    contours, hierarchy = cv2.findContours(img3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img4 = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # 这个可以打印xywh  宽高看最大的一个框 肯定就是最大的边界
        # print(x, y,w, h)
        if w > 100 and h > 50:
            img5 = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 100, 0), 2)
            # 可以裁剪出来
            img4 = img5[y:y + h, x:x + w]
    # 加载模型 实例化 bool=False 设置是否用显卡运行
    ocr = hub.Module(name="chinese_ocr_db_crnn_server")  # 有chinese_ocr_db_crnn_mobile 选项为轻量级模型
    # 识别图片的文字 调用模型对象的recognize_text 方法 传入img数组 返回的结果是一个json数据
    results = ocr.recognize_text(images=[img4])

    return (results[0]["data"][0]["text"]), results[0]["data"][0]['confidence']
