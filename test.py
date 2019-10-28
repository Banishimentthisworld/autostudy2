from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
#coding=utf-8
# option = webdriver.ChromeOptions()
# option.add_argument('--user-data-dir=C:\\Users\\zsliujunj\\AppData\\Local\\Google\\Chrome\\User Data')
# driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Chrome()

driver.get("http://sunnyoptical.21tb.com/els/html/courseStudyItem/courseStudyItem.learn.do?courseId=aecab7bfb4744105a926fa2d63e7864a&courseType=NEW_COURSE_CENTER&vb_server=http%3A%2F%2F21tb-video.21tb.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_xpath("//input[@id='loginName']").send_keys('1157831')
driver.find_element_by_xpath("//input[@id='password']").send_keys('1157831')
driver.find_element_by_xpath("//input[@class='btn']").click()
driver.implicitly_wait(20)
try:
    driver.find_element_by_xpath("//input[@class='btn-primary']")
    a = True
except:
    a = False

if a == True:
    a = False
    driver.find_element_by_xpath("//input[@class='btn-primary']").click()
# 获取打开的多个窗口句柄
windows = driver.window_handles
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])

driver.implicitly_wait(20)
try:
    driver.find_element_by_class_name("cs-item-evaluate").click()
except:
    print("faile")
# 点击没有看的最后一个小课程
finish_flag = 0
while(finish_flag == 0):
    try:
        lsts = driver.find_elements_by_class_name("item-no")
        lsts_flag = True
    except:
        lsts_flag = False
        finish_flag == 1

    if lsts_flag == True:
        print(len(lsts))
        for lst in lsts:
            driver.implicitly_wait(20)
            lst.click()
        # 每一分钟检查观看时间时候是否达标
        while(int(driver.find_element_by_id("minStudyTime").text) > int(driver.find_element_by_id("studiedTime").text)):
            time.sleep(60)


print(driver.find_element_by_id("minStudyTime").text)