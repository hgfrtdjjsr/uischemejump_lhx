### 部署开发环境
- 安装python 3
- 使用pip install 安装依赖模块

    pip3 install -r requirements.txt


- 如果添加新功能有安装新的python模块，请注意更新requirements.txt文件:
    pip3 freeze > requirements.txt //根据当前的安装包生成requirements.txt文件


使用：

1、打开uischemejump
2、如果需要增加js跳转url，打开utils/ConfigInfo.py 配置文件，将js的跳转地址添加进去
3、运行脚本：python excute.py ，会将ConfigInfo文件中所有的js跳转都执行一遍，并生成html文件