# coding=utf-8
__author__ = 'lixinyan'


takephotocoreBaseConfig = [
    ['拍视频页，贴纸：猫咪脸，打开面板', "m2u://m2u_home/sticker?materialId=6473365848767430154\'&\'catId=48\'&\'openSticker=1"],
    ['拍视频页，贴纸：星空妆，打开面板',
     "m2u://m2u_home/sticker?materialId=11653675879495264054\'&\'catId=10\'&\'openSticker=1"],
    ['拍照页，音乐：甜蜜暴击，MV：黑白格，打开面板',
     "m2u://m2u_home/mv?mvMaterialId=4592210740139934656"],
    ['拍前美妆', "m2u://m2u_home/beauty?beautyId=makeup\'&\'catId=yt_kouhong\'&\'materialId=kh_nvshen\'&\'value=90"],
]

#直接跳转类
takephotoBaseConfig = [
    ['拍视频页，贴纸：猫咪脸，打开面板', "m2u://m2u_home/sticker?materialId=6473365848767430154\'&\'catId=48\'&\'openSticker=1"],
    ['跳转到贴图商店',"m2u://chartlet_store?moreCatId=-20\co'&\'moreZipId=17927511266749525981"],
    ['拍视频页，贴纸：星空妆，打开面板',
     "m2u://m2u_home/sticker?materialId=11653675879495264054\'&\'catId=10\'&\'openSticker=1"],
    ['拍照页，音乐：甜蜜暴击，MV：黑白格，打开面板',
     "m2u://m2u_home/mv?mvMaterialId=4592210740139934656"],
    ['拍前美妆', "m2u://m2u_home/beauty?beautyId=makeup\'&\'catId=yt_kouhong\'&\'materialId=kh_nvshen\'&\'value=90"],
    ['跟拍-奶凶喵', "m2u://followshoot?materialId=5668651678452984715\'&\'catId=7"],
    ['卡点视频-慢热', "m2u://home_photomovie?materialId=3373039905440986926"],
    ['模板首页', 'm2u://template'],
    ["模板卡点-漫画女主", "m2u://template_photomovie?catId=12\'&\'templateId=14977016718800844566"],
    ["模板热拍-难道我又我又初恋了", "m2u://template_hot?templateId=2416643655248031735"],
    ["模板跟拍-口罩眼神杀", "m2u://template_follow?catId=2\'&\'templateId=17331094596628156833"],
    ["模板图片-发条朋友圈", "m2u://template?catId=201\'&\'templateId=18076116336291257921"],
    ["模板主题页-夏日天空", "m2u://temp_theme?themeId=1002"],
    ["一键get-图片-分类：快手爆款", "m2u://template?catId=201"],
    ["一键get-图片-分类：天空便利店-可爱天空", "m2u://template?catId=207\'&\'templateId=15117908878900927509"],
    ['卡点视频-变身漫画女主','m2u://home_photomovie?materialId=14977016718800844566'],
    ['拼图','m2u://home_puzzle'],
    ['素材中心-童话脸', "m2u://home_commonactivity?type=fairyTale"],
    ['素材中心-性别双修术', "m2u://home_commonactivity?type=GENDER_HDPIC"],
    ['素材中心-芭比魔法术', "m2u://home_commonactivity?type=mixedStyle3Channels"],
    ['素材中心-手绘女主', "m2u://home_handdrawn?unfoldAlbum=1"],
    ['素材中心-生发屋','m2u://home_commonactivity?type=longHair'],
    ['素材中心-全家福','m2u://home_family'],
    ['素材中心-漫画脸-样式2','m2u://home_cartoon?materialId=3'],
    ['神仙换脸-校园女神','m2u://home_changeface?materialId=8104911742779980083'],
    ['手绘女主-宠爱百分百','m2u://home_handdrawn?materialId=2194375317087117584'],
]

#修图类0
editphotoBaseConfig = [
    ['249之后版本：魔法抠图', "m2u://photo_edit?func=pe_cutout\'&\'unfoldAlbum=1"],
    ['一级页-玩法', 'm2u://photo_edit?func=pe_playfunction'],
    ['风格-自然-滤镜-50',"m2u://photo_edit?func=pe_style\'&\'materialId=7362968339169973685\'&\'catId=95\'&\'filterValue=50\'&\'makeupValue=100"],
    ['超清人像-75', "m2u://photo_edit?func=pe_hdrBeauty\'&\'hdrValue=75"],
    ['美妆-口红-90', "m2u://photo_edit?func=pe_makeup\'&\'catId=yt_kouhong\'&\'materialId=kh_nvshen\'&\'makeupValue=90"],
    ['染发-落日橙-100', "m2u://photo_edit?func=pe_hair\'&\'catId=0\'&\'materialId=14491845897280770035\'&\'hairValue=100"],
    ['柔发-100', "m2u://photo_edit?func=pe_hair\'&\'catId=1\'&\'softenHair=true\'&\'softenValue=100"],
    ['美体-一键瘦身', "m2u://photo_edit?func=pe_body\'&\'materialId=yt_meiti_all"],
    ['细调-自动优化-100', "m2u://photo_edit?func=pe_adjust\'&\'materialId=yt_hdr\'&\'value=100"],
    ['纹理-划痕-100', "m2u://photo_edit?func=pe_texture\'&\'materialId=12509011709648439897\'&\'value=100"],
    ['裁剪', "m2u://photo_edit?func=pe_crop"],
    ['旋转矫正', "m2u://photo_edit?func=pe_rotaterectify"],
    ['贴图-蕉个朋友',"m2u://photo_edit?func=pe_chartlet\'&\'catId=2850425357754097742\'&\'id=8302"],
    ['涂鸦笔-桃子爱心', "m2u://photo_edit?func=pe_graffiti\'&\'materialId=1584548826550941119"],
    ['贴纸-质感-星空-30',"m2u://photo_edit?func=pe_sticker\'&\'materialId=15735563591719004765\'&\'catId=20\'&\'makeupValue=30"],
    ['文字贴纸',
     "m2u://photo_edit?func=pe_text\'&\'catId=3\'&\'materialId=281748617884906603\'&\'color=DF2C1F\'&\'context=我是文字内容"],
    ['光斑-图形光-蝴蝶-100', "m2u://photo_edit?func=pe_facular\'&\'catId=2\'&\'materialId=18142769492175456808\'&\'value=98"],
    ['线条描边-荧光笔', "m2u://photo_edit?func=pe_lineDraw\'&\'materialId=4\'&\'color=DF2C1F"],
    ['虚化-动感-100', "m2u://photo_edit?func=pe_virtual\'&\'materialId=motion\'&\'value=100"],
    ['边框+素材', "m2u://photo_edit?func=pe_border\'&\'materialId=7123618734621558273"],
    ["肤色-深小麦", "m2u://photo_edit?func=pe_whiteskin\'&\'materialId=5019539700969421524"],
    ["马赛克-经典2", "m2u://photo_edit?func=pe_mosaic\'&\'materialId=1"],
    ["抠图", "m2u://photo_edit?func=pe_cutout"],
    ["文字-花字", "m2u://photo_edit?func=pe_text\'&\'catId=3\'&\'materialId=281748617884906603"],
    ["文字-字体tab-汉仪跳跳体", "m2u://photo_edit?func=pe_text\'&\'catId=0\'&\'materialId=16935433970051791003"],
    ["边框-踏春小熊", "m2u://photo_edit?func=pe_border\'&\'materialId=8576230569807152556"],
    ["放大镜", "m2u://photo_edit?func=pe_magnifier"],
]

if __name__ == "__main__":
    pass