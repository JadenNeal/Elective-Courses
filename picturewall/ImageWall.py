from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap
from PIL import Image
import os.path
import sys


class PhotoWall(QWidget):
    def __init__(self):
        super().__init__()
        self.filepath = r"./传播智客/"    # 旧路径
        self.outpath = r"./传播智客小图/"  # 新路径

        self.setWindowTitle("照片墙")
        self.pre_process()   # 预处理图片，缩小尺寸，执行一次即可
        self.load_photo()      # 载入图片
        self.lay_photo()       # 放置图片
        self.show()            # 显示窗口

    def pre_process(self):
        """
        将图片的尺寸缩小，并存储到新的文件夹中
        :return:
        """
        self.photo_list = os.listdir(self.filepath)
        self.photo_list = [os.path.join(self.filepath, file) for file in self.photo_list]  # 旧图片的完整路径

        # print(photo_list[:2])
        for each in self.photo_list:
            img = Image.open(each)
            img = img.resize((25, 36), Image.BILINEAR)
            img.save(os.path.join(self.outpath, os.path.basename(each).split('\\')[-1]))

    def load_photo(self):
        """
        载入图片
        图片名存储到新的列表中: self.newPhotoList
        """
        self.newPhotoList = os.listdir(self.outpath)
        self.newPhotoList = [os.path.join(self.outpath, file) for file in self.newPhotoList]  # 完整路径

    def lay_photo(self):
        gLayout = QGridLayout()
        for each in self.newPhotoList:
            i = self.newPhotoList.index(each)
            picture = QLabel(self)
            picture.setPixmap(QPixmap(each))
            gLayout.addWidget(picture, self.newPhotoList.index(each) // 37, self.newPhotoList.index(each) % 37)
            # if i < 5:
            #     gLayout.addWidget(picture, 0, self.newPhotoList.index(each) % 5 + 24)
            # elif 5 <= i < 18:
            #     gLayout.addWidget(picture, 1, self.newPhotoList.index(each) % 13 + 20)
            # elif 18 <= i < 39:
            #     gLayout.addWidget(picture, 2, self.newPhotoList.index(each) % 21 + 16)
            # elif 39 <= i < 68:
            #     gLayout.addWidget(picture, 3, self.newPhotoList.index(each) % 29 + 13)
            # elif 68 <= i < 105:
            #     gLayout.addWidget(picture, 4, self.newPhotoList.index(each) % 37 + 10)
            # elif 105 <= i < 150:
            #     gLayout.addWidget(picture, 5, self.newPhotoList.index(each) % 45 + 5)
            # elif 150 <= i < 203:
            #     gLayout.addWidget(picture, 6, self.newPhotoList.index(each) % 53 + 1)
            # elif 203 <= i < 259:
            #     gLayout.addWidget(picture, 7, self.newPhotoList.index(each) % 56)
        self.setLayout(gLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhotoWall()
    app.exec_()
