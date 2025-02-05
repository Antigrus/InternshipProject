import requests
# 请求
from bs4 import BeautifulSoup
# 解析
import os

dirs = "data"
# 创建文件夹
if not os.path.exists(dirs):
    os.makedirs(dirs)

file = open('data/西游记.txt', 'w+', encoding="utf-8")

url = "https://xiyouji.5000yan.com/"
# 西游记目录
response = requests.get(url)
# 请求目录页
soup = BeautifulSoup(response.content, features="lxml")
# 解析目录页
xiyouji_chapters = soup.find('div', class_='p-2 my-2 bg-white rounded').ul.children

# 获取章回内容
for cpt in xiyouji_chapters:
    #爬取目录名
    file.write(cpt.text + "\n")

    if cpt !='\n' and cpt is not None:
        link = cpt.a.get('href')
        # 获取章节地址
        cpt_page = requests.get(link)
        # 请求章节页面
        cpt_content = BeautifulSoup(cpt_page.content, features="lxml").find('div',class_='grap')
        # 获取章节内容
        file.write(cpt_content.text)
        # 写入本地文本
file.flush()
# 把缓存中的数据写入文本
file.close()
# 关闭文本流
