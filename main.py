from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")

chrome = webdriver.Chrome("./chromedriver.exe", options=options)
chrome.get("http://klas.kw.ac.kr")
options = webdriver.ChromeOptions()
time.sleep(5)
chrome.close()