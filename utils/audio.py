# -*- coding: UTF-8 -*-
# author: yuanpx

from pydub import AudioSegment


class AudioUtil:
    @classmethod
    def do_cut(cls, src, des, cutstart, cutend):
        # 不成熟
        song = AudioSegment.from_mp3(src)
        return song[cutstart:cutend].export(des)
