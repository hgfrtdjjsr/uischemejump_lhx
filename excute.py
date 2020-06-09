#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : lixinyan

from utils.Publicfunctions import *
import time
import os
import warnings
import traceback
import json
import argparse
from utils.ConfigInfo import *
from utils.report import *
import datetime

class m2utestcase():
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = appium_start()
        time.sleep(3)

    def test_startapp(self):
        time.sleep(3)
        imgs = ''
        try:
            time.sleep(10)
            shot = self.driver.get_screenshot_as_base64()
            imgs = shot
        except Exception as e:
            print('错误日志：' + str(e))
            traceback.print_exc()
        finally:
            return imgs

    def test_clipper(self, casenum):
        startservice = os.popen('adb shell am startservice ca.zgrs.clipper/.ClipboardService').read()
        if 'Error' in startservice:
            print('未启动广播服务，请检查')
        else:
            adbtext = os.popen("adb shell am broadcast -a clipper.set -e text \"%s\"" % ('\'' + baseConfig[casenum]+ '\'')).read()
            print('\'' + baseConfig[casenum]+ '\'')
            print(adbtext)


    def tearDown(self):
        self.driver.quit()

    def execute(self):
        filename = 'img.txt'
        crashlog = os.popen("adb logcat *:F | grep \"com.kwai.m2u\"")
        imgs = []
        for casenum in range(len(baseConfig)):
            self.test_clipper(casenum)
            self.setUp()
            time.sleep(3)
            img = self.test_startapp()
            time.sleep(3)
            imgs.append(img)
        os.system("ps -ef | grep logcat | grep -v grep | awk '{print $2}' | xargs kill -9")
        crashLog = str(crashlog.read())
        crashlog.close()
        with open(filename, 'w') as file:
            file.write(json.dumps(imgs))
        a = '/Users/lidoudou/PycharmProjects/uischemejump/img.txt'
        with open(a, 'r') as file:
            imgsdict = file.readline()
        createhtml(imgs, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'imgs', crashLog)



if __name__ == "__main__":
    m2utestcase = m2utestcase()
    m2utestcase.execute()
