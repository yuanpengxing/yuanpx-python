# -*- coding: UTF-8 -*-
# author: yuanpx

from utils.curlconvert import CurlConvert
from utils.file import FileUtil

def create_py(cURLBase, pysave):
    copy = FileUtil.get_text(cURLBase)
    converter = CurlConvert.to_python(copy)
    CurlConvert.to_script(pysave, converter)

if __name__ == '__main__':
    # create_py('../CopyAscURLBase/发表评论.txt', 'publish.py')
    create_py('..\CopyAscURLBase\用户列表\昕 昕.txt', './videos_author/py001.py')