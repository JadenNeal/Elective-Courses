import re
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time


class GetCat:
    """
    爬虫
    目标网站：https://unsplash.com/search/photos/cat
    预计数量：6,468
    """
    def __init__(self):
        self.siteUrl = "https://unsplash.com/search/photos/cat"  # 目标网站

    def browserSetting(self):
        """
        隐式打开浏览器
        """
        opt = Options()
        opt.add_argument('--no-sandbox')       # 解决DevToolsActivePort文件不存在的报错
        opt.add_argument('--disable-gpu')      # 谷歌文档提到需要加上这个属性来规避bug
        opt.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        opt.add_argument('--headless')         # 浏览器不提供可视化页面
        excute_path = r"C:\Users\ranfe\AppData\Local\Google\Chrome\Application\chromedriver.exe"
        # 执行路径
        driver = webdriver.Chrome(chrome_options=opt, executable_path=excute_path)
        return driver

    def set_proxy(self):
        """
        设置代理IP以及User Agent
        """
        proxies = [{"https": "http://36.99.212.226:8010", "http": "http://36.99.212.226:8010"},
                   {"https": "http://121.232.148.36:9000", "http": "http://121.232.148.36:9000"},
                   {"https": "http://182.92.233.137:8118", "http": "http://182.92.233.137:8118"}]  # timeout
        proxy = random.choice(proxies)  # 选择一个代理IP
        headers = [{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/72.0.3626.121 Safari/537.36"},
                   {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 10.0; en-us) "
                                  "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                   {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"},
                   {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.01; 360SE)"}]
        header = random.choice(headers)
        return proxy, header

    def scroll_down(self, i, driver):
        """
        页面滚动
        :param driver: 浏览器脚本
        :param i: 下拉次数
        """
        print("开始执行第 %d 次下拉操作" % (i+1))
        js = "window.scrollBy(0, 500)"  # 每次下拉固定的位置
        # js = "window.scrollTo(0, document.body.scrollHeight);"  # 拉到底部
        driver.execute_script(js)  # 执行JavaScript实现网页下拉
        print("第 %d 次下拉操作执行完毕" % (i+1))
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)  # 暂停sleep_time秒下拉页面

    def siteAnalyse(self):
        """
        网站解析，一直找到图片地址
        """
        driver = self.browserSetting()
        driver.get(self.siteUrl)  # 隐式打开网页

        # proxy, header = self.set_proxy()   # 设置代理池
        for i in range(10000):
            self.scroll_down(i, driver)  # 执行i次下拉操作
            html = driver.page_source
            # requests.get(self.siteUrl, headers=header, timeout=10).text  # 请求响应
            soup = BeautifulSoup(html, "lxml")            # lxml格式解析
            div_tag = soup.find_all("div", attrs={"class": "IEpfq"})  # limit=3, 拿3个来测试。结果集，列表形式
            # print(div_tag)
            imgs = []

            patt = re.compile(r"500w,\s(.*?)\s600w")  # 找到图片网址, 宽度为600

            for img_tag in div_tag:
                elements = img_tag.find_all("img")
                for each in elements:
                    try:
                        img_address = each["srcset"]
                        img = patt.findall(img_address)
                        imgs += img  # img本身就是个列表
                    except KeyError:
                        continue

            self.saveImg(imgs)  # 保存图片

    def saveImg(self, imgs: list):
        """
        保存图片到cats文件夹中
        :param imgs: 图片列表
        """
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/72.0.3626.121 Safari/537.36"}

        os.makedirs("./cats/", exist_ok=True)     # 新建文件夹

        for img in imgs:
            img_name = img.split("-")[1] + ".jpg"  # 取编号作为图片名
            req = requests.get(img, headers=header, stream=True)   # 原始响应
            if img_name not in os.listdir(r"./cats"):
                try:
                    with open("./cats/%s" % img_name, "wb") as f:
                        for chunk in req.iter_content(chunk_size=128):
                            f.write(chunk)
                    print('Saved %s' % img_name)
                except OSError:
                    print(img_name)


if __name__ == "__main__":
    test = GetCat()
    test.siteAnalyse()
