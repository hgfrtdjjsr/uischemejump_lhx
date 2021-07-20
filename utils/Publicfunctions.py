# -*- coding: utf-8 -*-
from appium import webdriver

import os
import time

platformVersion = os.popen('adb shell getprop ro.build.version.release').read().rstrip()
platformName = 'Android'
def Unlocking():
    a = os.popen('adb   shell dumpsys window policy|grep screenState').read()
    if "SCREEN_STATE_OFF" in a:
        os.popen('adb  shell input keyevent 26')
        time.sleep(1)
        os.popen('adb  shell input swipe 110 1800 110 100 500' )
    else:
        os.popen('adb shell input swipe 110 1800 110 100 500' )



def appium_start():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = 'Android'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['fullReset'] = False
    desired_caps['noReset'] = True
    desired_caps['recreateChromeDriverSessions'] = True
    desired_caps['appPackage'] = 'com.kwai.m2u'
    desired_caps['appActivity'] = '.launch.LaunchActivity'

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    return driver

def appium_start1():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = 'Android'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['fullReset'] = False
    desired_caps['noReset'] = True
    desired_caps['recreateChromeDriverSessions'] = True
    desired_caps['appPackage'] = 'ca.zgrs.clipper'
    desired_caps['appActivity'] = '.Main'

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    return driver

def uninstallapk(self):
    if self.driver.is_app_installed("com.kwai.m2u"):  # 判断指定APP是否已安装
        print("已安装一甜，现在执行卸载")
        self.driver.remove_app("com.kwai.m2u")  # 删除指定APP
    else:
        print("未安装一甜，现在执行安装")

def installapk(self, failname):
    self.driver.install_app(failname)  # 安装APP，需指定apk安装包路径
    self.driver.quit()

def get_windowsize(self, x1, y1, x2, y2):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    self.driver.swipe(x1 * x, y1 * y, x2 * x, y2 * y, 1000)

def isElement(self,identifyBy,c, multipe = False, wait = 10):
    '''
    一个元素是否存在，考虑到网络、性能等因素，如果10s一个元素还未检测到，说明没有这个元素
    Usage:
    isElement(By.XPATH,"//a")
    :param self:
    :param identifyBy:
    :param c:
    :return:
    '''
    time.sleep(1)
    flag=None
    wait_count = 1
    while(wait_count < wait):
        if(flag == False or flag == None):
            time.sleep(1)
            try:
                if multipe == False:
                    if identifyBy == "id":
                        self.driver.find_element_by_id(c)
                    elif identifyBy == "xpath":
                        self.driver.find_element_by_xpath(c)
                    elif identifyBy == "class":
                        self.driver.find_element_by_class_name(c)
                    elif identifyBy == "link text":
                        self.driver.find_element_by_link_text(c)
                    elif identifyBy == "partial link text":
                        self.driver.find_element_by_partial_link_text(c)
                    elif identifyBy == "name":
                        self.driver.find_element_by_name(c)
                    elif identifyBy == "tag name":
                        self.driver.find_element_by_tag_name(c)
                    elif identifyBy == "css selector":
                        self.driver.find_element_by_css_selector(c)
                    elif identifyBy == "text":
                        self.driver.find_element_by_android_uiautomator("text(\"%s\")" % c)
                    flag = True
                if multipe == True:
                    if identifyBy == "id":
                        self.driver.find_elements_by_id(c)
                    elif identifyBy == "xpath":
                        self.driver.find_elements_by_xpath(c)
                    elif identifyBy == "class":
                        self.driver.find_elements_by_class_name(c)
                    elif identifyBy == "link text":
                        self.driver.find_elements_by_link_text(c)
                    elif identifyBy == "partial link text":
                        self.driver.find_elements_by_partial_link_text(c)
                    elif identifyBy == "name":
                        self.driver.find_elements_by_name(c)
                    elif identifyBy == "tag name":
                        self.driver.find_elements_by_tag_name(c)
                    elif identifyBy == "css selector":
                        self.driver.find_elements_by_css_selector(c)
                    elif identifyBy == "text":
                        self.driver.find_element_by_android_uiautomator("text(\"%s\")" % c)
                    flag = True
            except:
                # logger.error(traceback.format_exc())
                flag = False

        wait_count += 1

    return flag
