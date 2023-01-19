from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument('no-sandbox')
# options.add_argument('headless')

chrome = webdriver.Chrome('./chromedriver.exe',options=options)
chrome.get('https://shopping.naver.com')
wait = WDW(chrome, 10)


def find(wait , CLASS_NAME):
    return wait.until(EC.presence_of_element_located((By.CLASS_NAME, CLASS_NAME)))


search = find(wait,"_searchInput_search_text_fSuJ6")
search.send_keys('아이폰 케이스\n')   # \n이 Enter 역할임 중요
# button = chrome.find_element(By.CLASS_NAME, '_searchInput_button_search_h79Dk')
# button.click()
time.sleep(5)
chrome.close()
