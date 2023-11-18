# -*- coding: UTF-8 -*-
# author: yuanpx

import numpy as np
import cv2
import glob
import operator
from functools import reduce
from PIL import ImageChops
import math
from PIL import Image, ImageDraw, ImageFont

from utils.str import StringUtil


class ImageUtil:
    @classmethod
    def merge_two(cls, img_path_below, img_path_above, top_left_x, top_left_y, img_new):
        img_below = Image.open(img_path_below)
        img_above = Image.open(img_path_above)
        img_below.paste(img_above, (top_left_x, top_left_y))
        img_below.save(img_new)

    @classmethod
    def join_two_image(cls, img_1, img_2, imgsave, flag='vertical'):  # 默认是垂直参数
        # 1、首先使用open创建Image对象，open()需要图片的路径作为参数
        # 2、然后获取size，size[0]代表宽，size[1]代表长，分别代表坐标轴的x,y
        # 3、使用Image.new创建一个新的对象
        # 4、设置地点，两个图片分别在大图的什么位置粘贴
        # 5、粘贴进大图，使用save()保存图像
        img1 = Image.open(img_1)
        img2 = Image.open(img_2)
        size1, size2 = img1.size, img2.size
        if flag == 'vertical':
            joint = Image.new("RGB", (size1[0], size1[1] + size2[1]))
            loc1, loc2 = (0, 0), (0, size1[1])
            joint.paste(img1, loc1)
            joint.paste(img2, loc2)
            joint.save(imgsave)
        else:
            joint = Image.new("RGB", (size1[0] + size2[0], size1[1]))
            loc1, loc2 = (0, 0), (size1[0], 0)
            joint.paste(img1, loc1)
            joint.paste(img2, loc2)
            joint.save(imgsave)

    @classmethod
    def change_color(cls, src, image_save, ereas_need_change, color_change_to):
        # ereas_need_change: [(left_top_x, left_top_y, right_below_x, right_below_y),(left_top_x, left_top_y, right_below_x, right_below_y)...]
        img = Image.open(src)
        array = np.array(img)
        for erea_need_change in ereas_need_change:
            for col in range(erea_need_change[0], erea_need_change[2]):
                for row in range(erea_need_change[1], erea_need_change[3]):
                    array[row, col] = color_change_to
        new_img = Image.fromarray(array)
        new_img.save(image_save)

    @classmethod
    def images_to_video(cls, path, suffix, fps, movie_save):
        img_array = []

        for filename in glob.glob(path + '*.' + suffix):
            img = cv2.imread(filename)
            img_array.append(img)

        # 图片的大小需要一致
        out = cv2.VideoWriter(movie_save, cv2.VideoWriter_fourcc(*'DIVX'), fps, (576, 1024))

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

    @classmethod
    def image_cut(cls, image_path, image_save, loc_tuple1, loc_tuple2):
        img = Image.open(image_path)
        erea_cut = (loc_tuple1[0], loc_tuple1[1], loc_tuple2[0], loc_tuple2[1])
        cropped = img.crop(erea_cut)
        cropped.save(image_save)

    @classmethod
    def compare_images(cls, img_path1, img_path2):
        image1 = cv2.imread(img_path1, 1)
        image2 = cv2.imread(img_path2, 1)
        difference = cv2.subtract(image1, image2)
        return not np.any(difference)

    def compare_images01(self, pic1, pic2):
        # 该方式对比速度要快一点，但比compare_images要慢点
        hist1 = Image.open(pic1).histogram()
        hist2 = Image.open(pic2).histogram()
        redu = reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, hist1, hist2))) / len(hist1)
        return math.sqrt(redu)

    def compare_images02(self, path_one, path_two):
        image_one = Image.open(path_one)
        image_two = Image.open(path_two)
        try:
            diff = ImageChops.difference(image_one, image_two)
            print(diff.getbbox())
            if diff.getbbox() is None:
                return 0
            else:
                return 1
        except ValueError as e:
            return 2

    @classmethod
    def template_match(cls, source, template):
        tmp = cv2.imread(template, 1)
        src = cv2.imread(source, 1)
        result = cv2.matchTemplate(src, tmp, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        return min_val, min_loc

    @classmethod
    def template_find(cls, source, template, savefile1, savefile2):
        tmp = cv2.imread(template)
        src = cv2.imread(source)
        result = cv2.matchTemplate(src, tmp, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        h, w = tmp.shape[:2]
        right = (min_loc[0] + w, min_loc[1] + h)
        cls.image_cut(source, savefile1, min_loc, right)
        cv2.rectangle(src, min_loc, right, (0, 0, 255), 2)
        cv2.imwrite(savefile2, src)
        if cls.compare_images(savefile1, template):
            pass
        else:
            print('原图片：%s 与模板图片有区别' % (source))
            print('区别参看%s' % savefile2)

    @classmethod
    def add_text_to_image(cls, img, text, imgsave):
        font = ImageFont.truetype('C:\Windows\Fonts\STXINGKA.TTF', 36)

        # 添加背景
        image = Image.open(img)
        new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
        new_img.paste(image, image.size)

        # 添加水印
        font_len = len(text)
        rgba_image = new_img.convert('RGBA')
        text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
        image_draw = ImageDraw.Draw(text_overlay)

        for i in range(0, rgba_image.size[0], font_len * 40 + 50):
            for j in range(0, rgba_image.size[1], 200):
                image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 50))
        text_overlay = text_overlay.rotate(-20)
        image_with_text = Image.alpha_composite(rgba_image, text_overlay)

        # 裁切图片
        var = (image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2)
        image_with_text = image_with_text.crop(var)
        # 图片保存的路径格式为 u'temp3.png'
        image_with_text.save(StringUtil.str_to_unicode(imgsave))

    @classmethod
    def imgs_merge(cls, img01, img02, savepath):
        img1 = cv2.imread(img01)
        img2 = cv2.imread(img02)
        dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
        cv2.imwrite(savepath, dst)
