#-*- encoding:utf-8 -*-

from xml.etree.ElementTree import parse,Element
import os

filePath = '/home/gcnan604/py-faster-rcnn/data/VOCdevkit2007/VOC2007/Annotations/'

#获取目录下的所有文件
dir_list = os.listdir(filePath)


def modifyXMLFile(name):
    #print type(name)
    #读入一个xml文件
    currentFile = parse(filePath+name)
    root = currentFile.getroot()

    #将floder节点内容替换成VOC2007
    for fld in root.iter('folder'):
        fld.text = 'VOC2007'

    #为filename节点添加后缀名
    for filename in root.iter('filename'):
        filename.text = str(name).split('.')[0]+'.jpg'
    #移除path节点
    for path in root.findall('path'):
        root.remove(path)
    #保存修改后的文件
    currentFile.write(filePath + name)

    print name + " has been modified!"

for filename in dir_list:
    if (str(filename).split('.')[1] == 'xml'):
        modifyXMLFile(filename)
