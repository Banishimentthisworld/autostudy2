from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time
driver = webdriver.Chrome()
driver.get("http://sunnyoptical.21tb.com/login/login.logout.do")
# driver.maximize_window()
driver.find_element_by_xpath("//input[@id='loginName']").send_keys('1157831')
driver.find_element_by_xpath("//input[@id='password']").send_keys('1157831')
driver.implicitly_wait(20)
driver.find_element_by_xpath("//input[@class='btn']").click()

try:
    driver.find_element_by_xpath("//input[@class='btn-primary']")
    a = True
except:
    a = False

if a == True:
    driver.find_element_by_xpath("//input[@class='btn-primary']").click()

time.sleep(2)
driver.implicitly_wait(10)
driver.find_element_by_xpath("/html/body/div[@class='tbc-desktop']/div[@class='tbc-desktop-slide tbc-tabset']/div[@class='tbc-slide-scene current']/div[@class='tbc-shortcut tbc-folder-shortcut'][1]/div[@class='tbc-shortcut-inner']/span[@class='tbc-shortcut-label']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[@class='tbc-desktop']/div[@class='tbc-desktop-slide tbc-tabset']/div[@class='tbc-slide-scene current']/div[@class='tbc-pop  tbc-pop-folder']/div[@class='tbc-pop-inner']/div[@class='tbc-pop-container']/div[@class='tbc-shortcut'][1]/div[@class='tbc-shortcut-inner']/span[@class='tbc-shortcut-label']").click()
time.sleep(5)

# try:
#     driver.find_element_by_xpath("/html/body/div[@class='tbc-desktop']/div[@class='tbc-desktop-slide tbc-tabset']/div[@class='tbc-slide-scene current']/div[@class='tbc-shortcut tbc-folder-shortcut'][1]/div[@class='tbc-shortcut-inner']/span[@class='tbc-shortcut-label']")
#     a = True
# except:
#     a = False
#
# if a == True:
#     driver.find_element_by_xpath("/html/body/div[@class='tbc-desktop']/div[@class='tbc-desktop-slide tbc-tabset']/div[@class='tbc-slide-scene current']/div[@class='tbc-shortcut tbc-folder-shortcut'][1]/div[@class='tbc-shortcut-inner']/span[@class='tbc-shortcut-label']").click()
#
# try:
#     driver.find_element_by_xpath(
#         "/html/body/div[@class='tbc-desktop']/div[@class='tbc-desktop-slide tbc-tabset']/div[@class='tbc-slide-scene current']/div[@class='tbc-pop  tbc-pop-folder']/div[@class='tbc-pop-inner']/div[@class='tbc-pop-container']/div[@class='tbc-shortcut'][1]/div[@class='tbc-shortcut-inner']/span[@class='tbc-shortcut-label']")
#     a = True
# except:
#     a = False
#
# if a == True:
#     driver.find_element_by_xpath(
#         "/html/body/div[@class='tbc-desktop']/div[@class='tbc-desktop-slide tbc-tabset']/div[@class='tbc-slide-scene current']/div[@class='tbc-pop  tbc-pop-folder']/div[@class='tbc-pop-inner']/div[@class='tbc-pop-container']/div[@class='tbc-shortcut'][1]/div[@class='tbc-shortcut-inner']/span[@class='tbc-shortcut-label']").click()

# 获取打开的多个窗口句柄
windows = driver.window_handles
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])

# 点击全部课程
try:
    driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/header[@class='nc-header cl-container redesign-course-center']/div[@class='nc-header-inner']/nav[@class='nc-nav cl-container redesign-course-nav']/div[@class='nc-nav-container']/div[@class='nc-menu-container']/div[@id='ncMenuHead']/a[@class='nc-menu-head-link']")
    b = True
except:
    b = False

if b == True:
    driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/header[@class='nc-header cl-container redesign-course-center']/div[@class='nc-header-inner']/nav[@class='nc-nav cl-container redesign-course-nav']/div[@class='nc-nav-container']/div[@class='nc-menu-container']/div[@id='ncMenuHead']/a[@class='nc-menu-head-link']").click()

time.sleep(3)
# 点击空白
driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/header[@class='nc-header cl-container redesign-course-center']/div[@class='nc-header-inner']/span[@class='nc-brand']").click()

time.sleep(3)
# 点击未选课程
driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/section[@id='courseCenterBody']/div[@class='cl-container']/form[@id='searchFilterForm']/div[1]/dl[@class='nc-filter-option'][1]/dd[@class='option-item'][1]").click()

time.sleep(3)
# 点击课程评估
driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/section[@id='courseCenterBody']/div[@class='cl-container']/form[@id='searchFilterForm']/div[1]/dl[@class='nc-filter-option'][2]/dd[@class='option-item'][2]").click()

time.sleep(3)
# 点击第一个课程
driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/section[@id='courseCenterBody']/article[@class='cl-container nc-lectuer']/div[@id='searchCourseBody']/ul[@class='nc-course-list']/li[@class='nc-course-card   '][1]/a/div[@class='card-body']/h3[@class='card-title']").click()

# 获取打开的多个窗口句柄
windows = driver.window_handles
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])

time.sleep(3)
# 点击选择课程
driver.find_element_by_xpath("/html/body/div[@class='cl-discuss-bg']/article[@class='cd-details cl-container']/figure[@class='cd-details-content']/div[@class='cd-details-body']/div[4]/div[@class='cd-details-left']/span[@id='chooseCourse']").click()

time.sleep(3)
# 点击确定
driver.find_element_by_xpath("/html/body/div[@id='layui-layer1']/div[@class='layui-layer-btn']/a[@class='layui-layer-btn0']").click()

# 获取打开的多个窗口句柄
windows = driver.window_handles
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])

time.sleep(3)
# 点击进入学习
driver.find_element_by_xpath("/html/body/div[@class='cl-discuss-bg']/article[@class='cd-details cl-container']/figure[@class='cd-details-content']/div[@class='cd-details-body']/div[4]/div[@class='cd-details-left']/a[@id='goStudy']").click()

