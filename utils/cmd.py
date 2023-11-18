# -*- coding: UTF-8 -*-
# author: yuanpx

import subprocess
import getopt
import sys


class CmdUtil:
    @classmethod
    def run_cmd(cls, cmd):
        # 执行cmd命令，并返回响应内容
        p = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding='utf-8',
            close_fds=True
        )
        return p.communicate()[0]

    @classmethod
    def parser(cls, argv):
        # h后面没有冒号，表示后面不带参数; help后面没有等号，表示后面不带参数
        try:
            options, args = getopt.getopt(argv, "hp:i:", ["help", "ip=", "port="])
        except getopt.GetoptError:
            sys.exit()

        params = {}
        for option, value in options:
            if option in ("-h", "--help"):
                print("usage example: I don't want to tell you, hahaha!!!!")
            if option in ("-p", "--period"):
                params["period"] = value
        return params
