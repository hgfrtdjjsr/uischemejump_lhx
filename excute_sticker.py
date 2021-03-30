#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : lixinyan

import aa

from utils.Publicfunctions import *
from utils import ConfigInfo_sticker
import time
import os

import warnings
import traceback
from utils.report_sticker import *
import datetime
import base64
from skimage.metrics import structural_similarity
import cv2
import uiautomator2 as u2
import re
import shutil


localpath=os.path.abspath('.')
pic_dir = localpath + '/imgtemporarypath/'

def test_startapp(d):
    warnings.simplefilter("ignore", ResourceWarning)
    time.sleep(3)
    imgs = []
    try:
        print('6.打开一甜app')
        d.app_start('com.kwai.m2u')
        time.sleep(5)
        print('点击同意')
        d(resourceId="com.kwai.m2u:id/confirm_btn").click()
        time.sleep(5)
        d(resourceId="com.kwai.m2u:id/confirm_btn").click()
        time.sleep(5)
        d(resourceId="com.lbe.security.miui:id/permission_allow_foreground_only_button").click()
        time.sleep(2)
        d(resourceId="com.lbe.security.miui:id/permission_allow_foreground_only_button").click()
        time.sleep(2)
        d(resourceId="com.lbe.security.miui:id/permission_allow_foreground_only_button").click()
        time.sleep(5)
        try:
            d(text="立即试试").click()
        except:
            pass
        time.sleep(2)
        print('点击取景框')
        d(resourceId="com.kwai.m2u:id/vertical_seek_bar_group_after_inflate").click()
        time.sleep(15)

        try:
            d(text="立即试试").click()
        except:
            pass
        print('点击后置摄像头')
        d.xpath('//*[@resource-id="com.kwai.m2u:id/top_panel"]/android.widget.FrameLayout[3]').click()
        time.sleep(30)
        imgname = '%s.png' % round(time.time() * 1000)
        d.screenshot(pic_dir + imgname)
        imgs.append(imgname)
        # 点击拍摄按钮
        print('点击拍摄按钮')
        d(resourceId="com.kwai.m2u:id/rl_controller_shoot").click()
        time.sleep(3)
        imgname = '%s.png' % round(time.time() * 1000)
        d.screenshot(pic_dir + imgname)
        imgs.append(imgname)
    except Exception:
        traceback.print_exc()
    finally:
        return imgs

# 将内容复制到手机剪切板
def test_clipper(d, casenum):
    d.app_start('ca.zgrs.clipper')
    time.sleep(1)
    startservice = os.popen('adb shell am startservice ca.zgrs.clipper/.ClipboardService').read()
    if 'Error' in startservice:
        print('未启动广播服务，请检查')
    else:
        os.popen("adb shell am broadcast -a clipper.set -e text  \"%s\"" % (
        '\'{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://m2u_home/sticker?materialId=%s\\"}}\'' % ConfigInfo_sticker.takephotoBaseConfig[casenum][1])).read()
        print('贴纸：' + ConfigInfo_sticker.takephotoBaseConfig[casenum][0])
        time.sleep(1)

def execute():
    if os.path.exists(pic_dir):
        shutil.rmtree(pic_dir, True)
    os.mkdir(pic_dir)
    result = []
    imgs = []
    imgsname = []
    crashLog = ''
    try:
        readDeviceId = list(os.popen('adb devices').readlines())
        deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
        d = u2.connect(deviceId)
        crashlog = os.popen("adb logcat *:F | grep \"com.kwai.m2u\"")
        for casenum in range(len(takephotoBaseConfig)):
            test_clipper(d, casenum)
            time.sleep(3)
            os.popen('adb shell pm clear com.kwai.m2u')
            img = test_startapp(d)
            time.sleep(1)
            imgs.append(img)
            imgsname.append(takephotoBaseConfig[casenum][0])
        os.system("ps -ef | grep logcat | grep -v grep | awk '{print $2}' | xargs kill -9")
        crashLog = str(crashlog.read())
        crashlog.close()
    except Exception:
        print(traceback.print_exc())
    finally:
        print(result)
        # 运行截图+html命名+崩溃日志+对比图片+对比结果
        print(imgs)
        createhtml(imgs, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + 'imgs', crashLog, imgsname)

if __name__ == "__main__":
    try:
        execute()
    except Exception as e:
        print(traceback.print_exc())
