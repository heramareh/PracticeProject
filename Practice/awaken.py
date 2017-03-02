#encoding-utf-8

import os
import time
import win32api
import win32con
import win32clipboard as w
from pymouse import PyMouse
from pywinauto import application

def getText():
    u'''获得剪贴板内容'''
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    u'''设置剪贴板内容'''
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

def ctrl_V():
    u'''粘贴快捷键Ctrl+V'''
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(86,0,0,0)
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

def enter():
    u'''回车键'''
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
    
def move_mouse(start_x,start_y,end_x,end_y):
    u'''移动鼠标'''
    m = PyMouse()
    m.position()
    m.move(start_x,start_y)
    time.sleep(1)
    m.move(end_x,end_y)

def kill(name):
    u'''杀掉进程'''
    ret = os.system('tasklist | find "%s"' %name)
    if ret == 0:
        print u'目标进程存在，杀死该进程'
        os.system('taskkill /F /IM "%s"' %name)
    else:
        print u'目标进程不存在'

def awaken(url,pwd):
    u'''唤醒虚拟机操作'''
    application.Application.start(r'C:\VirtViewer\bin\remote-viewer.exe')  #启动应用
    time.sleep(2)
    setText(url)
    ctrl_V()
    time.sleep(2)
    enter()
    time.sleep(5)
    if pwd == "":
        pass
    else:
        setText(pwd)
        ctrl_V()
        time.sleep(1)
        enter()
        time.sleep(3)
    move_mouse(960,540,980,500)
    time.sleep(3)
    kill("remote-viewer.exe")

if __name__ == '__main__':
    print '-'*10+'start time: ',
    print time.ctime(),
    print '-'*10
    url_pwd_dict = {"spice://10.2.31.121:5901":"2480", "spice://10.2.31.1:5954":"2480", "spice://10.2.31.121:5958":""}
    time.sleep(3)
    awaken("spice://10.2.31.121:5901", "2480")
    while True:
        for url,pwd in url_pwd_dict.items():
            time.sleep(2)
            awaken(url, pwd)
            time.sleep(2)
        date = time.ctime()
        print '-'*10,
        print date,
        print '-'*10
        hour = date[-13:-11]
        print
        # 到下午5点时停止唤醒
        if hour == '17':
            break
        time.sleep(300)
    print '-'*10+'end time: ',
    print time.ctime(),
    print '-'*10