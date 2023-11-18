# -*- coding: UTF-8 -*-
# author: yuanpx

import os
from os import path
import shutil


class FileUtil:
    @classmethod
    def create_file(cls, filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                pass
        else:
            pass

    @classmethod
    def create_dir(cls, dirname):
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        else:
            pass

    @classmethod
    def get_lines(cls, filename):
        with open(filename, encoding='utf-8') as f:
            return f.readlines()

    @classmethod
    def get_text(cls, filename):
        with open(filename) as f:
            return f.read()

    @classmethod
    def _get_files(cls, dirpath, list):
        for (pathname, dirs, files) in os.walk(dirpath):
            if files:
                for f in files:
                    list.append(path.join(pathname, f))
            if dirs:
                for dir in dirs:
                    cls._get_files(path.join(pathname, dir), list)

    @classmethod
    def get_files(cls, dirpath):
        files = []
        cls._get_files(dirpath, files)
        return files

    @classmethod
    def delete_dir(cls, dir):
        if os.path.exists(dir):
            shutil.rmtree(dir)

    @classmethod
    def sub_dirs(cls, dirpath):
        dirarr = []
        for (pathname, dirs, files) in os.walk(dirpath):
            if files:
                pass
            if dirs:
                dirarr = dirs
        return dirarr

    @classmethod
    def is_exist(cls, filename):
        return os.path.exists(filename)

    @classmethod
    def path_join(cls, path1, path2):
        return os.path.join(path1, path2)

    @classmethod
    def write(cls, filename, text):
        with open(filename, 'w') as f:
            f.write(text)
