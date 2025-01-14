import PySimpleGUI as sg

# 创建布局组件
layout = [
    [sg.Text("编号:", size=(10, 1)), sg.InputText(key='id')],
    [sg.Text("姓名:", size=(10, 1)), sg.InputText(key='name')],
    [sg.Text(key='msg')],
    [sg.Button('关闭'), sg.Button('保存')]
 ]
# 创建窗口
window = sg.Window('我的第一个窗口', layout)
while True:
    # 读取窗口信息
    event, value = window.read()
    if event == '关闭':
        sg.popup('你点击了关闭按钮')
        break
    if event == '保存':
        id = value['id']
        name = value['name']
        window['msg'].update('id:{id}, name:{name}')
        sg.popup(f'id:{id}, name:{name}')
# 释放资源
window.close()
