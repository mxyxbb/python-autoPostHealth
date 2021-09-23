from pymouse import PyMouse
from time import sleep
import pyautogui
import os

import win32gui
import win32con
import win32clipboard as w
import time
import datetime
import os
import requests
from bs4 import BeautifulSoup

def oneday():
    url='http://wufazhuce.com/one/'#每一期的链接共同的部分
    # ran=(datetime.today()-datetime.date()).days+2376
    ran=(datetime.date.today()-datetime.date(2019,3,11)).days+2376
    currenturl=url+str(ran)#当前期的链接
    try:
        res=requests.get(currenturl)
        res.raise_for_status()
    except requests.RequestException as e:#处理异常
        print(e)
    else:
        html=res.text#页面内容
        soup = BeautifulSoup(html,'html.parser')
        b=soup.select('.one-cita')#查找“每日一句”所在的标签
        print(b[0].string.split())
        words=str(b[0].string.split())
        words = words.replace("['", "[").replace("']", "]")
        print(words)
        return words
        
class sendMsg():
    def __init__(self,receiver,msg):
        self.receiver=receiver
        self.msg=msg
        self.setText()
    #设置剪贴版内容
    def setText(self):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
        w.CloseClipboard()
    #发送消息
    def sendmsg(self):
        qq=win32gui.FindWindow(None,self.receiver)
        time.sleep(0.01)
        win32gui.SendMessage(qq,win32con.WM_PASTE , 0, 0) #win32on 见site-packages\win32\lib\win32con.py,有的博文里出现的770对用的就是win32con.WM_PASTE
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

def open_app(app_dir):
    os.startfile(app_dir) # os.startfile（）打开外部应该程序，与windows双击相同

