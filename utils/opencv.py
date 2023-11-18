import cv2
import numpy as np


def tm_sqdiff_normed_matching(source, template):
    tmp = cv2.imread(template, 1)
    src = cv2.imread(source, 1)
    result = cv2.matchTemplate(src, tmp, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return min_val, min_loc


def multi_tm_sqdiff_normed_matching(source, template, threshold):
    tmp = cv2.imread(template, 1)
    src = cv2.imread(source, 1)
    result = cv2.matchTemplate(src, tmp, cv2.TM_SQDIFF_NORMED)
    loc = np.where(result <= threshold)
    for pt in zip(*loc[::-1]):
        print(pt[0], pt[1])


def tm_ccoeff_normed_matching(source, template):
    tmp = cv2.imread(template, 1)
    src = cv2.imread(source, 1)
    result = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_val, max_loc
