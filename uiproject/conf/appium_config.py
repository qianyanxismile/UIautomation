import os
import sys
import time
import re
from appium import webdriver

#sys.path.append("..")
# 用于解决多个手机连接问题
#from common.mobile import get_serialno
# Read mobile deviceId
#device_id = get_serialno()

# Read mobile os Version
#os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()


def appium_start():
    config = {
        "platformName": "Android",
        "platformVersion": "8.0.0",
        "deviceName": "5R4C17B17001096",
        "appPackage": "com.jifen.qukan",
        "appActivity": "com.jifen.qkbase.main.MainActivity",
        "automationName": "UIAutomator2",
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "noReset": True,
        "autoLaunch": True

    }
    return webdriver.Remote('http://localhost:4723/wd/hub', config)


if __name__ == "__main__":
    appium_start()