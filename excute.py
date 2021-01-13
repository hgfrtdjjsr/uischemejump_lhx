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

class m2utestcase():


    def setUp1(self):
        warnings.simplefilter("ignore", ResourceWarning)
        time.sleep(1)
        self.driver = appium_start1()
        time.sleep(3)
        try:
            self.driver.quit()
        except:
            pass

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
            print( str(e))
        finally:
            try:
                self.driver.quit()
                return imgs
            except:
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
            self.driver.find_elements_by_id('com.kwai.m2u:id/preview_container')[0].click()
            time.sleep(5)
            shot = self.driver.get_screenshot_as_base64()
            time.sleep(1)
            imgs = shot
        except Exception:
            print(traceback.print_exc())
        finally:
            try:
                self.driver.close_app()
                self.driver.quit()
                return imgs
            except:
                return imgs

    def test_editplayapp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        time.sleep(2)
        self.driver = appium_start()
        time.sleep(3)
        imgs = ''
        try:
            time.sleep(10)
            #是否有立即体验按钮
            element_exist1 = isElement(self, 'id', 'com.kwai.m2u:id/get_image_view')
            if element_exist1:
                self.driver.find_element_by_id('com.kwai.m2u:id/get_image_view').click()
                #是否有相册按钮
                element_exist2 = isElement(self, 'id', 'com.kwai.m2u:id/gallery_icon')
                if element_exist2:
                    self.driver.find_element_by_id('com.kwai.m2u:id/gallery_icon').click()
                    time.sleep(3)
                while True:
                    element_exist3 = isElement(self, 'id', 'com.kwai.m2u:id/sdv_item_picture_icon', multipe=True)
                    if element_exist3:
                        try:
                            print('element_exist3')
                            self.driver.find_elements_by_id('com.kwai.m2u:id/sdv_item_picture_icon')[0].click()
                            break
                        except:
                            pass
                    element_exist4 = isElement(self, 'id', 'com.kwai.m2u:id/preview_container', multipe=True)
                    if element_exist4:
                        print('element_exist4')
                        try:
                            self.driver.find_elements_by_id('com.kwai.m2u:id/preview_container')[0].click()
                            break
                        except:
                            pass
                    element_exist5 = isElement(self, 'id', 'com.kwai.m2u:id/preview_container', multipe=True)
                    if element_exist5:
                        print('element_exist5')
                        self.driver.find_elements_by_id('com.kwai.m2u:id/preview_container')[0].click()
                        break

            time.sleep(5)
            shot = self.driver.get_screenshot_as_base64()
            time.sleep(1)
            imgs = shot
        except Exception:
            print(traceback.print_exc())
        finally:
            try:
                self.driver.quit()
                return imgs
            except:
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
                adbtext = os.popen("adb shell am broadcast -a clipper.set -e text \"%s\"" % ('\'{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"' + takephotoBaseConfig[casenum][1] + '\\"}}\'')).read()
                
                print('跳转页面：' + takephotoBaseConfig[casenum][0])
                print(adbtext)
                time.sleep(1)
            elif type == 2:
                adbtext = os.popen("adb shell am broadcast -a clipper.set -e text \"%s\"" % ('\'{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"' + editphotoBaseConfig[casenum][1] + '\\"}}\'')).read()

                print('跳转页面：' + takephotoBaseConfig[casenum][0])
                print(adbtext)
                time.sleep(1)
            elif type == 3:
                adbtext = os.popen("adb shell am broadcast -a clipper.set -e text \"%s\"" % ('\'{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"' + editphotoPlayConfig[casenum][1] + '\\"}}\'')).read()

                print('跳转页面：' + takephotoBaseConfig[casenum][0])
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
        imgsname = []
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
                imgsname.append(takephotoBaseConfig[casenum][0])
            for casenum in range(len(editphotoBaseConfig)):
                self.test_clipper(casenum, 2)
                time.sleep(3)
                img = self.test_editstartapp()
                time.sleep(1)
                imgs.append(img)
                imgsname.append(editphotoBaseConfig[casenum][0])
            for casenum in range(len(editphotoPlayConfig)):
                self.test_clipper(casenum, 3)
                time.sleep(3)
                img = self.test_editplayapp()
                time.sleep(1)
                imgs.append(img)
                imgsname.append(editphotoPlayConfig[casenum][0])
            os.system("ps -ef | grep logcat | grep -v grep | awk '{print $2}' | xargs kill -9")
            crashLog = str(crashlog.read())
            crashlog.close()
            with open(filename, 'w') as file:
                file.write(json.dumps(imgs))
            a = os.getcwd() + '/img.txt'
            with open(a, 'r') as file:
                imgs = file.read()
            imgs = eval(imgs)
            # failname = os.getcwd() + '/fileimgs'
            # imgsname = os.listdir(failname)
            # imgsname.sort()
            # for i in range(len(imgsname)):
            #     path_image1 = failname + '/' + imgsname[i]
            #     path_image2 = imgs[i]
                # a = self.compare_image(path_image1, path_image2)
                # result.append(a)
        except Exception:
            print(traceback.print_exc())
        finally:
            print(result)
            # 运行截图+html命名+崩溃日志+对比图片+对比结果
            createhtml(imgs, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + 'imgs', crashLog, imgsname)

if __name__ == "__main__":
    try:
        m2utestcase = m2utestcase()
        m2utestcase.execute()
    except Exception as e:
        print(traceback.print_exc())
