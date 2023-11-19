# -*- coding: UTF-8 -*-
# author: yuanpx

import os

from utils.curlconvert import CurlConvert
from utils.file import FileUtil

rootpath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def createpy_a(cURLBaseFile, save):
    converter = CurlConvert.to_python(FileUtil.get_text(cURLBaseFile))
    CurlConvert.to_script(save, converter)


if __name__ == '__main__':
    pass
