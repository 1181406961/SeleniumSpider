''''''
'''# 学习使用selenium模拟浏览器
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# brower = webdriver.Chrome()
# try:
#     brower.get('https://www.baidu.com')
#     inpuT = brower.find_element_by_id('kw')
#     inpuT.send_keys('Python')
#     inpuT.send_keys(Keys.ENTER)
#     wait = WebDriverWait(brower,10)
#     wait.until(EC.presence_of_all_elements_located((By.ID,'content_left')))
#     #当前的 URL、Cookies、源代码
#     print(brower.current_url)
#     print( brower.get_cookies())
#     print(brower.page_source)
# finally:
#     brower.close()
'''

'''# from selenium import webdriver
# brower = webdriver.Chrome()
# brower.get('https://www.taobao.com')
# print(brower.page_source)
# brower.close()


# from selenium import webdriver
# brower = webdriver.Chrome()
# brower.get('https://www.taobao.com')
# #使用了三种方式获取输入框
# input_first = brower.find_element_by_id('mq')
# input_second = brower.find_element_by_css_selector('#mq')
# input_third = brower.find_element_by_xpath('//*[@id="mq"]')
# print(input_first,input_second,input_third)
# brower.close()
# <selenium.webdriver.remote.webelement.WebElement (session="78da37d728ab680274dda0699c028731", element="0.2709059677565382-1")>
# <selenium.webdriver.remote.webelement.WebElement (session="78da37d728ab680274dda0699c028731", element="0.2709059677565382-1")>
# <selenium.webdriver.remote.webelement.WebElement (session="78da37d728ab680274dda0699c028731", element="0.2709059677565382-1")>
# 在这里列出所有获取单个节点的方法：
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# brower = webdriver.Chrome()
# brower.get('https://www.taobao.com')
# input_first = brower.find_element(By.ID,'mq')
# print(input_first)
# brower.close()


# from selenium import webdriver
# brower = webdriver.Chrome()
# brower.get('https://www.taobao.com')
# lis = brower.find_elements_by_xpath('//div[contains(@class,"cat cat-")]')
# print(lis)
# brower.close()
# 用 find_element() 方法，只能获取匹配的第一个节点，结果是 WebElement 类型，
# 如果用 find_elements() 方法，则结果是列表类型，列表的每个节点是 WebElement 类型。
# [<selenium.webdriver.remote.webelement.WebElement (session="c1b7903f7fa8837951b2435a48b6e0f8", element="0.5660997869239812-1")>,
# <selenium.webdriver.remote.webelement.WebElement (session="c1b7903f7fa8837951b2435a48b6e0f8", element="0.5660997869239812-2")>,
# <selenium.webdriver.remote.webelement.WebElement (session="c1b7903f7fa8837951b2435a48b6e0f8", element="0.5660997869239812-3")>,……
#函数的列表如下：
# find_elements_by_id
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector


# from selenium import webdriver
# import time
# brower = webdriver.Chrome()
# brower.get('https://www.taobao.com')
# inpuT = brower.find_element_by_id('mq')
# inpuT.send_keys('iPhone')
# time.sleep(1)
# inpuT.clear()
# inpuT.send_keys('iPad')
# button =brower.find_element_by_xpath('//div[@class="sb-search"]/form[@target="_self"]/input[@type="submit"]')
# button.click()
#输入文字用 send_keys() 方法，清空文字用 clear() 方法，另外还有按钮点击，用 click() 方法
# 更多操作，见官方文档http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement
# 首先驱动浏览器打开淘宝，然后用 find_element_by_id() 方法获取输入框，
# 然后用 send_keys() 方法输入 iPhone 文字，等待一秒之后用 clear() 方法清空输入框，
# 再次调用 send_keys() 方法输入 iPad 文字，之后再用 find_element_by_class_name() 方法获取搜索按钮，
# 最后调用 click() 方法完成搜索动作


#动作链
# 存在一些操作它是没有特定的执行对象的，比如鼠标拖拽、键盘按键等操作，这些动作有另一种方式来执行，那就是动作链。
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# brower = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# brower.get(url)
# brower.switch_to.frame('iframeResult')#切换到HTML的iframe上(iframe 元素会创建包含另外一个文档的内联框架（即行内框架))
# source = brower.find_element_by_css_selector('#draggable')
# target = brower.find_element_by_css_selector('#droppable')
# actions = ActionChains(brower)
# actions.drag_and_drop(source,target)
# actions.perform()
# 首先打开网页中的一个拖拽实例，然后依次选中要被拖拽的节点和拖拽到的目标节点，
# 然后声明了 ActionChains 对象赋值为 actions 变量，然后通过调用 actions 变量的 drag_and_drop() 方法，
# 然后再调用 perform() 方法执行动作，就完成了拖拽操作。
#更多动作链见官网：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains


#执行JavaScript
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

#获取节点信息
#使用 get_attribute() 方法来获取节点的属性
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))


# 每个 WebEelement 节点都有 text 属性，
# 可以通过直接调用这个属性就可以得到节点内部的文本信息了，
# 就相当于 BeautifulSoup 的 get_text() 方法、PyQuery 的 text() 方法
# from selenium import webdriver
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# inpuT = browser.find_element_by_id('zu-top-add-question')
# print(inpuT.text)


# from selenium import webdriver
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# inpuT = browser.find_element_by_id('zu-top-add-question')
# print(inpuT.id)# id 属性可以获取节点 id
# print(inpuT.location)#location 可以获取该节点在页面中的相对位置
# print(inpuT.tag_name)#tag_name 可以获取标签名称
# print(inpuT.size)#size 可以获取节点的大小，也就是宽高


# 在网页中有这样一种节点叫做 iframe，也就是子Frame，相当于页面的子页面，它的结构和外部网页的结构是完全一致的。
# Selenium 打开页面后，它默认是在父级Frame 里面操作，而此时如果页面中还有子 Frame，
# 它是不能获取到子 Frame 里面的节点的。所以这时候我们就需要使用 switch_to.frame() 方法来切换 Frame
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No LoGo')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)
#想获取子Frame 中的节点，需要先调用 switch_to.frame() 方法切换到对应的 Frame，然后再进行操作


#延时等待
#隐式等待
# 当使用了隐式等待执行测试的时候，如果 Selenium 没有在DOM 中找到节点，将继续等待，
# 超出设定时间后则抛出找不到节点的异常, 换句话说，当查找节点而节点并没有立即出现的时候，
# 隐式等待将等待一段时间再查找 DOM，默认的时间是 0
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# inpuT = browser.find_element_by_class_name('zu-top-add-question')
# print(inpuT)



#显式等待
# 隐式等待的效果其实并没有那么好，因为只是规定了一个固定时间，而页面的加载时间是受到网络条件影响的。
# 所以在这里还有一种更合适的显式等待方法，它指定好要查找的节点，
# 然后指定一个最长等待时间。如果在规定时间内加载出来了这个节点，那就返回查找的节点，
# 如果到了规定时间依然没有加载出该节点，则会抛出超时异常。
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC#等待条件
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser,10)
# inpuT = wait.until(EC.presence_of_element_located((By.ID,'mq')))#代表节点出现的意思
# button = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="sb-search"]/form[@target="_self"]/input[@type="submit"]')))#可点击
# print(inpuT,button)
# <selenium.webdriver.remote.webelement.WebElement (session="a2900efe2019d0cda71fadd5d2a816ec", element="0.5042141143454564-1")>
# <selenium.webdriver.remote.webelement.WebElement (session="a2900efe2019d0cda71fadd5d2a816ec", element="0.5042141143454564-2")>
等待条件	含义
title_is	标题是某内容
title_contains	标题包含某内容
presence_of_element_located	节点加载出，传入定位元组，如(By.ID, 'p')
visibility_of_element_located	节点可见，传入定位元组
visibility_of	可见，传入节点对象
presence_of_all_elements_located	所有节点加载出
text_to_be_present_in_element	某个节点文本包含某文字
text_to_be_present_in_element_value	某个节点值包含某文字
frame_to_be_available_and_switch_to_it frame	加载并切换
invisibility_of_element_located	节点不可见
element_to_be_clickable	节点可点击
staleness_of	判断一个节点是否仍在DOM，可判断页面是否已经刷新
element_to_be_selected	节点可选择，传节点对象
element_located_to_be_selected	节点可选择，传入定位元组
element_selection_state_to_be	传入节点对象以及状态，相等返回True，否则返回False
element_located_selection_state_to_be	传入定位元组以及状态，相等返回True，否则返回False
alert_is_present	是否出现Alert
# 更多详细的等待条件的参数及用法介绍可以参考官方文档
#http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions


#前进后退
# 使用 Selenium 也可以完成这个操作，使用 back() 方法可以后退，forward() 方法可以前进。
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()


#Cookies
# 使用 Selenium 还可以方便地对 Cookies 进行操作，例如获取、添加、删除 Cookies 等等。
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())


# 选项卡管理
# 在访问网页的时候会开启一个个选项卡，那么在 Selenium 中也可以对选项卡进行操作
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')#JavaScript 语句新开启一个选项卡
# print(browser.window_handles)#调用 window_handles 属性获取当前开启的所有选项卡，一个列表。
# #切换选项卡只需要调用 switch_to_window() 方法，传入选项卡的代号
# browser.switch_to_window(browser.window_handles[1])#切换选项卡
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])#切换选项卡
# browser.get('https://python.org')


#异常处理
#超时、节点未找到等错误，一旦出现此类错误，程序便不会继续运行了
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.find_element_by_id('hello')
#寻找不存在的节点，会抛出NoSuchElementException异常


from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print("Time out")
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
#更多异常，参考官方文档http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions'''
