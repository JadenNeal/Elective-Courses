import requests
from bs4 import BeautifulSoup
import os
# 爬取传播智客网站

ul = 'http://www.itcast.cn/channel/teacher.shtml#ajavaee'
html = requests.get(ul).text
main_url = 'http://www.itcast.cn'
# print(html)
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('div', {'class': 'li_img'})

os.makedirs('./传播智客/', exist_ok=True)

for ul in img_ul:
    imgs = ul.find_all('img')
    # print(imgs)
    for img in imgs:
        url = img['data-original']
        img_name = url.split('/')[-1]
        req = requests.get(main_url+url, stream=True)
        with open('./传播智客/%s' % img_name, 'wb') as f:
            for chunk in req.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % img_name)
