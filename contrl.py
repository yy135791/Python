from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import os



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.implicitly_wait(20)
driver.get('http://www.9damaogame.net/thread-228300-1-1.html')


i = 0
while i <= 85:
    search = driver.find_element_by_xpath('//*[@id="fastpostmessage"]')  # 找到输入框id
    time.sleep(15)
    saohua = None
    r = random.randint(1, 3)  # 随机回答
    if r == 1:
        saohua = "9DM不倒，陪你到老！9DM不倒，陪你到老！9DM不倒，陪你到老！"
    elif r == 2:
        saohua = '辛苦了，太棒了！\n支持支持'
    elif r == 3:
        saohua= '感谢福利,感谢佛爷\nNice！！！！'
    search.send_keys(saohua)  # 输入内容
    time.sleep(1)
    qqq = driver.find_element_by_xpath('//*[@id="fastpostsubmit"]')
    ActionChains(driver).double_click(qqq).perform()
    print('已发送{}次贴子！'.format(i+1))
    i += 1
browserName = "chrome.exe"
cmd = "taskkill /f /t /im {}".format(browserName)
os.system(cmd)
driver.quit()