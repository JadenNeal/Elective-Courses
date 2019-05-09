from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from pdf_process import pdfProcess  # 导入自己的pdf处理接口
import sys


class MyGui(QWidget):
    """
    交互处理pdf
    需要注意：查看文件信息、旋转页面、加密文档功能均使用同一个选择文件按钮
    """
    def __init__(self):
        """
        初始化
        """
        super().__init__()    # 继承QWidget所有函数
        self.pypdf = pdfProcess.MyPdf()  # 导入类接口，必须这么写，因为pdfProcess开头还调用了其他模块

        self.setWindowTitle("PDF处理器")
        self.initUI()          # 初始化界面
        self.initSignalSlot()  # 连接信号与槽

        self.show()            # 显示窗口

    def initUI(self):
        """
        UI界面管理
        """
        vbox = QVBoxLayout()  # 盒子布局
        grid = QGridLayout()  # 栅格布局

        self.nameLabel = QLineEdit()          # 显示文件名称
        self.nameLabel.setPlaceholderText("文件名称")
        self.nameLabel.setReadOnly(True)      # 只读

        self.infoLabel = QTextEdit()  # 显示文件名称
        self.infoLabel.setPlaceholderText("文件信息")  # 需要设置为多行显示
        self.infoLabel.setReadOnly(True)  # 只读

        self.mergeLabel = QLineEdit()  # 显示文件名称
        self.mergeLabel.setPlaceholderText("合并文件输出结果")
        self.mergeLabel.setReadOnly(True)  # 只读

        self.splitLabel = QLineEdit()  # 显示文件名称
        self.splitLabel.setPlaceholderText("切分页面输出结果")
        self.splitLabel.setReadOnly(True)  # 只读

        self.blankLabel = QLineEdit()  # 显示文件名称
        self.blankLabel.setPlaceholderText("加入空白页输出结果")
        self.blankLabel.setReadOnly(True)  # 只读

        grid.addWidget(QLabel("", self), 5, 0)
        grid.addWidget(QLabel("选择页数（从0开始）", self), 6, 0)
        grid.addWidget(QLabel("0:顺时针，1:逆时针", self), 7, 0)
        grid.addWidget(QLabel("", self), 9, 0)
        self.rotatePageLabel = QLineEdit()
        self.rotatePageLabel.setPlaceholderText("选择页数")  # 选择需要旋转的页面编号

        self.rotateTypeLabel = QLineEdit()
        self.rotateTypeLabel.setPlaceholderText("选择操作类型")  # 选择顺时针或者逆时针操作

        self.rotateLabel = QLineEdit()  # 显示文件名称
        self.rotateLabel.setPlaceholderText("旋转页面输出结果")
        self.rotateLabel.setReadOnly(True)  # 只读

        self.watermarkLabel = QLineEdit()  # 显示文件名称
        self.watermarkLabel.setPlaceholderText("添加水印输出结果")
        self.watermarkLabel.setReadOnly(True)  # 只读

        self.password = QLabel("输入密码", self)
        self.password.setAlignment(QtCore.Qt.AlignCenter)

        self.passwordLabel = QLineEdit()
        self.passwordLabel.setPlaceholderText("在这里输入密码")

        self.encryptLabel = QLineEdit()
        self.encryptLabel.setPlaceholderText("文档加密输出结果")
        self.encryptLabel.setReadOnly(True)  # 只读

        self.nameButton = QPushButton("选择文件", self)       # 选择文件按钮
        self.infoButton = QPushButton("文件信息", self)       # 文件信息按钮
        self.mergeButton = QPushButton("合并文件", self)      # 合并文件按钮
        self.splitButton = QPushButton("切分文件", self)      # 切分文件按钮
        self.blankButton = QPushButton("加空白页", self)      # 加入空白页
        self.rotateButton = QPushButton("旋转页面", self)     # 旋转页面按钮
        self.watermarkButton = QPushButton("添加水印", self)  # 添加水印按钮
        self.encryptButton = QPushButton("加密文档", self)    # 文档加密按钮
        self.aboutButton = QPushButton("关于", self)         # 关于按钮
        self.closeButton = QPushButton("退出", self)         # 退出按钮

        grid.addWidget(self.nameButton, 0, 0)
        grid.addWidget(self.nameLabel, 0, 1)
        grid.addWidget(self.infoButton, 1, 0)
        grid.addWidget(self.infoLabel, 1, 1)
        grid.addWidget(self.mergeButton, 2, 0)
        grid.addWidget(self.mergeLabel, 2, 1)
        grid.addWidget(self.splitButton, 3, 0)
        grid.addWidget(self.splitLabel, 3, 1)
        grid.addWidget(self.blankButton, 4, 0)
        grid.addWidget(self.blankLabel, 4, 1)
        grid.addWidget(self.rotatePageLabel, 6, 1)
        grid.addWidget(self.rotateTypeLabel, 7, 1)
        grid.addWidget(self.rotateButton, 8, 0)
        grid.addWidget(self.rotateLabel, 8, 1)
        grid.addWidget(self.watermarkButton, 10, 0)
        grid.addWidget(self.watermarkLabel, 10, 1)
        grid.addWidget(self.password, 11, 0)
        grid.addWidget(self.passwordLabel, 11, 1)
        grid.addWidget(self.encryptButton, 12, 0)
        grid.addWidget(self.encryptLabel, 12, 1)
        grid.addWidget(self.aboutButton, 13, 0)
        grid.addWidget(self.closeButton, 13, 1)
        vbox.addLayout(grid)

        self.setLayout(vbox)

    def initSignalSlot(self):
        """
        连接信号与槽
        """
        self.nameButton.clicked.connect(self.onNameButton)            # 选择文件按钮
        self.infoButton.clicked.connect(self.onInfoButton)            # 文件信息按钮
        self.mergeButton.clicked.connect(self.onMergeButton)          # 合并文件按钮
        self.splitButton.clicked.connect(self.onSplitButton)          # 切分文件按钮
        self.blankButton.clicked.connect(self.onBlankButton)          # 加空白页按钮
        self.rotateButton.clicked.connect(self.onRotateButton)        # 旋转页面按钮
        self.watermarkButton.clicked.connect(self.onWatermarkButton)  # 添加水印按钮
        self.encryptButton.clicked.connect(self.onEncryptButton)      # 文档加密按钮
        self.aboutButton.clicked.connect(self.onAboutButton)          # 关于程序按钮
        self.closeButton.clicked.connect(self.onCloseButton)          # 退出程序按钮

    def onNameButton(self):
        """
        选择文件
        """
        self.pdf_name, _ = QFileDialog.getOpenFileName(self, "选择要查看的文件", "", "*.pdf")
        # 打开pdf文件
        if self.pdf_name:
            self.nameLabel.setText(self.pdf_name)
            # 这里self.pdf_name为pdf文件的完整路径

    def onInfoButton(self):
        """
        获取文件信息功能
        """
        info, page_num = self.pypdf.pdf_info(self.pdf_name)
        info = dict(info)
        self.infoLabel.append("页数：" + str(page_num) + "\n")
        for k, v in info.items():
            self.infoLabel.append(k + ": " + v + "\n")

    def onMergeButton(self):
        """
        合并文件
        """
        names, _ = QFileDialog.getOpenFileNames(self, "选择多个文件", "", "pdf files(*.pdf)")
        text = self.pypdf.merge_pdf(names, "merge_res.pdf")

        self.mergeLabel.setText(text)

    def onSplitButton(self):
        """
        切分pdf文件
        """
        name, _ = QFileDialog.getOpenFileName(self, "选择要切分的文件", "", "*.pdf")
        text = self.pypdf.split_pdf(name, "split")
        self.splitLabel.setText(text)

    def onBlankButton(self):
        """
        在文件末尾插入空白页
        """
        name, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "*.pdf")
        text = self.pypdf.add_page(name)
        self.blankLabel.setText(text)

    def onRotateButton(self):
        """
        将某页面旋转
        """
        page_num = self.rotatePageLabel.text()
        rotate_type = self.rotateTypeLabel.text()

        text = self.pypdf.rotate_pdf(self.pdf_name, page_num, rotate_type, "rotate.pdf")
        self.rotateLabel.setText(text)

    def onWatermarkButton(self):
        """
        添加水印
        """
        inputpdf, _ = QFileDialog.getOpenFileName(self, "选择原始文件", "", "*.pdf")
        watermark, _ = QFileDialog.getOpenFileName(self, "选择水印文件", "", "*.pdf")

        text = self.pypdf.add_watermark(inputpdf, "watermark.pdf", watermark)
        self.watermarkLabel.setText(text)

    def onEncryptButton(self):
        password = self.passwordLabel.text()  # 获取密码

        text = self.pypdf.encrypt_pdf(self.pdf_name, "encrypted.pdf", password)
        self.encryptLabel.setText(text)       # 输出结果

    def onAboutButton(self):
        """
        关于按钮
        """
        text = "名称：pdf处理器    \n\n" \
               "作者：夏阁哀帝剑"
        QMessageBox.about(self, "关于", text)

    def onCloseButton(self):
        """
        关闭按钮
        """
        reply = QMessageBox.question(self, "提示消息", "确定退出吗?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyGui()
    app.exec_()
