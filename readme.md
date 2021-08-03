# 自动向理报平安

- 依赖环境：pywin32、python-opencv、pyhook、pyautogui、pyuserinput

- 仓库地址：[mxyxbb/python-autoPostHealth: 自动向理报平安 (github.com)](https://github.com/mxyxbb/python-autoPostHealth)

- 主要方法：

1. 使用`pyuserinput`中的`pymouse`进行鼠标操作
2. 使用`pyautogui`的`locateOnScreen`方法进行图像匹配，依赖opencv
   ![health_link](https://i.loli.net/2021/08/03/IROnh3UFWHTfzEC.png) ![njust_weixin_app](https://i.loli.net/2021/08/03/jXTD1m7NIb8hYeG.png) ![weixin_windowmax](https://i.loli.net/2021/08/03/SprfFdycJPY2aXH.png) ![weixin_windowclose](https://i.loli.net/2021/08/03/Un6oym1IQjgO9K4.png) ![weixin_windowmin](https://i.loli.net/2021/08/03/bcPL7qGvOASZItR.png)![njust_weixin](https://i.loli.net/2021/08/03/123eutl597RXfSy.png)
3. 使用`mouseclick.py`可以打印出鼠标的当前坐标，用于调试

- 其它说明：使用前安装好依赖包，确保自己的微信已经登陆，打开时能在屏幕上看到南理工企业号的图标即可。(本程序是在屏幕范围内进行识别的)