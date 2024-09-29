import cv2
import os


class video():
    def __init__(self):
        self.start_name = '0000000.jpg'
        self.timeF = 25  #选择按帧提取

    def cut(self, video_path, save_path):

        filename = os.listdir(video_path)
        n = 0

        for name in filename:
            name = video_path + name
            cv = cv2.VideoCapture(name)  # 读入视频文件，命名cv

            if cv.isOpened():  # 判断是否正常打开
                rval, frame = cv.read()
                i = 1
            else:
                rval = False
                print('open video error!!')

            while rval:  # 正常打开 开始处理
                rval, frame = cv.read()
                jpg_name = save_path + str(int(self.start_name[0:-4]) + n).zfill(6) + '.jpg'  # 命名保存的图片

                if (i % self.timeF == 0):  # 每隔timeF帧进行存储操作
                    n += 1
                    try:
                        cv2.imwrite(jpg_name, frame)  # 存储为图像
                    except:
                        pass
                    # print(jpg_name)
                i += 1
            cv2.waitKey(1)
            cv.release()
            print(name + ' done')
        print('cut video done')


if __name__ == "__main__":

    video_path = 'C:/Learn/xiangmu/video_cut/VIdeo/'  # 设置为视频文件存储的路径即可
    img_path = 'C:/Learn/data/MVS/imgs/'

    if not os.path.exists(img_path):  # 如果存储图片的文件夹不存在，自动创建保存图片文件夹
        os.makedirs(img_path)
    v = video()
    v.cut(video_path, img_path)  # 执行提取图片程序
