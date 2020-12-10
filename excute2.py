#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : lixinyan
"""html文件跳转"""
from utils.Publicfunctions import *
import time
import os
import warnings
import traceback
import json
import argparse
from utils import ConfigInfo1
from utils.report1 import *
import datetime
import base64
from skimage.metrics import structural_similarity
import cv2

class m2utestcase():
    #
    #
    # def setUp(self):
    #

    def execute(self):
        # 打开浏览器
        imgs = []
        self.driver = appium_start()
        time.sleep(3)
        os.popen('adb shell am start -a android.intent.action.VIEW -d content://com.tencent.mobileqq.fileprovider/external_files/storage/emulated/0/Android/data/com.tencent.mobileqq/Tencent/QQfile_recv/H5.html')
        for i in range(len(ConfigInfo1.tapy)):
            os.popen('adb shell input tap %s %s ' % (ConfigInfo1.tapx[0], ConfigInfo1.tapy[i]))
            time.sleep(10)
            shot = self.driver.get_screenshot_as_base64()
            imgs.append(shot)
            time.sleep(3)
            os.popen('adb shell am force-stop com.kwai.m2u')
            os.popen('adb shell am start -a android.intent.action.VIEW -d content://com.tencent.mobileqq.fileprovider/external_files/storage/emulated/0/Android/data/com.tencent.mobileqq/Tencent/QQfile_recv/H5.html')
            time.sleep(3)
        createhtml(imgs, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + 'imgs')



if __name__ == "__main__":
    m2utestcase = m2utestcase()
    m2utestcase.execute()