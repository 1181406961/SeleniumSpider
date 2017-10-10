from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import json
# browser =webdriver.Chrome()
# wait = WebDriverWait(browser,10)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)#无头浏览器
wait = WebDriverWait(browser,10)
def get_page(page):
    try:
        url = 'https://zh.airbnb.com/s/Shenzhen--China?page='+str(page)
        print(url)
        browser.get(url)
        divmessage = wait.until(
            EC.presence_of_all_elements_located((By.XPATH,'//div[@class="_gig1e7"]'))
        )
        for item in deal_page(browser.page_source):
            save_page(item)

    except TimeoutException:
        get_page(page)
def deal_page(html):
    bs4 = BeautifulSoup(html,'lxml')
    items = bs4.find_all('div',{'class':'_1uyh6pwn'})
    for item in items:
        yield  {'price' : item.find('div',{'class':"_ij17et"}).find('span',{'class':"_up0n8v6"}).span.next_sibling.get_text(),
        'address' : item.find('div',{'class':'_1ap4g6fo'}).find('span',{'class':"_1jhetorm"}).span.get_text(),
        'detail'  : item.find('div',{'class':"_144gzuv"}).find('span',{'class':"_2a3fke5"}).find('span',{'class':"_j1kt73"}).get_text()
        }
def save_page(item):
    with open('./message.txt','a+',encoding='utf-8') as f:#注意编码格式
        f.write(json.dumps(item,ensure_ascii=False)+'\n')
#
try:
    for i in range(1,18):
        get_page(i)
finally:
    browser.close()

