from selenium import webdriver

options = webdriver.ChromeOptions()
# 禁用图片，CSS，JS
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
        'permissions.default.stylesheet': 2,
        'javascript': 2
    }
}
options.add_experimental_option('prefs', prefs)
# 下载的geckodriver的存储位置
driver = webdriver.Chrome(executable_path='D:\\12102\\files\\chromedriver.exe', options=options)
# 自动访问的网站
driver.get("http://www.santostang.com/2018/07/04/hello-world/")