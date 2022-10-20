import math
import cv2
import os
import glob
import logging
import os
import time
from os.path import splitext
from tqdm import tqdm
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#上面两行可以防止以后出很多奇怪的导包错误


def get_all_files_pth(dir_pth:str,suffix:str=None):
    pathlist=[]#路径列表
    for home,dirs,files in os.walk(dir_pth):
        for filename in files:
            if filename.endswith(suffix):
                pathlist.append(os.path.join(home,filename))
    return pathlist
#返回dir_pth下以后缀suffix结尾的文件绝对路径的list对象
def get_file_from_dir(dir_path,suffix):#首字母大写不太符合pythonic风格
    list=[]
    needExtFilter=(suffix!=None)
    for root,dirs,files in os.walk(dir_path):
        for filespath in files:
            filepath=os.path.join(root,filespath)
            extension=os.path.splitext(filepath)[1][1:]
            if needExtFilter and extension in suffix:
                list.append(filepath)
            elif not needExtFilter:
                list.append(filepath)
    # print(list) 在轮子库中尽量避免打印输出~
    return list


def get_file_name_from_pth(fpth:str):

    for home,dirs,files in os.walk(fpth):
        for filename in files:
            basename,ext=os.path.splitext(filename)#切分文件名里面的基础名称和后缀部分
            list.append(basename)
            
'''
    
以下是我常用的一些代码，你可以参考着加到你自己的轮子库里~
    
    
'''
def auto_make_directory(dir_pth: str):
    '''
    自动检查dir_pth是否存在，若存在，返回真，若不存在创建该路径，并返回假
    :param dir_pth: 路径
    :return: bool
    '''
    if os.path.exists(dir_pth):  ##目录存在，返回为真
        return True
    else:
        os.makedirs(dir_pth)
        return False
def get_dirs_pth(dir_pth: str):
    '''
    返回返回dir_pth下文件夹路径
    :param dir_pth:
    :return: 文件夹绝对路径list
    '''
    rst = []
    for item in os.listdir(dir_pth):
        temp = os.path.join(dir_pth, item)
        if os.path.isdir(temp):
            rst.append(str(temp))
    return rst
def get_dirs_name(dir_pth: str):
    rst = []
    for item in os.listdir(dir_pth):
        temp = os.path.join(dir_pth, item)
        if os.path.isdir(temp):
            rst.append(str(item))
    return rst
def get_filename_from_pth(file_pth: str, suffix: bool = True):
    '''
    根据文件路径获取文件名
    :param file_pth:文件路径
    :return:文件名
    '''
    fname_list = os.path.split(file_pth)[1].split('.')
    if suffix: #如果保留后缀

        rst = '.'.join(fname_list)
    else:#如果不保留后缀
        rst = '.'.join(fname_list[:-1])
    return rst

def get_files_pth(dir_pth: str, suffix: str = '*'):
    '''
    返回dir_pth下以后缀名suffix结尾的文件绝对路径list
    :param dir_pth:文件夹路径
    :param suffix:限定的文件后缀
    :return: 文件绝对路径list
    '''
    rst = []
    glob_pth = os.path.join(dir_pth, f'*.{suffix}')
    for filename in glob.glob(glob_pth):
        rst.append(filename)
    return rst
def get_all_files_pth(dir_pth: str, suffix: str = None):
    '''
    获取指定文件夹下（含子目录）以指定后缀结尾的文件路径列表
    :param dir_pth: 指定文件夹路径
    :param suffix: 指定后缀
    :return:
    '''
    rst = []
    for root, dirs, files in os.walk(dir_pth):
        if len(files) > 0:
            for file_name in files:
                file_pth = os.path.join(root, file_name)
                if not suffix:
                    rst.append(file_pth)
                elif file_pth.endswith(f'.{suffix}'):
                    rst.append(file_pth)
    return rst


def get_files_name(dir_path: str, suffix: str = '*'):
    '''
    返回指定文件夹内的文件名（不带后缀）列表
    :param dir_path: 文件夹路径
    :param suffix:限定的文件后缀
    :return:文件名（不带后缀）列表
    '''
    if suffix == '*':
        ids = [splitext(file)[0] for file in os.listdir(dir_path) if not file.startswith('.')]
        return ids
    else:
        ids = [splitext(file)[0] for file in os.listdir(dir_path) if file.endswith(f'.{suffix}')]  # 获取图片名称，ids是一个列表
        return ids


def get_filename_from_pth(file_pth: str, suffix: bool = True):
    '''
    根据文件路径获取文件名
    :param file_pth:文件路径
    :return:文件名
    '''
    fname_list = os.path.split(file_pth)[1].split('.')
    if suffix: #如果保留后缀

        rst = '.'.join(fname_list)
    else:#如果不保留后缀
        rst = '.'.join(fname_list[:-1])
    return rst


def get_suffix_from_pth(file_pth: str):
    '''
    根据文件路径获取后缀
    :param file_pth:文件路径
    :return:后缀
    '''
    return os.path.split(file_pth)[1].split('.')[-1]