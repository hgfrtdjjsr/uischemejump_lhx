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
import base64
from skimage.metrics import structural_similarity
import cv2

class m2utestcase():


    def setUp1(self):
        warnings.simplefilter("ignore", ResourceWarning)
        time.sleep(1)
        self.driver = appium_start1()
        time.sleep(3)
        self.driver.quit()

    def test_startapp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        time.sleep(2)
        self.driver = appium_start()
        time.sleep(3)
        imgs = ''
        try:
            time.sleep(10)
            shot = self.driver.get_screenshot_as_base64()
            time.sleep(1)
            imgs = shot
        except Exception as e:
            print('错误日志：' + str(e))
            traceback.print_exc()
        finally:
            self.driver.quit()
            return imgs

    def test_editstartapp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        time.sleep(2)
        self.driver = appium_start()
        time.sleep(3)
        imgs = ''
        try:
            time.sleep(10)
            element_exist = isElement(self, 'id', 'com.kwai.m2u:id/sdv_item_picture_icon', multipe=True)
            if not element_exist:
                self.driver.find_elements_by_id('com.kwai.m2u:id/rl_picture_mv_layout')[-3].click()
                time.sleep(3)
            # self.driver.find_elements_by_id('com.kwai.m2u:id/image_container')[0].click()
            # time.sleep(5)
            self.driver.find_elements_by_id('com.kwai.m2u:id/sdv_item_picture_icon')[0].click()
            time.sleep(5)
            shot = self.driver.get_screenshot_as_base64()
            time.sleep(1)
            imgs = shot
        except Exception as e:
            print('错误日志：' + str(e))
            traceback.print_exc()
        finally:
            self.driver.close_app()
            self.driver.quit()
            return imgs

    # 将内容复制到手机剪切板
    def test_clipper(self, casenum, type):
        self.setUp1()
        time.sleep(1)
        startservice = os.popen('adb shell am startservice ca.zgrs.clipper/.ClipboardService').read()
        if 'Error' in startservice:
            print('未启动广播服务，请检查')
        else:
            if type == 1:
                adbtext = os.popen("adb shell am broadcast -a clipper.set -e text \"%s\"" % ('\'' + takephotoBaseConfig[casenum]+ '\'')).read()
                print('\'' + takephotoBaseConfig[casenum]+ '\'')
                print(adbtext)
                time.sleep(1)
            else:
                adbtext = os.popen("adb shell am broadcast -a clipper.set -e text \"%s\"" % ('\'' + editphotoBaseConfig[casenum] + '\'')).read()
                print('\'' + editphotoBaseConfig[casenum] + '\'')
                print(adbtext)
                time.sleep(1)

    def compare_image(self, path_image1, path_image2):
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

    def execute(self):
        result = []
        imgs = []
        crashLog = ''
        try:
            filename = 'img.txt'
            crashlog = os.popen("adb logcat *:F | grep \"com.kwai.m2u\"")
            for casenum in range(len(takephotoBaseConfig)):
                self.test_clipper(casenum, 1)
                time.sleep(3)
                img = self.test_startapp()
                time.sleep(1)
                imgs.append(img)
            for casenum in range(len(editphotoBaseConfig)):
                self.test_clipper(casenum, 2)
                time.sleep(3)
                img = self.test_editstartapp()
                time.sleep(1)
                imgs.append(img)
            os.system("ps -ef | grep logcat | grep -v grep | awk '{print $2}' | xargs kill -9")
            crashLog = str(crashlog.read())
            crashlog.close()
            with open(filename, 'w') as file:
                file.write(json.dumps(imgs))
            a = os.getcwd() + '/img.txt'
            with open(a, 'r') as file:
                imgs = file.read()
            imgs = eval(imgs)
            failname = os.getcwd() + '/fileimgs'
            imgsname = os.listdir(failname)
            imgsname.sort()
            for i in range(len(imgsname)):
                path_image1 = failname + '/' + imgsname[i]
                path_image2 = imgs[i]
                a = self.compare_image(path_image1, path_image2)
                result.append(a)
        except Exception as e:
            print('错误日志：' + str(e))
        finally:
            print(result)
            # 运行截图+html命名+崩溃日志+对比图片+对比结果
            createhtml(imgs, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + 'imgs', crashLog, result)

if __name__ == "__main__":
    try:
        m2utestcase = m2utestcase()
        m2utestcase.execute()
    except Exception as e:
            print('错误日志：' + str(e))
            traceback.print_exc()
