# selenium获取文章的所有评论
from selenium import webdriver

# 下载的geckodriver的存储位置
driver = webdriver.Chrome(executable_path='D:\\12102\\files\\chromedriver.exe')
# 自动访问的网站
driver.get("http://www.santostang.com/2018/07/04/hello-world/")

# 需要提前知道ii的范围，ii指的是需要翻几次页，在我写这个代码时，评论有27页，意味着要点两次下一页，因为每页有10小页，所以ii为3
for ii in range(0, 3):
    # i指的是每页有10小页
    for i in range(0, 10):
        # 下滑到页面底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 爬取某一页的所有评论
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
        driver.implicitly_wait(10)  # 隐性等待10秒
        comment = driver.find_elements_by_css_selector('div.reply-content')
        print()
        print("第 %g 页评论:" % int(i + 1 + ii * 10))
        # 打印所有评论
        for eachcomment in comment:
            content = eachcomment.find_element_by_tag_name('p')
            print(content.text)

        # 获取所有的页码按钮
        page_btn = driver.find_elements_by_class_name("page-btn")
        # 统计这一页总共有多少页评论，默认最多为10页
        page_btn_size = len(page_btn)
        if i == page_btn_size - 1:
            driver.switch_to.default_content()
            driver.implicitly_wait(10)
            break
        # 按顺序点击某一页
        if i != 9 and i + 1 < page_btn_size:
            page_btn[i + 1].click()
        # 把iframe又转回去，注意加上这一句
        driver.switch_to.default_content()
        driver.implicitly_wait(10)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
    # 判断页面是否有下一页的按钮，没有就退出
    try:
        next_page = driver.find_element_by_class_name("page-last-btn")
        next_page.click()
        # 把iframe又转回去，注意加上这一句
        driver.switch_to.default_content()
        driver.implicitly_wait(10)
    except:
        print()
        print("爬取结束！（不是爬取内容）")
