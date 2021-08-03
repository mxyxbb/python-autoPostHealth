from pymouse import PyMouse
from time import sleep
import pyautogui
import os


def open_app(app_dir):
    os.startfile(app_dir) # os.startfile（）打开外部应该程序，与windows双击相同


if __name__ == "__main__":
    app_dir = r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe'  # 指定应用程序目录
    open_app(app_dir)
    sleep(1)

    # 超级菜鸡的自动填报程序
    m = PyMouse()
    # 参考：https://www.cnblogs.com/gexbooks/p/10790063.html
    weixin_njust_location = pyautogui.locateOnScreen('njust_weixin.png', confidence=0.9)  # 匹配南理工微信坐标
    print(weixin_njust_location)
    njust_x,njust_y = pyautogui.center(weixin_njust_location)
    print(njust_x,njust_y)
    m.click(int(njust_x), int(njust_y))  # 点企业号
    sleep(1)
    weixin_njust_app_location = pyautogui.locateOnScreen('njust_weixin_app.png', confidence=0.9)  # 匹配南理工企业号应用坐标
    weixin_njust_app_x,weixin_njust_app_y = pyautogui.center(weixin_njust_app_location)
    m.click(int(weixin_njust_app_x), int(weixin_njust_app_y))  # 点企业号应用
    sleep(0.5)
    m.click(int(weixin_njust_app_x), int(weixin_njust_app_y+100))  # 点校园助手
    sleep(1)
    weixin_window_max_location = pyautogui.locateOnScreen('weixin_windowmax.png', confidence=0.9)  # 匹配微信窗口最大化坐标
    weixin_window_max_x,weixin_window_max_y = pyautogui.center(weixin_window_max_location)
    m.click(int(weixin_window_max_x), int(weixin_window_max_y))  # 点微信窗口最大化
    sleep(1)
    health_location = pyautogui.locateOnScreen('health_link.png', confidence=0.9)  # 匹配健康上报微信坐标
    healthy_x,healthy_y = pyautogui.center(health_location)
    m.click(int(healthy_x), int(healthy_y))  # 点链接
    sleep(2)            # 点完链接多等会
    m.click(950, 660)   # 点填报
    sleep(1)
    m.click(1150, 740)   # 点体温
    sleep(0.5)
    m.click(1150, 830)   # 点咳嗽
    sleep(0.5)
    m.click(1150, 893)   # 点上报
    sleep(0.5)
    weixin_window_min_location = pyautogui.locateOnScreen('weixin_windowmin.png', confidence=0.9)  # 匹配微信窗口最大化坐标
    weixin_window_min_x, weixin_window_min_y = pyautogui.center(weixin_window_min_location)
    m.click(int(weixin_window_min_x),
            int(weixin_window_min_y))  # 点微信窗口最小化(微信bug,最大化窗口时直接关闭，再打开时会处于小化状态，此时没有最大化图标，显示的是最小化图标)
    sleep(1)
    weixin_window_close_location = pyautogui.locateOnScreen('weixin_windowclose.png', confidence=0.9)  # 匹配微信关闭窗口坐标
    weixin_window_close_x, weixin_window_close_y = pyautogui.center(weixin_window_close_location)
    m.click(int(weixin_window_close_x),
            int(weixin_window_close_y))  # 关闭报平安窗口
    sleep(1)
    weixin_window_close_location = pyautogui.locateOnScreen('weixin_windowclose.png', confidence=0.9)  # 匹配微信关闭窗口坐标
    weixin_window_close_x, weixin_window_close_y = pyautogui.center(weixin_window_close_location)
    m.click(int(weixin_window_close_x),
            int(weixin_window_close_y))  # 关闭微信窗口
    sleep(1)

# m = PyMouse()
    # m.click(470, 1060) # 从下面的任务栏点微信
    # sleep(1)
    # m.click(170, 90)  # 点企业号
    # sleep(1)
    # m.click(1160, 110)  # 点企业号应用
    # sleep(0.5)
    # m.click(620, 200)  # 点校园助手
    # sleep(1)
    #
    # m.click(1500, 960)  # 点链接
    # sleep(2)            # 点完链接多等会
    # m.click(950, 660)   # 点填报
    # sleep(1)
    # m.click(1150, 740)   # 点体温
    # sleep(0.5)
    # m.click(1150, 830)   # 点咳嗽
    # sleep(0.5)
    # m.click(1150, 893)   # 点上报
    # sleep(0.5)


