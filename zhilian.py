from bs4 import BeautifulSoup
from urllib.parse import urlencode
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
#分析url
# url ='''http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p=1&isfilter=0&fl=530&isadv=0&sg=af864477051b415891b559491f1aaa4a'''
page = 1
def params(key,page):
    return {
        'jl': key,
        'kw': 'python',
        'sm': '0',
        'p': page,
        'isfilter': 0,
        'fl': 530,
        'isadv': '0',
        'sg': 'af864477051b415891b559491f1aaa4a',
    }
def get_page(page):
    try:
        url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?' + urlencode(params('北京', 1))#注意问号
        browser.get(url)
        if page >1:
            inpuT = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#goto.pagesnum')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.nextpagego-btn')))
            inpuT.clear()
            inpuT.send_keys(page)
            submit.click()
        parse_page()
        wait.until(EC.text_to_be_present_in_element_value((By.ID,'goto'),str(page)))#value值包涵节点信息
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.pagesDown .current')))
    except TimeoutException :
        get_page(page)
def parse_page():
    html = browser.page_source
    bsObj = BeautifulSoup(html,'lxml')
    with open('./mes.txt', 'a', encoding='utf-8') as f:
        for table in bsObj.find_all('table',{'cellpadding':'0','cellspacing':'0','width':'853','class':'newlist'})[1:]:
             a =  {'job':table.tr.find('td',{'class':'zwmc'}).get_text().strip(),
                  'company':table.tr.find('td',{'class':'gsmc'}).get_text().strip(),
                 'money':table.tr.find('td', {'class': 'zwyx'}).get_text().strip(),
                'place':table.tr.find('td', {'class': 'gzdd'}).get_text().strip(),
                'time':table.tr.find('td', {'class': 'gxsj'}).get_text().strip()
                   }
             f.write(json.dumps(a,ensure_ascii=False)+'\n')


for i in range(1,90):
    get_page(i)



