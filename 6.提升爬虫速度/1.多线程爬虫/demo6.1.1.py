import requests
import time

link_list = []
with open('../alexa.txt', 'r') as file:
    file_list = file.readlines()
    for each in file_list:
        link = each.split('\t')[1]
        link = link.replace('\n', '')
        link_list.append(link)

    start = time.time()
    for each in link_list:
        try:
            r = requests.get(each)
            print(r.status_code, each)
        except Exception as e:
            print(e)
    end = time.time()
    print("串行总时间为", end - start)
