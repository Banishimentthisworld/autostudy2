from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
#coding=utf-8

def study(driver):
    finish_flag = 1000
    while (finish_flag != 0):
        try:
            lsts = driver.find_elements_by_class_name("item-no")
            lsts_flag = True
        except:
            lsts_flag = False

        if lsts_flag == True:
            finish_flag = len(lsts)
            print(len(lsts))
            for lst in lsts:
                driver.implicitly_wait(10)
                lst.click()
            # 每一分钟检查观看时间时候是否达标
            while (int(driver.find_element_by_id("minStudyTime").text) > int(
                    driver.find_element_by_id("studiedTime").text)):
                time.sleep(60)

    while (int(driver.find_element_by_id("minStudyTime").text) > int(driver.find_element_by_id("studiedTime").text)):
        time.sleep(60)
# option = webdriver.ChromeOptions()
# option.add_argument('--user-data-dir=C:\\Users\\zsliujunj\\AppData\\Local\\Google\\Chrome\\User Data')
# driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Chrome()

driver.get("http://sunnyoptical.21tb.com/els/html/courseStudyItem/courseStudyItem.learn.do?courseId=4e6e51013e3f45ffabffa74d46c44fd7&courseType=NEW_COURSE_CENTER&vb_server=http%3A%2F%2F21tb-video.21tb.com")
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

driver.implicitly_wait(10)

# 点击没有看的最后一个小课程
study(driver)

# 判断课程评价按钮是否能按下
btn = driver.find_elements_by_class_name("cs-menu-link")
flag = btn[1].get_attribute("onclick")
while(flag == None):
    print(flag)
flag = btn[1].click()

# 获取打开的多个窗口句柄
windows = driver.window_handles
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])

driver.implicitly_wait(10)

# 评分
stars = driver.find_elements_by_class_name("cs-input-star")
stars[4].click()

radios = driver.find_elements_by_class_name("cs-test-radio-last")
radios[0].click()
radios[1].click()
radios[2].click()
radios[3].click()

text = driver.find_element_by_class_name("cs-question-textarea")
text.send_keys('我觉得可以，梓锴牛逼')
time.sleep(3)

#点击提交
driver.find_element_by_id("courseEvaluateSubmit").click()

time.sleep(5)
driver.quit()