import time

import requests
from bs4 import BeautifulSoup

for i in range(1, 11):
    link = "https://xa.zu.anjuke.com/fangyuan/p" + str(i)
    print(link)
    html = requests.get(link)

    soup = BeautifulSoup(html.text, 'lxml')

    house_list = soup.find_all('div', class_="zu-itemmod")
    print('第' + str(i) + '页数据')

    for house in house_list:
        name = house.find('div', class_='zu-info').h3.a.b.text.strip()
        price = house.find('div', class_='zu-side').p.text.strip()
        summary = house.find('p', class_='details-item').text.strip()
        address = house.find('address', class_='details-item').text.strip()

        print("名字:" + name)
        print("租金:" + price)
        print("简介：" + summary)
        print("地址：" + address)
        print()

    time.sleep(2)