def tell_njust_imhealthy():
    app_dir = r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe'  # 指定应用程序目录
    open_app(app_dir)
    sleep(5)
    # 超级菜鸡的自动填报程序
    m = PyMouse()
    # 参考：https://www.cnblogs.com/gexbooks/p/10790063.html
    weixin_njust_location = pyautogui.locateOnScreen('njust_weixin.png', confidence=0.9)  # 匹配南理工微信坐标
    print(weixin_njust_location)
    njust_x,njust_y = pyautogui.center(weixin_njust_location)
    print(njust_x,njust_y)
    m.click(int(njust_x), int(njust_y))  # 点企业号
    sleep(3)
    weixin_njust_app_location = pyautogui.locateOnScreen('njust_weixin_app.png', confidence=0.9)  # 匹配南理工企业号应用坐标
    weixin_njust_app_x,weixin_njust_app_y = pyautogui.center(weixin_njust_app_location)
    m.click(int(weixin_njust_app_x), int(weixin_njust_app_y))  # 点企业号应用
    sleep(2)
    weixin_njust_assistant_location = pyautogui.locateOnScreen('campus_assistant.png', confidence=0.9)  # 匹配校园助手坐标
    weixin_njust_assistant_location_x,weixin_njust_assistant_location_y = pyautogui.center(weixin_njust_assistant_location)
    m.click(int(weixin_njust_assistant_location_x), int(weixin_njust_assistant_location_y))  # 点校园助手
    sleep(2)
    weixin_window_max_location = pyautogui.locateOnScreen('weixin_windowmax.png', confidence=0.9)  # 匹配微信窗口最大化坐标
    weixin_window_max_x,weixin_window_max_y = pyautogui.center(weixin_window_max_location)
    m.click(int(weixin_window_max_x), int(weixin_window_max_y))  # 点微信窗口最大化
    sleep(2)
    health_location = pyautogui.locateOnScreen('health_link.png', confidence=0.9)  # 匹配健康上报微信坐标
    healthy_x,healthy_y = pyautogui.center(health_location)
    m.click(int(healthy_x), int(healthy_y))  # 点链接
    sleep(10)            # 点完链接多等会
    weixin_window_max_location = pyautogui.locateOnScreen('weixin_windowmax.png', confidence=0.9)  # 匹配窗口最大化坐标
    weixin_window_max_x,weixin_window_max_y = pyautogui.center(weixin_window_max_location)
    m.click(int(weixin_window_max_x), int(weixin_window_max_y))  # 点健康上报窗口最大化
    sleep(2)
    tianxie_location = pyautogui.locateOnScreen('kaishitianxie.png', confidence=0.8, region=(100,850, 1800, 200))  # 匹配开始填写坐标
    tianxie_x,tianxie_y = pyautogui.center(tianxie_location)
    m.click(int(tianxie_x), int(tianxie_y))  # 点填报
    sleep(3.5)
    m.click(int(tianxie_x), int(tianxie_y))  # 激活窗口
    for i in range(0,20):
        pyautogui.press('down')   
    small_location = pyautogui.locateOnScreen('small.png', confidence=0.9)  # 匹配体温坐标
    small_x,small_y = pyautogui.center(small_location)
    m.click(int(small_x), int(small_y))  # 点
    sleep(1.5)
    no_location = pyautogui.locateOnScreen('no.png', confidence=0.9)  # 匹配否坐标
    no_x,no_y = pyautogui.center(no_location)
    m.click(int(no_x), int(no_y))  # 点
    sleep(1.5)
    njust_zi_location = pyautogui.locateOnScreen('tijiao.png')  # 匹配提交坐标
    njust_zi_x,njust_zi_y = pyautogui.center(njust_zi_location)
    m.click(int(njust_zi_x), int(njust_zi_y))  # 点
    sleep(1.5)
    weixin_window_min_location = pyautogui.locateOnScreen('weixin_windowmin.png', confidence=0.9)  # 匹配微信窗口最xiao化坐标
    weixin_window_min_x, weixin_window_min_y = pyautogui.center(weixin_window_min_location)
    m.click(int(weixin_window_min_x),
            int(weixin_window_min_y))  # 点微信窗口最小化(微信bug,最大化窗口时直接关闭，再打开时会处于小化状态，此时没有最大化图标，显示的是最小化图标)
    sleep(2)
    weixin_window_min_location = pyautogui.locateOnScreen('weixin_windowmin.png', confidence=0.9)  # 匹配微信窗口最xiao化坐标
    weixin_window_min_x, weixin_window_min_y = pyautogui.center(weixin_window_min_location)
    m.click(int(weixin_window_min_x),
            int(weixin_window_min_y))  # 点微信窗口最小化(微信bug,最大化窗口时直接关闭，再打开时会处于小化状态，此时没有最大化图标，显示的是最小化图标)
    sleep(2)
    weixin_window_close_location = pyautogui.locateOnScreen('weixin_windowclose.png', confidence=0.9)  # 匹配微信关闭窗口坐标
    weixin_window_close_x, weixin_window_close_y = pyautogui.center(weixin_window_close_location)
    m.click(int(weixin_window_close_x),
            int(weixin_window_close_y))  # 关闭报平安窗口
    sleep(2)
    weixin_window_close_location = pyautogui.locateOnScreen('weixin_windowclose.png', confidence=0.9)  # 匹配微信关闭窗口坐标
    weixin_window_close_x, weixin_window_close_y = pyautogui.center(weixin_window_close_location)
    m.click(int(weixin_window_close_x),
            int(weixin_window_close_y))  # 关闭微信窗口
    sleep(2)
    

if __name__ == "__main__":
    # 获取时间
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
    receiver = '自动化 19 杨城彰 '
    start_str = time_str+" python:开始健康上报"
    # 发送QQ消息，告知开始报平安
    qq = sendMsg(receiver, start_str)
    qq.sendmsg()
    
    if(curr_time.hour > 15):
        curr_word = oneday()
        qq = sendMsg(receiver, curr_word)
        qq.sendmsg()
    
    # 执行健康上报流程
    tell_njust_imhealthy()
    
    # 重新获取时间，发送QQ消息，告知报平安完成
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
    end_str = time_str + " python:已成功填报"
    qq = sendMsg(receiver, end_str)
    qq.sendmsg()
    



