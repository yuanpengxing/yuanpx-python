from moviepy.editor import *
import cv2


class MovieUtil:
    @classmethod
    def get_ftp(cls, path):
        return VideoFileClip(path).fps

    # 串联
    def concatenate_videoclips_serial(self, movie1, movie2):
        clip1 = VideoFileClip("demo.mp4").subclip(0, 9.5)  # 读取视频，并截取10-20秒的内容
        clip2 = VideoFileClip("demo.mp4").subclip(10, 20)  # 读取视频，并截取10-20秒的内容
        final_clip = concatenate_videoclips([clip1, clip2])  # 视频合并
        final_clip.write_videofile("testc.mp4")

    @classmethod
    def audio_concat_vedio(cls, movie_path, audio_path, save_path):
        """音频视频合成"""
        video = VideoFileClip(movie_path)
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)  # 不能直接是audio的路径
        video.write_videofile(save_path)

    @classmethod
    def get_video_frames(cls, movie_path, des_dir):
        vc = cv2.VideoCapture(movie_path)
        ret, frame = vc.read()
        num = 10000
        while ret:
            image_path = des_dir + str(num) + '.jpg'
            cv2.imwrite(image_path, frame)
            ret, frame = vc.read()
            num += 1

    @classmethod
    def get_audio(cls, source_movie_path, audio_sava_path):
        """音频提取"""
        vedio = VideoFileClip(source_movie_path)
        audio = vedio.audio
        audio.write_audiofile(audio_sava_path)

    @classmethod
    def movie_cut(cls, movie_path, movie_save, second_s, second_e):
        clip = VideoFileClip(movie_path).subclip(second_s, second_e)
        clip.write_videofile(movie_save)

    @classmethod
    def modify_fps(cls, movie_path, movie_save, fps):
        clip = VideoFileClip(movie_path)
        clip.write_videofile(movie_save, fps=fps)

    @classmethod
    def get_frame(cls, movie_path, image_save, moment=0):
        clip = VideoFileClip(movie_path)
        clip.save_frame(image_save, t=moment)
