#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : lixinyan
# coding=utf-8

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
print(rootPath)
sys.path.append(rootPath)
from .pyh import *
import numpy
from .Publicfunctions import *
from utils.ConfigInfo2 import *


def createhtml(imgs, createHtmlname, crashLog, result, imgsname):
    page = PyH('My UItest')
    add_css(page)
    maindiv = page << div(id='myMainDiv',style="padding-left:40px;padding-top:20px;")
    maindiv << h2('是否有崩溃：')
    if crashLog:
        maindiv << p(crashLog)
    else:
        maindiv << p('没有')
    maindiv << h2('测试机信息：')
    maindiv << p('测试机类型：', platformName, ' 测试机版本：', platformVersion)
    shotdiv = maindiv << div(id='sheetDiv', style="white-space: nowrap;")
    shotdiv << h2('截图：')
    # print(type(imgs))
    # print(type(imgs[0]))
    # for i in range(len(result)):
    #     shotdiv << span(result[i], style="padding-left:40px;")
    # shotdiv << p(' ')
    mytab = page << table(style="padding-left:40px;")
    tr2 = mytab << tr()
    for i in range(len(imgs)):
        td1 = tr2 << td()
        td1 << p(imgsname[i])
        td1 <<  img(src='data:image/jpg;base64,' + imgs[i], border="1", width='230')
        # shotdiv << div(imgsname[i])
        # shotdiv << img(src='data:image/jpg;base64,' + imgs[i], border="1", width='230')
    # shotdiv << p(' ')
    # failname = os.getcwd() + '/contrastPng'
    # imgsname = os.listdir(failname)
    # imgsname.sort()
    # for i in range(len(imgsname)):
    #     shotdiv << img(src='contrastPng/' + imgsname[i], border="1", width='230')

    page.printOut('%s.html' % createHtmlname)

def add_css(page):
    page.head << style('''
        #newVersion{display:inline}
        #oldVersion{display:inline}
        }''', type="text/css")
if __name__ == "__main__":
    imgs2=[]
    imgs1 = []
    # imgs2 = numpy.array(imgs2)
    createhtml(imgs1, imgs2)
