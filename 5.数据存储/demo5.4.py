import datetime

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

link = "http://www.santostang.com"
html = requests.get(link)

# 连接MongoDB数据库
client = MongoClient('localhost', 27017)
db = client.blog_database
collection = db.blog

soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.find_all('h1', class_='post-title')
for i in range(len(title_list)):
    url = title_list[i].a['href']
    title = title_list[i].a.text.strip()
    post = {
        "url": url,
        "title": title,
        "date": datetime.datetime.utcnow()
    }
    collection.insert_one(post)
