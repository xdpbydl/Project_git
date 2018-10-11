from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re,time,random
from pyquery import PyQuery as pq

brower = webdriver.Firefox()
wait = WebDriverWait(brower,10)
def search():
    try:
        brower.get('https://www.xiami.com/genre/songs/gid/12')
    except TimeoutError:
        return  search()

def eline():
    for i in range(1,25):

        flag = '#songs > div > div:nth-child({}) > div.info > p:nth-child(1) > strong > a'.format(i)
        submit = wait.until (EC.element_to_be_clickable((By.CSS_SELECTOR, flag)))
        submit.click ()
        # a = random.randrange(3, 30)
        # time.sleep(a)
        brower.switch_to_window (brower.window_handles[1])
        title = brower.find_element (By.CSS_SELECTOR, '#title > h1').text
        shit = brower.find_element (By.CSS_SELECTOR, '#play_count_num').text[:-3]
        fenx = brower.find_element (By.CSS_SELECTOR, '#sidebar > div.music_counts > ul > li:nth-child(2)').text[:-3]
        pingl = brower.find_element (By.CSS_SELECTOR, '#sidebar > div.music_counts > ul > li:nth-child(3) > a').text[:-3]
        # link = brower.find_element (By.CSS_SELECTOR, '#sidebar > div.music_counts > ul > li:nth-child(3) > a').text
        print(title, shit, fenx, pingl)
        print ('----------------------')
        a = random.randrange(3, 30)
        time.sleep(a)
        brower.close()
        brower.switch_to_window (brower.window_handles[0])
        a = random.randrange(10, 44)
        time.sleep(a)


if __name__ == '__main__':
    search ()
    eline ()
