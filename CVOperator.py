
import math
import cv2
import os
import glob
import logging
import os
import time
from os.path import splitext
from tqdm import tqdm
import numpy as np
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from FileOperator import *

def cal_mean_std(images_dir:str):
    list=get_all_files_pth("D:/test",'jpg')
    mean1=0
    std1=0
    count=0
    #循环每张图片
    for i in range(0,list.__len__()):
        img=cv2.imread(list[i],0)
        (mean,std)=cv2.meanStdDev(img)
        mean1=mean1+mean
        std1=std1+std
        count=count+1
   # print(mean1,std1)
    mean=mean1/count
    std=math.sqrt(std1/count)
    dict={}
    dict['mean']=mean
    dict['std']=std
    #print(mean,std)
    return dict
#经验告诉我 otsu需要自己单独写成一个方法
def otsu_bin(img: np.ndarray):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, res = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return res
def showim(img:np.ndarray,img_name:str='image',is_fixed=True):
    '''
    展示图片
    :param img: ndarray格式的图片
    '''
    if is_fixed:
        cv2.namedWindow(img_name, cv2.WINDOW_AUTOSIZE)
    else:
        cv2.namedWindow(img_name, cv2.WINDOW_NORMAL)
    cv2.imshow(img_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def cal_mean_std(images_dir,is_normalized=False):
    """
    给定数据图片根目录,计算图片整体均值与方差
    :param images_dir:
    :return:
    """
    img_filenames = os.listdir(images_dir)
    m_list, s_list = [], []
    for img_filename in tqdm(img_filenames):
        img = cv2.imread(images_dir + '/' + img_filename)
        img = img / 255.0
        m, s = cv2.meanStdDev(img)

        m_list.append(m.reshape((3,)))
        s_list.append(s.reshape((3,)))
        print(m_list)
    m_array = np.array(m_list)
    s_array = np.array(s_list)
    m = m_array.mean(axis=0, keepdims=True)
    s = s_array.mean(axis=0, keepdims=True)

    mean = m[0][::-1] if is_normalized else m[0][::-1]*255
    std = s[0][::-1] if is_normalized else s[0][::-1]*255
    print('mean: ',mean)
    print('std:  ',std)
    return {'mean':mean,'std':std}