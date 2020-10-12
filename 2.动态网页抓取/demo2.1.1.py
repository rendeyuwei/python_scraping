# 通过浏览器审查元素解析地址，爬取第一页评论
import requests
import json

link = """https://api-zero.livere.com/v1/comments/list?callback=jQuery1124027946415311453476_1602502907332&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1602502907334"""
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
r = requests.get(link, headers=headers)
print(r.text)

# 获取 json 的 string
json_string = r.text
# 将文本中的json提取出来
json_string = json_string[json_string.find('{'):-2]
# 测试是否提取成功
print(json_string)
json_data = json.loads(json_string)
comment_list = json_data['results']['parents']
for eachone in comment_list:
    message = eachone['content']
    print(message)
