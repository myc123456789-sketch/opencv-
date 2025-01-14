import cv2
import face_recognition

# 开启摄像头
c = cv2.VideoCapture(0)

while True:
    ret, frame = c.read()
    face_locations = face_recognition.face_locations(frame)
    print(face_locations)
    for (top, right, bottom, left) in face_locations:
        # 画出人脸区域
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        qg_image = frame[top:bottom, left:right]


    if ret:
        # 显示图
        cv2.imshow("a", frame)
    if cv2.waitKey(20) == 27:
        break
    if cv2.waitKey(20) == 113:
        #保存人脸
        iss = cv2.imwrite("D:\\images\\renlian01.png", frame)
        if iss:
            print("收集人脸成功")
        else:
            print("收集人脸失败")
cv2.destroyAllWindows()
