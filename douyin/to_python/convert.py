# -*- coding: UTF-8 -*-
# author: yuanpx

from utils.curlconvert import CurlConvert
from utils.file import FileUtil

copy = FileUtil.get_text('../CopyAscURLBase/发表评论.txt')
converter = CurlConvert.to_python(copy)
CurlConvert.to_script('publish.py', converter)