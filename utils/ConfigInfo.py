# coding=utf-8
__author__ = 'lixinyan'

#直接跳转类
takephotoBaseConfig = [
    ['拍视频页，贴纸：猫咪脸，打开面板', "m2u://m2u_home/sticker?materialId=6473365848767430154&catId=48&openSticker=1&jumpStrategy=1"],
    ['拍视频页，贴纸：星空妆，打开面板', "m2u://m2u_home/sticker?materialId=11653675879495264054&catId=10&openSticker=1&jumpStrategy=1"],
#     ['拍照页，音乐：甜蜜暴击，MV：黑白格，打开面板', "m2u://m2u_home/mv?mvMaterialId=4592210740139934656&openMVBoard=1&musicId=13849353500971794162&jumpStrategy=0"],
#     ['拍前美妆', "m2u://m2u_home/beauty?beautyId=makeup&catId=yt_kouhong&materialId=kh_nvshen&value=90"],
#     ['跟拍-奶凶喵', "m2u://followshoot?materialId=5668651678452984715&catId=7"],
#     ['玩图首页', "m2u://playphoto"],
#     ['卡点视频-儿童节', "m2u://home_photomovie?materialId=16296650741246357122"],
#     ['贴图', "m2u://materialcenter?func=pe_chartlet"],
# #    ['贴图+非hot的tab', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://materialcenter?func=pe_chartlet&catId=14203952946683646248\\"}}'],
# #    ['贴图+hot的tab+素材', '{\\"from\\":\\"yitianH5\\",\\"data\\":{\\"jumpUrl\\":\\"m2u://materialcenter?func=pe_chartlet&catId=1001&materialId=11490196417641268516\\"}}'],
#     ['贴图+非hot的tab+素材', "m2u://materialcenter?func=pe_chartlet&catId=12924239871261681147&materialId=1a14c76795051a89d3e7a337a1d8d096"],
#     ['涂鸦', "m2u://materialcenter?func=pe_graffiti"],
#     ['涂鸦笔+素材', "m2u://materialcenter?func=pe_graffiti&materialId=11337195945248630559"],
#     ['文字', "m2u://materialcenter?func=pe_text"],
#     ['文字+分类tab', "m2u://materialcenter?func=pe_text&catId=3"],
#     ['文字+分类tab+素材', "m2u://materialcenter?func=pe_text&catId=3&materialId=3264333769522071756"],
#     ['光斑', "m2u://materialcenter?func=pe_facular"],
#     ['光斑+分类tab', "m2u://materialcenter?func=pe_facular&catId=4"],
#     ['光斑+分类tab+素材', "m2u://materialcenter?func=pe_facular&catId=4&materialId=16462017114902855738"],
#     ['全家福', "m2u://home_family"],
]

#修图类
editphotoBaseConfig = [
    ['一级页-美化', "m2u://photo_edit?category=beauty"],
    ['一级页-工具', "m2u://photo_edit?category=tool"],
    # ['一级页-装饰', "m2u://photo_edit?category=decorate"],
    # ['一级页-特效', "m2u://photo_edit?category=effect"],
    # ['风格-铃木-滤镜-50', "m2u://photo_edit?func=pe_style&materialId=10383854300615203545&catId=95&filterValue=50&makeupValue=100"],
    # ['超清人像-75', "m2u://photo_edit?func=pe_hdrBeauty&hdrValue=75"],
    # ['美颜-瘦脸', "m2u://photo_edit?func=pe_beauty&catId=1&materialId=yt_shoulian"],
    # ['美颜-立体光', "m2u://photo_edit?func=pe_beauty&catId=0&materialId=yt_3dlight"],
    # ['美妆-口红-90', "m2u://photo_edit?func=pe_makeup&catId=yt_kouhong&materialId=kh_nvshen&makeupValue=90"],
    # ['染发-落日橙-100', "m2u://photo_edit?func=pe_hair&catId=0&materialId=14491845897280770035&hairValue=100"],
    # ['柔发-100', "m2u://photo_edit?func=pe_hair&catId=1&softenHair=true&softenValue=100"],
    # ['美体-一键瘦身', "m2u://photo_edit?func=pe_body&materialId=yt_meiti_all"],
    # ['细调-自动优化-100', "m2u://photo_edit?func=pe_adjust&materialId=yt_hdr&value=100"],
    # ['纹理-划痕-40', "m2u://photo_edit?func=pe_texture&materialId=12509011709648439897&value=100"],
    # ['裁剪', "m2u://photo_edit?func=pe_crop"],
    # ['旋转矫正', "m2u://photo_edit?func=pe_rotaterectify"],
    # ['贴图-蕉个朋友', "m2u://photo_edit?func=pe_chartlet&catId=2850425357754097742&materialId=e8256d5be4d1e6af7c5f353f7539488a"],
    # ['涂鸦笔-桃子爱心', "m2u://photo_edit?func=pe_graffiti&materialId=1584548826550941119"],
    # ['贴纸-质感-星空-30', "m2u://photo_edit?func=pe_sticker&materialId=15735563591719004765&catId=20&makeupValue=30"],
    # ['文字贴纸', "m2u://photo_edit?func=pe_text&catId=3&materialId=281748617884906603&color=DF2C1F&context=我是文字内容"],
    # ['光斑-图形光-蝴蝶-100', "m2u://photo_edit?func=pe_facular&catId=2&materialId=18142769492175456808&value=98"],
    # ['线条描边-荧光笔', "m2u://photo_edit?func=pe_lineDraw&materialId=4&color=DF2C1F"],
    # ['虚化-动感-100', "m2u://photo_edit?func=pe_virtual&materialId=motion&value=100"],
    # ['边框+素材', "m2u://photo_edit?func=pe_border&materialId=7123618734621558273"],
]

#修图+玩法类
editphotoPlayConfig = [
    ['魔法抠图-霓虹光圈', "m2u://home_cutout?materialId=11078933340716172452"],
    ['漫画脸-样式3', "m2u://home_cartoon?materialId=3"],
    # ['素材中心-童话脸', "m2u://home_commonactivity?type=fairyTale"],
    # ['神仙换脸-校园女神', "m2u://home_changeface?materialId=8104911742779980083"],
    # ['手绘女主-宠爱百分百', "m2u://home_handdrawn?materialId=2194375317087117584"],
    # ['拼图', "m2u://home_puzzle"],
]
if __name__ == "__main__":
    print(type(editphotoPlayConfig))