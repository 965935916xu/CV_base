import os
import xml.etree.ElementTree as ET

# 图像文件夹和标注文件夹的路径
img_dir = r"C:\Users\86199\Desktop\1"
ann_dir = r"C:\Users\86199\Desktop\2"

# 获取所有图像文件名
img_files = [f for f in os.listdir(img_dir) if f.endswith(".jpg")]

# 获取所有标注文件名
ann_files = [f for f in os.listdir(ann_dir) if f.endswith(".xml")]
# 创建一个集合来存储所有图像文件名
img_set = set(img_files)
ann_set = set(ann_files)

# 遍历所有标注文件,标注文件多于图片
for ann_file in ann_files:
    # 解析标注文件以获取图像文件名
    if ann_file.split('.')[0]+'.jpg' not in img_set:
        os.remove(os.path.join(ann_dir, ann_file))
# 遍历所有标注文件，图片多于标注文件
# for img_file in img_files:
#     # 解析标注文件以获取图像文件名
#     if img_file.split('.')[0]+'.xml' not in ann_set:
#         os.remove(os.path.join(img_dir, img_file))
