# 通过浏览器审查元素解析地址，爬取所有评论
import requests
import json


# 爬取某一页的评论，link为链接
def single_page_comment(link, page_number):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    r = requests.get(link, headers=headers)

    # 获取 json 的 string
    json_string = r.text
    # 将文本中的json提取出来
    json_string = json_string[json_string.find('{'):-2]
    # 测试是否提取成功
    # print(json_string)
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']
    print("       第 %g 页评论：" % page_number)
    for eachone in comment_list:
        message = eachone['content']
        print(message)
    print()


# 链接前半部分
link1 = """https://api-zero.livere.com/v1/comments/list?callback=jQuery1124027946415311453476_1602502907332&limit=10&offset="""
# 链接后半部分
link2 = """&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1602502907334"""

for page in range(1, 11):
    # 链接进行拼接，得到不同页评论的URL
    current_link = link1 + str(page) + link2
    single_page_comment(current_link, page)
