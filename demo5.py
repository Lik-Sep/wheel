import os
#返回dir_pth下以后缀suffix结尾的文件绝对路径的list对象
def GetFileFromDir(dir_path,suffix):
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
    print(list)
    return list
GetFileFromDir('D:\opencvTest','xml')