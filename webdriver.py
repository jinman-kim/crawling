from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pyperclip

# selenium -> chrome 에 http response 던져주기
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument('no-sandbox')
# options.add_argument('headless') #화면 안 띄우기 ㅇㅋㅇㅋ?

chrome = webdriver.Chrome('./chromedriver.exe', options=options) # Debug모드 ,크롬
# chrome.implicitly_wait(3) # 크롬드라이버가 멈춤
short_wait = WDW(chrome,3)
wait = WDW(chrome, 10)

chrome.get('https://shopping.naver.com')
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'a#gnb_login_button'))) # a 태그의 id
# login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'a#gnb_login_button'))) # a 태그의 id
print(login_button.text)
login_button.click()

time.sleep(3)
chrome.close()

