import os
from os.path import basename


def get_file_name_from_pth(fpth:str):

    for home,dirs,files in os.walk(fpth):
        for filename in files:
            basename,ext=os.path.splitext(filename)#切分文件名里面的基础名称和后缀部分
            list.append(basename)
    #return list
list=[]#文件名列表
get_file_name_from_pth('C:/Users/Lenovo/Desktop/test/A2.1/')
for i in range(list.__len__()):
    print(list[i])