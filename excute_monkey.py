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
from utils.ConfigInfo1 import *
from utils.report import *
import datetime
import base64
from skimage.metrics import structural_similarity
import cv2
import uiautomator2 as u2
import re
import shutil

def monkeycase():
    os.popen('adb shell monkey -p com.kwai.m2u  --ignore-crashes --throttle 1000  10000')


def test_startapp(d):
    warnings.simplefilter("ignore", ResourceWarning)
    time.sleep(3)
    imgs = []
    try:
        print('6.打开一甜app')
        d.app_start('com.kwai.m2u')
        time.sleep(10)
        monkeycase()
    except Exception:
        traceback.print_exc()
    finally:
        return imgs

def test_editstartapp(d):
    warnings.simplefilter("ignore", ResourceWarning)
    time.sleep(2)
    imgs = []
    try:
        print('6.打开一甜app')
        d.app_start('com.kwai.m2u')
        time.sleep(10)
        monkeycase()
    except Exception:
        print(traceback.print_exc())
    finally:
        return imgs

def test_editplayapp(d):
    warnings.simplefilter("ignore", ResourceWarning)
    time.sleep(2)
    imgs = []
    try:
        print('6.打开一甜app')
        d.app_start('com.kwai.m2u')
        time.sleep(10)
        monkeycase()
    except Exception:
        traceback.print_exc()
    finally:
        return imgs

# 将内容复制到手机剪切板
def test_clipper(d, casenum, type):
    d.app_start('ca.zgrs.clipper')
    time.sleep(1)
    startservice = os.popen('adb shell am startservice ca.zgrs.clipper/.ClipboardService').read()
    if 'Error' in startservice:
        print('未启动广播服务，请检查')
    else:
        if type == 1:
            adbtext = os.popen("adb shell am broadcast -a clipper.set -e text \"%s\"" % ('\'{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"' + takephotoBaseConfig[casenum][1] + '\\"}}\'')).read()
            print('跳转页面：' + takephotoBaseConfig[casenum][0])
            print(adbtext)
            time.sleep(1)
        elif type == 2:
            adbtext = os.popen("adb shell am broadcast -a clipper.set -e text \"%s\"" % ('\'{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"' + editphotoBaseConfig[casenum][1] + '\\"}}\'')).read()
            print('跳转页面：' + editphotoBaseConfig[casenum][0])
            print(adbtext)
            time.sleep(1)
        elif type == 3:
            adbtext = os.popen("adb shell am broadcast -a clipper.set -e text \"%s\"" % ('\'{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"' + editphotoPlayConfig[casenum][1] + '\\"}}\'')).read()
            print('跳转页面：' + editphotoPlayConfig[casenum][0])
            print(adbtext)
            time.sleep(1)

def compare_image(path_image1, path_image2):
    fh = open('imagetosave.png', 'wb')
    fh.write(base64.b64decode(path_image2))
    fh.close()
    imageA = cv2.imread(path_image1)
    imageB = cv2.imread('/Users/lidoudou/PycharmProjects/uischemejump/imagetosave.png')

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = structural_similarity(grayA, grayB, full=True)
    print("SSIM: {}".format(score))
    return score

def execute():
    try:
        Unlocking()
        readDeviceId = list(os.popen('adb devices').readlines())
        deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
        d = u2.connect(deviceId)
        crashlog = os.popen("adb logcat *:F | grep \"com.kwai.m2u\"")
        for casenum in range(len(takephotoBaseConfig)):
            test_clipper(d, casenum, 1)
            time.sleep(3)
            test_startapp(d)
        for casenum in range(len(editphotoBaseConfig)):
            test_clipper(d, casenum, 2)
            time.sleep(3)
            test_editstartapp(d)
            time.sleep(1)
        for casenum in range(len(editphotoPlayConfig)):
            test_clipper(d, casenum, 3)
            time.sleep(3)
            test_editplayapp(d)
            time.sleep(1)
        os.system("ps -ef | grep logcat | grep -v grep | awk '{print $2}' | xargs kill -9")
        print(crashlog)
    except Exception:
        print(traceback.print_exc())


if __name__ == "__main__":
    try:
        execute()
    except Exception as e:
        print(traceback.print_exc())
