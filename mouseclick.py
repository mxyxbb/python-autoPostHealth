import  os
import  time
import  pyautogui as pg
import  win32api
import  win32con

try:
    while True:
        sW, sH = pg.size()  #获取屏幕的尺寸（像素）screenWidth，screenHeight
        print("屏幕分辨率：\n"+str(sW)+','+str(sH)+'\n')  #打印屏幕分辨率
        x,y = pg.position()   #获取当前鼠标的坐标（像素）
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-1)
        print("鼠标坐标:\n" + str(x).rjust(4)+','+str(y).rjust(4)) #打印鼠标坐标值
        pg.press('down')
        print('down')
        time.sleep(2) #等待1秒
        os.system('cls')   #清屏
except KeyboardInterrupt:
    print('\n结束')