# selenium的实战案例-爬取一条评论
from selenium import webdriver

# 下载的geckodriver的存储位置
driver = webdriver.Chrome(executable_path='D:\\12102\\files\\chromedriver.exe')
# 自动访问的网站
driver.get("http://www.santostang.com/2018/07/04/hello-world/")

# 错误范例，注意函数的名称，elements与element的区别
# 爬取一条评论
# switch_to相当于转移焦点
# driver.switch_to.frame(driver.find_elements_by_css_selector("iframe[title='livere-comment']"))
# comment = driver.find_elements_by_css_selector("div.reply-content")
# content = comment.find_element_by_tag_name('p')
# print(content.text)

# 爬取一条评论
# switch_to相当于转移焦点
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
driver.implicitly_wait(10)  # 隐性等待10秒
comment = driver.find_element_by_css_selector('div.reply-content')
content = comment.find_element_by_tag_name('p')
print(content.text)
