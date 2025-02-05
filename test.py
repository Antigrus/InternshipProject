import requests
# 请求
from bs4 import BeautifulSoup
# 解析
import os

dirs = "data"
# 创建文件夹
if not os.path.exists(dirs):
    os.makedirs(dirs)

file = open('data/世说新语.txt', 'w+', encoding="utf-8")

url = "https://shishuoxinyu.5000yan.com/"
# 西游记目录
response = requests.get(url)
# 请求目录页
soup = BeautifulSoup(response.content, features="lxml")
# 解析目录页
xiyouji_chapters = soup.find_all('div', class_='p-3 my-2 bg-white rounded')[1].ul.children

# 获取章回内容
for cpt in xiyouji_chapters:
    file.write(cpt.text + "\n")
    if cpt !='\n' and cpt is not None:
        link = cpt.a.get('href')
        # 获取章节地址
        cpt_page = requests.get(link)
        # 请求章节页面
        cpt_content = BeautifulSoup(cpt_page.content, features="lxml").find_all('h5',class_='mb-1 lh-base')
        # 获取章节内容
        for content in cpt_content:
            file.write(content.text+'\n')
        # 写入本地文本
file.flush()
# 把缓存中的数据写入文本
file.close()
# 关闭文本流
