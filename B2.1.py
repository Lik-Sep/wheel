import math
import cv2
import os

def get_all_files_pth(dir_pth:str,suffix:str=None):
    pathlist=[]#路径列表
    for home,dirs,files in os.walk(dir_pth):
        for filename in files:
            if filename.endswith(suffix):
                pathlist.append(os.path.join(home,filename))
    return pathlist

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

list=get_all_files_pth("D:/test",'txt')
for i in range(0, list.__len__()):
    print(list[i])
a=cal_mean_std("D:/test")
print(a)




