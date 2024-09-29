
"""剪切四点坐标内的固定目标，ps查看原始图片的剪裁区域内的坐标"""

# from PIL import Image
# import os
#
# srcPath = 'C:/Users/86199/Desktop/800_2/'   # 所要读取修改的文件夹
# dstPath = 'C:/Users/86199/Desktop/data20/'    # 修改后所存放路径
# filelist = os.listdir(srcPath)
#
# list1=[]
# # 读取图片
# for filename in filelist:
#     filename1 = os.path.splitext(filename)[1]  # 读取文件后缀名
#     filename0 = os.path.splitext(filename)[0]  # 读取文件名
#     list1.append(filename0+filename1)
#
# for i in range(0,len(list1)):
#     filea = str(srcPath+list1[i])
#     img_1 = Image.open(filea)
#     # 设置裁剪的位置
#     crop_box = (2418,1086,2568,1422) #ps查看图片左上角和右下角坐标  确定截取矩形区域
#
#     # 裁剪图片
#     img_2 = img_1.crop(crop_box)
#     #保存图片
#     img_2.save(dstPath+list1[i])
# print('已经截图成功')


"""在标注好xml文件后，剪裁图像内四点标注的图像，需要有VOC2007格式中的Annotations中xml文件和JPEGImages原始图片"""
import cv2
import xml.etree.ElementTree as ET
import numpy as np

import xml.dom.minidom
import os
import argparse


def main():
    # JPG文件的地址
    img_path = 'E:/data/VOC2007/JPEGImages/'
    # XML文件的地址
    anno_path = 'E:/data/VOC2007/Annotations/'
    # 存结果的文件夹

    cut_path = 'temp_imgs/cut_imgs'
    if not os.path.exists(cut_path):
        os.makedirs(cut_path)
    # 获取文件夹中的文件
    imagelist = os.listdir(img_path)
    # print(imagelist
    for image in imagelist:
        image_pre, ext = os.path.splitext(image)
        img_file = img_path + image
        img = cv2.imread(img_file)
        xml_file = anno_path + image_pre + '.xml'
        # DOMTree = xml.dom.minidom.parse(xml_file)
        # collection = DOMTree.documentElement
        # objects = collection.getElementsByTagName("object")

        tree = ET.parse(xml_file)
        root = tree.getroot()
        # if root.find('object') == None:
        #     return
        obj_i = 0
        for obj in root.iter('object'):
            obj_i += 1
            print(obj_i)
            cls = obj.find('name').text
            xmlbox = obj.find('bndbox')
            b = [int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)),
                 int(float(xmlbox.find('xmax').text)),
                 int(float(xmlbox.find('ymax').text))]
            img_cut = img[b[1]:b[3], b[0]:b[2], :]
            path = os.path.join(cut_path, cls)
            # 目录是否存在,不存在则创建
            mkdirlambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True
            mkdirlambda(path)
            try:
                cv2.imwrite(os.path.join(cut_path, cls, '{}_{:0>2d}.jpg'.format(image_pre, obj_i)), img_cut)
            except:
                continue

            print("&&&&")


if __name__ == '__main__':
    main()