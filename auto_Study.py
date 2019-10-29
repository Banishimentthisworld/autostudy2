# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time

def study(driver):
    finish_flag = 1000
    while finish_flag != 0:
        driver.refresh()
        time.sleep(5)
        driver.implicitly_wait(10)
        print("·····················梓锴牛逼·····················")
        # 获取课程名称
        courseTitle = driver.find_element_by_id("courseTitle")
        print("课程标题：", courseTitle.get_attribute("title"))
        # 获取课程章节总数
        courses = driver.find_elements_by_class_name("cl-catalog-item")
        print("课程章节：", len(courses))
        # 获取以学习章节数量
        courses_Learned = driver.find_elements_by_class_name("cl-catalog-link-done")
        print("已学习章节：", len(courses_Learned))
        # 获取未学习章节数量
        courses_Learn = driver.find_elements_by_class_name("item-no")
        print("未学习章节：", len(courses_Learn))

        # 点击第一个未学习的课程
        if len(courses_Learn) != 0:
            courses_Learn[0].click()
            time.sleep(5)
            # 正在学习的章节
            courser_learning = driver.find_element_by_class_name("cl-catalog-playing")
            print("正在学习的章节：", courser_learning.get_attribute("title"))
            # 每15秒检查观看时间时候是否达标
            while int(driver.find_element_by_id("minStudyTime").text) > int(driver.find_element_by_id("studiedTime").text):
                study_time = driver.find_element_by_id("minStudyTime").text
                studied_time = driver.find_element_by_id("studiedTime").text
                print("\r" + "需学习时间：" + study_time + "  已学习时间：" + studied_time, end="")
                time.sleep(15)

        else:
            # 完成学习
            finish_flag = 0

        print("\n·····················梓锴牛逼·····················")
    print("所有课程已经完成学习")

driver = webdriver.Chrome()
driver.get("http://sunnyoptical.21tb.com/els/html/courseStudyItem/courseStudyItem.learn.do?courseId=a44e3363d513e2756da0a330650c068c&courseType=NEW_COURSE_CENTER&vb_server=http%3A%2F%2F21tb-video.21tb.com")
time.sleep(3)
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='loginName']").send_keys('1157830')
driver.find_element_by_xpath("//input[@id='password']").send_keys('1157830')
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@class='btn']").click()

try:
    driver.find_element_by_xpath("//input[@class='btn-primary']")
    a = True
except:
    a = False

if a == True:
    driver.find_element_by_xpath("//input[@class='btn-primary']").click()


# 点击没有看的课程
study(driver)

# 判断课程评价按钮是否能按下
btn = driver.find_elements_by_class_name("cs-menu-link")
flag = btn[1].get_attribute("onclick")
while (flag == None):
    print(flag)
flag = btn[1].click()

# 获取打开的多个窗口句柄
windows = driver.window_handles
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])
time.sleep(3)
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
driver.implicitly_wait(10)

# 点击提交
driver.find_element_by_id("courseEvaluateSubmit").click()
time.sleep(5)
driver.implicitly_wait(10)
driver.find_element_by_class_name("layui-layer-btn1").click()
time.sleep(5)
driver.implicitly_wait(10)
driver.quit()