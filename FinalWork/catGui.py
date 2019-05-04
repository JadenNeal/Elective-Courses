from keras.models import load_model    # 载入模型用
from keras.preprocessing import image
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import numpy as np
import sys


class CatIdentification(QWidget):
    """
    猫咪识别器
    """
    def __init__(self):
        super().__init__()  # 继承

        self.model_cat = load_model("./cats_and_dogs/cat.h5")  # 导入训练好的模型

        self.setWindowTitle("猫咪检测器")
        self.initUI()          # 初始化界面
        self.initSignalSlot()  # 连接信号和槽

        self.show()

    def initUI(self):
        """
        初始化界面
        """
        self.resize(500, 500)
        vbox = QVBoxLayout()       # 盒子布局
        self.grid = QGridLayout()  # 栅格布局

        self.grid.addWidget(QLabel("检测结果", self), 2, 0)  # 显示结果标签
        self.picLabel = QLabel(self)  # 放置图片用
        self.picLabel.setFixedSize(500, 500)
        self.picLabel.setStyleSheet("QLabel{background:white;}"
                                    "QLabel{color:rgb(300,300,300,120);font-size:20px;font-family:黑体;}")
        self.picLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.picLabel.setText("请选择图片进行检测")

        self.resLabel = QLineEdit()
        self.resLabel.setPlaceholderText("检测结果在这里显示")
        self.resLabel.setReadOnly(True)                 # 只读

        self.aboutButton = QPushButton("关于", self)     # 关于
        self.selButton = QPushButton("选择图片", self)    # 选择按钮
        self.decButton = QPushButton("检测", self)       # 检测按钮
        self.closeButton = QPushButton("退出", self)

        vbox.addWidget(self.picLabel, stretch=1)
        self.grid.addWidget(self.selButton, 1, 0)
        self.grid.addWidget(self.decButton, 1, 2)
        self.grid.addWidget(self.resLabel, 2, 2)
        self.grid.addWidget(self.closeButton, 3, 2)
        self.grid.addWidget(self.aboutButton, 3, 0)  # 暂时就先这个布局吧
        vbox.addLayout(self.grid)

        self.setLayout(vbox)

    def initSignalSlot(self):
        """
        连接信号和槽
        """
        self.selButton.clicked.connect(self.onSelButton)        # 选择图片按钮
        self.decButton.clicked.connect(self.onDetectButton)     # 检测按钮，最重要的功能
        self.aboutButton.clicked.connect(self.onAboutButton)    # 关于按钮
        self.closeButton.clicked.connect(self.onCloseButton)    # 退出按钮

    def onSelButton(self):
        """
        选择图片
        """
        self.img_name, img_type = QFileDialog.getOpenFileName(self, "选择图片", "", "*.jpg;;*.png;;*.bmp;;All Files(*)")
        # 支持类型：.jpg; .png; .bmp
        if self.img_name:
            img = QPixmap(self.img_name).scaled(self.picLabel.width(), self.picLabel.height())
            self.picLabel.setPixmap(img)

    def onDetectButton(self):
        """
        检测图片
        """
        img = image.load_img(self.img_name, target_size=(100, 100))  # 载入选择的图片
        x = image.img_to_array(img)
        x_flatten = x.reshape(1, -1)     # 展平，作为神经网络的输入
        x = x_flatten / 255.0

        result = self.model_cat.predict_classes(x)
        if result == np.array([[0]]):
            text = "It's a cat!"
        else:
            text = "It's not a cat!"
        self.resLabel.setText(text)

    def onAboutButton(self):
        """关于按钮"""
        text = "猫咪识别器    \n\n" \
               "作者：夏阁哀帝剑   \n\n"
        QMessageBox.about(self, "关于", text)

    def onCloseButton(self):
        """
        当用户点击退出时, 保障程序不会崩溃
        """
        reply = QMessageBox.question(self, "提示消息", "确定退出吗?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    font = QFont()
    font.setPointSize(15)  # 15 px
    font.setBold(True)
    splash = QSplashScreen(QPixmap("./cats_and_dogs/splash.jpg"))
    splash.setFont(font)
    splash.showMessage("应用程序加载中...", QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, QtCore.Qt.yellow)
    splash.show()

    window = CatIdentification()  # GUI窗口
    splash.finish(window)
    app.exec_()
