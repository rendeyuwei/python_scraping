import requests
from bs4 import BeautifulSoup


def getTop250():
    movie_list = []
    for i in range(0, 10):
        http = "https://movie.douban.com/top250?start=" + str(i * 25)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
            'Host': 'movie.douban.com'
        }
        r = requests.get(http, headers=headers)

        # BeautifulSoup对内容解析
        soup = BeautifulSoup(r.text, "html.parser")

        list = soup.find_all('div', class_='hd')
        for each in list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)

    return movie_list


movie_list = getTop250()
for (index, movie) in enumerate(movie_list):
    print(index + 1, '. ', movie)
