# -*- coding: UTF-8 -*-
# author: yuanpx
import os

from utils.str import StringUtil
from utils.cmd import CmdUtil
from utils.file import FileUtil

LF = '\n'


class CurlConvert:
    @classmethod
    def to_python(cls, urlBashCopy, save='D:/js/test.js'):
        # urlBashCopy = curl  ... --compressed
        copy = urlBashCopy.replace('"', '\\"')
        with open(save, 'w') as wf:
            wf.write("import * as curlconverter from 'curlconverter';" + LF)
            wf.write('let res = curlconverter.toPython("')
            wf.write(copy.strip(LF).strip(LF).strip(LF))
            wf.write('");' + LF)
            wf.write('console.log(res);')
        resp = CmdUtil.run_cmd('node ' + save)
        return resp

    @classmethod
    def to_script(cls, script_save, convert):
        with open(script_save, 'w') as wf:
            wf.write('# -*- coding: UTF-8 -*-' + LF)
            split = convert.strip(LF).strip(LF).split(LF)
            flag = False
            for i in range(len(split)):
                line = split[i]
                if line.startswith('response = requests.'):
                    wf.write(LF + 'def do():' + LF)
                    flag = True
                if flag:
                    wf.write('    ' + line + LF)
                else:
                    wf.write(line + LF)
                if i == len(split) - 1:
                    wf.write('    return response.text')
                    wf.write(LF)

    @classmethod
    def get_url_method(cls, script_save):
        text = FileUtil.get_text(script_save)
        s1 = StringUtil.match1(text, 'response = requests.', 'return response.text')
        s2 = ''
        for line in s1.split(LF):
            s2 += line.strip()
        s3 = StringUtil.match1(s2, "('", "',")
        s4 = StringUtil.match1(text, 'response = requests.', '(')
        return s3, s4.upper()


