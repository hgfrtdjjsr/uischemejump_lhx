# coding=utf-8
__author__ = 'lixinyan'

#直接跳转类
takephotoBaseConfig = [
    ['拍视频页，贴纸：星空妆，打开面板', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://m2u_home/sticker?materialId=11653675879495264054&catId=10&openSticker=1&jumpStrategy=1\\"}}'],
    ['拍照页，音乐：甜蜜暴击，MV：黑白格，打开面板', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://m2u_home/mv?mvMaterialId=4592210740139934656&openMVBoard=1&musicId=13849353500971794162&jumpStrategy=0\\"}}'],
    ['拍前美妆', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://m2u_home/beauty?beautyId=makeup&catId=yt_kouhong&materialId=kh_nvshen&value=90\\"}}'],
    ['跟拍-奶凶喵', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://followshoot?materialId=5668651678452984715&catId=7\\"}}'],
    ['玩图首页', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://playphoto\\"}}'],
    ['通用玩法', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://home_commonactivity?type=fairyTale\\"}}'],
    ['卡点视频-儿童节', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://home_photomovie?materialId=16296650741246357122\\"}}'],
    ['全家福', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://home_family\\"}}'],
    ['素材中心', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://materialcenter\\"}}'],
    ['贴图', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://materialcenter?func=pe_chartlet\\"}}'],
    ['涂鸦', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://materialcenter?func=pe_graffitii\\"}}'],
    ['文字', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://materialcenter?func=pe_text\\"}}'],
    ['光斑', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://materialcenter?func=pe_facular\\"}}'],
    ['社区首页', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://feed_home?tab=0\\"}}'],
    ['个人首页', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://feed_home?tab=1\\"}}'],
    ['作品详情', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://feed_detail?itemId=131986158332304437\\"}}'],
    ['个人页', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://feed_user?userId=1003437220\\"}}'],
    ['通知', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://feed_message?tab=0\\"}}'],
    ['评论', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://feed_message?tab=1\\"}}'],
]

#修图类
editphotoBaseConfig = [
    ['一级页-美化', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?category=beauty\\"}}'],
    ['一级页-工具', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?category=tool\\"}}'],
    ['一级页-装饰', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?category=decorate\\"}}'],
    ['一级页-特效', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?category=effect\\"}}'],
    ['风格-铃木-滤镜-50', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_style&materialId=10383854300615203545&catId=95&filterValue=50&makeupValue=100\\"}}'],
    ['超清人像-75', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_hdrBeauty&hdrValue=75\\"}}'],
    ['美颜-瘦脸', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_beauty&materialId=yt_shoulian\\"}}'],
    ['美颜-立体光', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_beauty&materialId=yt_3dlight\\"}}'],
    ['美妆-眉毛-一字眉-90', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_makeup&catId=yt_kouhong&materialId=kh_nvshen&makeupValue=90\\"}}'],
    ['染发-落日橙-100', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_hair&catId=0&materialId=14491845897280770035&hairValue=100\\"}}'],
    ['柔发-100', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_hair&catId=1&softenHair=true&softenValue=100\\"}}'],
    ['美体-一键瘦身', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_body&materialId=yt_meiti_all\\"}}'],
    ['细调-自动优化-100', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_adjust&materialId=yt_hdr&value=100\\"}}'],
    ['纹理-划痕-40', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_texture&materialId=12509011709648439897&value=40\\"}}'],
    ['裁剪', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_crop\\"}}'],
    ['旋转矫正', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_rotaterectify\\"}}'],
    ['贴图-蕉个朋友', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_chartlet&catId=2850425357754097742&materialId=e8256d5be4d1e6af7c5f353f7539488a\\"}}'],
    ['涂鸦笔-桃子爱心', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_graffiti&materialId=1584548826550941119\\"}}'],
    ['贴纸-质感-星空-30', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_sticker&materialId=15735563591719004765&catId=20&makeupValue=30\\"}}'],
    ['文字贴纸', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_text&catId=3&materialId=281748617884906603&color=DF2C1F&context=我是文字内容\\"}}'],
    ['光斑-图形光-蝴蝶-100', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_facular&catId=2&materialId=18142769492175456808&value=98\\"}}'],
    ['线条描边-荧光笔', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_lineDraw&materialId=4&color=DF2C1F\\"}}'],
    ['虚化-动感-100', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://photo_edit?func=pe_virtual&materialId=motion&value=100\\"}}'],
]

#修图+玩法类
editphotoPlayConfig = [
    ['魔法抠图-霓虹光圈', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://home_cutout?materialId=11078933340716172452\\"}}'],
    ['漫画脸-样式2', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://home_cartoon?materialId=3\\"}}'],
    ['神仙换脸-校园女神', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://home_changeface?materialId=8104911742779980083\\"}}'],
    ['手绘女主-宠爱百分百', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://home_handdrawn?materialId=2194375317087117584\\"}}'],
]
if __name__ == "__main__":
    print(type(editphotoPlayConfig))