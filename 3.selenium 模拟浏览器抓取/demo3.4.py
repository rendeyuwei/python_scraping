# selenium获取文章的所有评论
from selenium import webdriver

# 下载的geckodriver的存储位置
driver = webdriver.Chrome(executable_path='D:\\12102\\files\\chromedriver.exe')
# 自动访问的网站
driver.get("https://www.airbnb.cn/s/%E8%A5%BF%E5%AE%89/homes?refinement_paths%5B%5D=%2Fhomes")

# 找出所有的出租房
rent_list = driver.find_elements_by_css_selector('div._qlq27g')

for each_house in rent_list:
    comment = each_house