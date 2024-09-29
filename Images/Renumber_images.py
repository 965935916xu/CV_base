
import os
import re


def ReName(dir_Path, pattern):
    i = 1
    for filename in os.listdir(dir_Path):
        print(filename)
        new_filename = "imgs" + str(i) + ".jpg"  #可以在中间加上"image"+ 重命名
        print(new_filename)
        os.rename(os.path.join(dir_Path, filename), os.path.join(dir_Path, new_filename))
        i = i + 1

    print("----------Success!-------------")


if __name__ == '__main__':
    dir_Path = r"E:\data\VOC2007\JPEGImages"
    pattern = re.compile(r'.*')
    ReName(dir_Path, pattern)
