from selenium import webdriver
from selenium.webdriver import FirefoxOptions

options = FirefoxOptions ()
options.add_argument ('--headless')
dr = webdriver.Firefox (firefox_options=options)
dr.get ("https://www.baidu.com")
print (dr.current_url)
print(dr)
