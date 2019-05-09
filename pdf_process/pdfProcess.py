from PyPDF4 import PdfFileReader, PdfFileWriter
import os


class MyPdf:
    """
    pdf处理
    """
    def __init__(self):
        """
        初始化函数
        """
        self.processed = "./processed/"
        os.makedirs(self.processed, exist_ok=True)   # 处理后的文件存放处

    def pdf_info(self, pdfpath):
        """
        pdf文件信息
        path：pdf文件路径
        """
        with open(pdfpath, "rb") as f:
            pdf = PdfFileReader(f)          # 读取pdf文件
            info = pdf.getDocumentInfo()    # 返回的pdf信息为字典格式
            '''
            Author:   {info.author}
            Creator:  {info.creator}
            Producer: {info.producer}
            Subject:  {info.subject}
            Title:    {info.title}
            '''
            page_num = pdf.getNumPages()    # 得到pdf页数

        return info, page_num

    def merge_pdf(self, file_list, outpdf):
        """
        合并pdf文件
        outpdf: 输出的pdf名称，不包含路径,如：merge_res.pdf
        """
        pdf_writer = PdfFileWriter()

        for eve in file_list:
            pdf_reader = PdfFileReader(eve)
            for page in range(pdf_reader.getNumPages()):
                # 将每一页添加到writer对象中
                pdf_writer.addPage(pdf_reader.getPage(page))

        # 写入合并的pdf文件
        with open(self.processed + outpdf, "wb") as f:
            pdf_writer.write(f)

        # print("合并完成！")
        return "合并完成！"

    def split_pdf(self, path: str, name_of_split: str):
        """
        切分pdf文件
        path: 原始文件存放路径
        name_of_split:切分后的文件名，不包含后缀
        """
        pdf = PdfFileReader(path)
        pdf_writer = PdfFileWriter()
        for page in range(pdf.getNumPages()):
            pdf_writer.addPage(pdf.getPage(page))

            output = self.processed + name_of_split + str(page) + ".pdf"
            with open(output, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

        # print("切分完成！")
        return "切分完成！"

    def add_page(self, path: str):
        """
        添加空白页面
        path:文件完整路径
        """
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(path)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.addBlankPage()      # 插入空白页面

        with open("./processed/add_blank.pdf", "wb") as f:
            pdf_writer.write(f)

        # print("加入空白页完成！")
        return "添加空白页完成！"

    def rotate_pdf(self, path: str, page_num: str, rotate_type: str, outpdf: str):
        """
        旋转pdf页面
        path； 需要处理的pdf文件路径
        page_num: 页面编号
        rotate_type: 0或1，为顺时针或逆时针旋转
        outpdf: 输出pdf名称，不包含路径
        """
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(path)

        # 顺时针旋转90°
        if rotate_type == "0":
            page_1 = pdf_reader.getPage(int(page_num)).rotateClockwise(90)
            pdf_writer.addPage(page_1)

        elif rotate_type == "1":
            # 逆时针旋转90°
            page_2 = pdf_reader.getPage(int(page_num)).rotateCounterClockwise(90)
            pdf_writer.addPage(page_2)

        else:
            return "输入错误，请重新输入！"

        with open(self.processed + outpdf, "wb") as f:
            pdf_writer.write(f)

        # print("旋转页面完成！")
        return "旋转页面完成！"

    def add_watermark(self, inputpdf, outpdf, watermark):
        """
        添加水印
        inputpdf；输入的pdf名称，包含路径
        outpdf:输出的pdf名称，不包含路径
        需要注意的是，存放水印的pdf的第一页就是水印
        """
        watermark_obj = PdfFileReader(watermark)  # 带文字或图像的pdf
        watermark_page = watermark_obj.getPage(0)

        pdf_reader = PdfFileReader(inputpdf)
        pdf_writer = PdfFileWriter()

        # 给所有页面添加水印
        for page in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)

        with open(self.processed+outpdf, 'wb') as out:
            pdf_writer.write(out)

        # print("添加水印完成！")
        return "添加水印完成！"

    def encrypt_pdf(self, inputpdf, outpdf, password):
        """
        加密pdf
        inputpdf: 输入的pdf名称，包含路径
        outpdf: 输出的pdf名称，不包含路径
        """
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(inputpdf)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=password, use_128bit=True)
        # 默认为40bit加密

        with open(self.processed + outpdf, 'wb') as f:
            pdf_writer.write(f)

        # print("文档加密完成！")
        return "文档加密完成！"
