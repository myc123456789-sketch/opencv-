import cv2
import face_recognition
import os
import numpy as np

# 开启摄像头
c = cv2.VideoCapture(0)

while True:
    ret, frame = c.read()
    if ret:
        # 显示图
        cv2.imshow("a", frame)

    if cv2.waitKey(20) == 27:
        break
    if cv2.waitKey(20) == 113:
        # 检测人脸
        face_list = face_recognition.face_locations(frame)
        print(len(face_list))
        if len(face_list) > 0:
            print("检测到人脸")
            # 遍历目录，查找人脸
            path = os.listdir("D:\\images")
            print(path)
            for i in path:
                # 获取人脸特征
                img = cv2.imread(f"D:\\images\\{i}")
                en1 = face_recognition.face_encodings(img)[0]
                en2 = face_recognition.face_encodings(frame)[0]
                iss = np.linalg.norm(en1 - en2)
                print(iss)
                if iss < 0.5:
                    print("是同一个人")
                else:
                    print("不是同一个人")

cv2.destroyAllWindows()
