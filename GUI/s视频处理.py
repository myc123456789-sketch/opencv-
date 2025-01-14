import cv2
import PySimpleGUI as sg


#
def demo():
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == False:
        print('没有开摄像头')
        return
    layout = [
        [sg.Button('关闭'), sg.Button('保存')],
        [sg.Image(key='video')]
    ]
    window = sg.Window('视频处理', layout)
    while True:
        event, values = window.read(timeout=10)
        # 读取数据帧
        ret, frame = cap.read()
        print(event)
        if event in (None, '关闭'):
            break
        if ret:
            imgType = cv2.imencode('.png', frame)[1].tobytes()
            window['video'].update(data=imgType)
    cap.release()
    window.close()


if __name__ == '__main__':
    demo()
