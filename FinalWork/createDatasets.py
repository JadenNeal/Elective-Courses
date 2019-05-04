import os
import h5py
import numpy as np
from PIL import Image


class CreateDatasets:
    """
    首先进行resize，将尺寸处理成一致的
    然后读取图片，形成numpy的array格式
    最后写入h5文件
    """
    def __init__(self):
        self.filepath = r"D:\Py_projects\Deeplearning\cats_and_dogs\test"
        # 确保移植性,这里给了绝对路径；验证、测试集都可以根据这个修改
        # os.chdir(self.filepath)
        self.file_list = os.listdir(self.filepath)
        self.file_list = [os.path.join(self.filepath, file) for file in self.file_list]  # 完整路径

        # self.preprocessPic()  # 图片预处理
        self.createH5(datapath="./cats_and_dogs/newPic/train/", h5name="./cats_and_dogs/datasets/train_set.h5",
                      set_x_name="train_set_x", set_y_name="train_set_y")       # 创建训练集
        self.createH5(datapath="./cats_and_dogs/newPic/validation/", h5name="./cats_and_dogs/datasets/valid_set.h5",
                      set_x_name="valid_set_x", set_y_name="valid_set_y")  # 创建测试集
        self.createH5(datapath="./cats_and_dogs/newPic/test/", h5name="./cats_and_dogs/datasets/test_set.h5",
                      set_x_name="test_set_x", set_y_name="test_set_y")         # 创建测试集

    def preprocessPic(self):
        """
        图片预处理，均为100x100的，算比较大的
        """
        new_path = "D:/Py_projects/Deeplearning/cats_and_dogs/newPic/test/"
        os.makedirs(new_path, exist_ok=True)
        for eachPic in self.file_list:
            # print(eachPic)
            img_name = eachPic.split("\\")[-1]
            img = Image.open(eachPic)  # 图像模式可不填
            try:
                img = img.resize((100, 100), Image.ANTIALIAS)  # 不会造成信息失真
                img.save(new_path + img_name, quality=80)
            except OSError:
                print(eachPic)    # 尺寸不够大，对于该图片来说不是缩放

    def createH5(self, datapath, h5name: str, set_x_name: str, set_y_name: str):
        """
        创建h5文件
        train_set.h5:训练集.train_set_x:猫和狗的图片; train_set_y:猫：0，狗：1
        valid_set.h5:验证集.valid_set_x:猫和狗的图片；valid_set_y:猫：0，狗：1
        test_set.h5:测试集.test_set_x:猫和狗的图片；test_set_y:猫：0，狗：1
        """
        # datapath是预处理后的图片路径，比如训练集：./cats_and_dogs/newPic/train/
        pic_list = os.listdir(datapath)  # pic_list是图片名列表，不是完整路径
        x_data = []
        y_data = []
        for eachPic in pic_list:
            if eachPic.split(".")[0] == "cat":
                y_data.append(0)   # cat标签为0
            else:
                y_data.append(1)   # dog标签为1
            img = Image.open(datapath + eachPic)
            x_data.append(np.asarray(img))

        y_data = np.asarray(y_data)  # 转换成array格式

        with h5py.File(h5name, "w") as f:
            f.create_dataset(set_x_name, data=x_data)
            f.create_dataset(set_y_name, data=y_data)


if __name__ == "__main__":
    datasets = CreateDatasets()
