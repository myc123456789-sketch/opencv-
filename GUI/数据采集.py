import mysql
import cv2
import PySimpleGUI as sg


# 数据采集窗口

def dataget():
    # 开摄像头
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == False:
        print('摄像头没开')
        return
        #
    layout = [
        [sg.Text('编号：'), sg.InputText(key='num')],
        [sg.Text('姓名'), sg.InputText(key='name')],
        [sg.Image(key='video')],
        [sg.Button('关闭'), sg.Button('人脸采集')]

    ]

    window = sg.Window('人脸信息采集', layout)

    while True:
        event, values = window.read(timeout=10)
        ret, frame = cap.read()
        if event in (None, '关闭'):
            break
        if ret:
            imgType = cv2.imencode('.png', frame)[1].tobytes()
            window['video'].update(data=imgType)

        if event == '人脸采集':
            # 获取编号姓名
            num = values['num']
            name = values['name']
            # 写入人脸图片
            iss = cv2.imwrite(f'D:\\images\\{id}.png', frame)
            if iss:
                isAdd = mysql.add(name, num)
                if isAdd:
                    sg.popup('人脸采集成功')
            else:
                sg.popup('人脸采集失败')
    cap.release()
    window.close()


dataget()
