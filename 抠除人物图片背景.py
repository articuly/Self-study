# 抠除人物图片背景
# 请使用"pip install removebg"先安装模块
# 在Windows测试通过，需要在当前工作目录下新建"picture"目录，在其它系统需要修改路经的符号
# API需要在remove.bg网站申请，请将"xirBtVjr681jz1VUKBG2B7ZP"替换为自己的API，每个账号可以每月处理50张图片
# 抠图成功的图片请及时移出"picture"目录，否则会消耗每月50张的处理资源
from removebg import RemoveBg
import os

rmbg = RemoveBg("xirBtVjr681jz1VUKBG2B7ZP", "removebgerror.log")
path = "%s\\picture" % os.getcwd()
for pic in os.listdir(path):
    rmbg.remove_background_from_img_file("%s\%s" % (path, pic))
    print("完成'{0}'的抠图".format(pic))
