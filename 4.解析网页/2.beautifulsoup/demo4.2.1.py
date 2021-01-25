import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com"
html = requests.get(link)

soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.find_all('h1', class_='post-title')
for i in range(len(title_list)):
    title = title_list[i].a.text.strip()
    print("第 %s 个标题是： %s" % (i + 1, title))
