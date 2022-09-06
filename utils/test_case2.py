# # 导包
# import uiautomator2 as u2
#
# # 链接手机
# device = u2.connect(addr=" ")
# # 安装app 去搜索 apk地址
# url = "http://dizhi"
# device.app_install(url)  # url作为参数传参  app_install是下载
# # 获取包名（）和界面名 current
# print(device.app_current())
# # 卸载app
# device.app_uninstall(" 包名package name")
# # 打开app 关闭APP
# device.app_start("package_name ")
# device.app_stop("package_name ")
# # 清除app数据
# device.app_clear("package_name")
# # 显示设备信息 字典类型，包名，高度，宽度 设备名
# print(device.info)
# # 更加详细的设备信息 udid设备编号，操作系统的版本 adk 电池
# print(device.device_info)
# # 截取屏幕大小 元组形式(宽，高)
# print(device.window_size())
# # 截屏保存 不写路径就保存在py目录里
# device.screenshot(r'd:\test.png')
# # 电脑上的文件推送到手机上去
# device.push(r"d:\目录下的某文件,'/手机目录/")
# # 手机文件存到电脑中
# device.pull('手机目录下某文件，r"电脑目"')
# # 音量键，音量增加 可以写在循环里
# for i in range(3):
#     device.press("volume_up")
# device.press("volume_down")  # 音量键 减少
# device.press('volume_mute')  # 静音
# # 屏幕中显示出最近浏览过的程序
# device.press('recent')
# # 电源键 有点像屏幕被锁了
# device.press('power')
# # 通过weditor去定位元素
# device(resourceid="").click()
# device(text="").send_keys("")
# # 出现多个元素定位不了 两种办法
# device(resource="", text="").click()
# device(text="", instance=2).click()  # 只点击第三个元素
# # 根据上下同级关系定位元素
# my_icon = device('父级').child('下级')
# my_icon.click()
# text_view = my_icon.sibling("")
# text_view.click()
# # 找左边的元素left，right，up，dowm
# my = device("")
# my.left().click()
# # 滑动操作
# device.swipe(800, 500, 100, 500)
# # 前面是方向后面scale是百分比
# device.swipe_ext('right', scale=0.9)
# # 先定位元素在使用元素对象滑动
# e = device(" ")
# e.swipe("方向", steps=100)  # 这里的100像时间
# # 元素定位输入框
# mobile_elem = device(" ")
# mobile_elem.send_keys("")
# mobile_elem.clear_text()
# # 截屏
# im = device.screenshot()
# im.save("hello.png")
# # 对保存的图片做模糊处理
# im2 = im.filter(ImageFilter.BLUR)
# im2.save("text2.png")
# # 对保存的图片指定大小
# im3 = im.resize((200, 400))
# im3.save("text3.png")
# import time
#
# time.sleep(3)
# # 等待app加载完成    超时时间默认20s
# device.app_start("package_name", wait=Ture)
# # 修改超时时间
# device.wait_timeout(10)
# device.implicitly_wait(10)  # 函数方法修改
# # 单独设置等待时间
# device(id="").click(timeout=50)
# device.set_text(timeout=50)
# device.clear_text(timeout=50)
#
#导包
# import uiautomator2 as u2
# #连接手机
# device = u2.connect(addr='f46b8c99')
# # device()

# url ='https://github.com/majido/clipper/releases/download/v1.2.1/clipper.apk'
# device.app_install(url)
#打开一甜
# device(resourceId="com.miui.home:id/icon_icon").click()
# device.app_start("com.miui.home")
# a = device.app_current()
# print(a)
import uiautomator2 as u2
# import time
d = u2.connect(addr="2b00208e")
url ='https://github.com/majido/clipper/releases/download/v1.2.1/clipper.apk'
d.app_install(url)
# for i in range(5):
#     device.swipe(800,500,100,500)
# time.sleep(2)
# im = device.screenshot()
# im.save("截屏保存")
# time.sleep(2)
# d(resourceId="com.miui.home:id/icon_icon", description="一甜相机(Debug)").click()
# time.sleep(10)
# d(resourceId="com.kwai.m2u:id/preview_container").click()
# device(xpath='//*[@resource-id="com.kwai.m2u:id/top_panel"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[4]').click()
# device(text="跳过").click_exist()

# d.click(0.286, 0.891)
# d.click(0.457, 0.847)
# d.click(0.563, 0.669)
# d.click(0.388, 0.779)
# d.click(0.286, 0.841)
# d.click(0.442, 0.845)
# d.click(0.813, 0.669)
# d.click(0.099, 0.947)
# d.click(0.084, 0.784)
# d.click(0.635, 0.848)
# d.click(0.337, 0.845)
# d.click(0.768, 0.669)
# d.click(0.496, 0.944)
# d.click(0.487, 0.899)
# d.click(0.647, 0.369)
# d.click(0.719, 0.886)
# d.click(0.581, 0.834)
# d.click(0.891, 0.664)
# d.click(0.102, 0.949)
# d.click(0.909, 0.897)
# d.click(0.521, 0.729)
# d.click(0.358, 0.615)
# d.click(0.614, 0.328)
# d.click(0.635, 0.975)
# d.click(0.647, 0.064)
# d.click(0.539, 0.113)

