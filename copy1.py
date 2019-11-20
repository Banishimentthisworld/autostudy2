
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
username = input("username:")
password = input("password:")

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

while(1):
    try:
        import time
        driver = webdriver.Chrome()
        driver.get("http://sunnyoptical.21tb.com/login/login.logout.do")
        time.sleep(3)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element_by_xpath("//input[@id='loginName']").send_keys(username)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.implicitly_wait(10)
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
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div[@class='tbc-desktop']/div[@class='tbc-desktop-slide tbc-tabset']/div[@class='tbc-slide-scene current']/div[@class='tbc-pop  tbc-pop-folder']/div[@class='tbc-pop-inner']/div[@class='tbc-pop-container']/div[@class='tbc-shortcut'][1]/div[@class='tbc-shortcut-inner']/span[@class='tbc-shortcut-label']").click()
        time.sleep(5)
        driver.implicitly_wait(10)


        windows = driver.window_handles
        # 切换到当前最新打开的窗口
        driver.switch_to.window(windows[-1])
        driver.implicitly_wait(20)
        # 点击全部课程
        try:
            driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/header[@class='nc-header cl-container redesign-course-center']/div[@class='nc-header-inner']/nav[@class='nc-nav cl-container redesign-course-nav']/div[@class='nc-nav-container']/div[@class='nc-menu-container']/div[@id='ncMenuHead']/a[@class='nc-menu-head-link']")
            b = True
        except:
            b = False

        if b == True:
            driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/header[@class='nc-header cl-container redesign-course-center']/div[@class='nc-header-inner']/nav[@class='nc-nav cl-container redesign-course-nav']/div[@class='nc-nav-container']/div[@class='nc-menu-container']/div[@id='ncMenuHead']/a[@class='nc-menu-head-link']").click()

        time.sleep(3)
        driver.implicitly_wait(10)
        # 点击空白
        driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/header[@class='nc-header cl-container redesign-course-center']/div[@class='nc-header-inner']/span[@class='nc-brand']").click()

        time.sleep(3)
        driver.implicitly_wait(10)
        # 点击未选课程
        driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/section[@id='courseCenterBody']/div[@class='cl-container']/form[@id='searchFilterForm']/div[1]/dl[@class='nc-filter-option'][1]/dd[@class='option-item'][1]").click()

        time.sleep(3)
        driver.implicitly_wait(10)
        # 点击课程评估
        driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/section[@id='courseCenterBody']/div[@class='cl-container']/form[@id='searchFilterForm']/div[1]/dl[@class='nc-filter-option'][2]/dd[@class='option-item'][2]").click()

        time.sleep(3)
        driver.implicitly_wait(10)
        nc = driver.find_elements_by_class_name("nc-rank-link")
        # print(len(nc))
        nc[1].click()

        time.sleep(3)
        driver.implicitly_wait(10)
        # 点击第一个课程
        driver.find_element_by_xpath("/html/body[@class='redesign-course-center-body']/section[@id='courseCenterBody']/article[@class='cl-container nc-lectuer']/div[@id='searchCourseBody']/ul[@class='nc-course-list']/li[@class='nc-course-card   '][1]/a/div[@class='card-body']/h3[@class='card-title']").click()

        # 获取打开的多个窗口句柄
        windows = driver.window_handles
        # 切换到当前最新打开的窗口
        driver.switch_to.window(windows[-1])

        time.sleep(3)
        driver.implicitly_wait(10)
        # 点击选择课程
        driver.find_element_by_xpath("/html/body/div[@class='cl-discuss-bg']/article[@class='cd-details cl-container']/figure[@class='cd-details-content']/div[@class='cd-details-body']/div[4]/div[@class='cd-details-left']/span[@id='chooseCourse']").click()

        time.sleep(3)
        driver.implicitly_wait(10)
        # 点击确定
        driver.find_element_by_xpath("/html/body/div[@id='layui-layer1']/div[@class='layui-layer-btn']/a[@class='layui-layer-btn0']").click()

        # 获取打开的多个窗口句柄
        windows = driver.window_handles
        # 切换到当前最新打开的窗口
        driver.switch_to.window(windows[-1])

        time.sleep(3)
        driver.implicitly_wait(10)
        # 点击进入学习
        driver.find_element_by_xpath("/html/body/div[@class='cl-discuss-bg']/article[@class='cd-details cl-container']/figure[@class='cd-details-content']/div[@class='cd-details-body']/div[4]/div[@class='cd-details-left']/a[@id='goStudy']").click()

        time.sleep(5)
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_xpath("//input[@class='btn-primary']")
            a = True
        except:
            a = False

        if a == True:
            a = False
            driver.find_element_by_xpath("//input[@class='btn-primary']").click()

        time.sleep(3)
        driver.implicitly_wait(10)

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
            driver.refresh()
            study(driver)
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
        text.send_keys('无')
        time.sleep(3)
        driver.implicitly_wait(10)

        #点击提交
        driver.find_element_by_id("courseEvaluateSubmit").click()
        time.sleep(5)
        driver.implicitly_wait(10)
        driver.find_element_by_class_name("layui-layer-btn1").click()
        time.sleep(5)
        driver.implicitly_wait(10)
        driver.quit()
    except:
        print("失败")
        driver.quit()