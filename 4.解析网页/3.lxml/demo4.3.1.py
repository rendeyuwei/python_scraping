import requests
from lxml import etree

link = "http://www.santostang.com"
r = requests.get(link)

html = etree.HTML(r.text)
title_list = html.xpath('//h1[@class="post-title"]/a/text()')
print(title_list)
