import time

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

from MongoAPI.MongoDB import MongoAPI


def get_page(link):
    r = requests.get(link)
    html = r.content
    html = html.decode('UTF-8')
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_data(post_list):
    data_list = []
    for post in post_list:
        title = post.find('a', class_='truetit').text.strip()  # 获取标题
        link1 = post.find('a', class_='truetit')['href']  # 获取帖子链接，获取a标签里的链接
        title_link = "https://bbs.hupu.com/" + link1  # 拼接起来
        author = post.find('a', class_='aulink').text.strip()
        author_link = post.find('a', class_='aulink')['href']
        time = post.find('div', class_='author').contents[1].text.strip()  # 注意使用contents获取子标签
        reply = post.find('span', class_='ansour').text.strip().split('/')[0].strip()
        watch = post.find('span', class_='ansour').text.strip().split('/')[1].strip()
        last_reply_time = post.find('div', class_='endreply').a.text.strip()
        last_reply_author = post.find('span', class_='endauthor').text.strip()

        data_list.append(
            [title, title_link, author, author_link, time, reply, watch, last_reply_time, last_reply_author])
    return data_list


hupu_post = MongoAPI("localhost", 27017, "hupu", "post")
link = 'https://bbs.hupu.com/bxj-'
for i in range(10):
    new_link = link + str(i + 1)
    soup = get_page(new_link)
    # post_list = soup.find('ul', class_='for-list').find('li')
    post_list = soup.select("div.show-list ul li")  # 获取所有的li
    # print(len(post_list))
    data_list = get_data(post_list)
    print("第 %s 页帖子数据:" % str(i + 1))
    for each in data_list:
        print(each)
        hupu_post.update({"post_link": each[1]}, {
            "title": each[0],
            "post_link": each[1],
            "author": each[2],
            "author_page": each[3],
            "start_date": str(each[4]),
            "reply": each[5],
            "view": each[6],
            "last_reply_time": str(each[7]),
            "last_reply_author": each[8]
        })
    time.sleep(3)
    print("第 %s 页获取完成休息3秒" % str(i+1))
