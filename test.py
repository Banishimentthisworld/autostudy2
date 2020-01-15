import datetime
from selenium import webdriver
import datetime
import os
import sys
driver = webdriver.Chrome()
driver.get("http://sunnyoptical.21tb.com/login/login.logout.do")
while 1:
    try:
        driver.quit()
        sys.exit(1)
    except:
        print("失败")
