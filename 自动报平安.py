# coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random

tem_morn = '%.1f' % random.uniform(36.0, 36.9)
tem_noon = '%.1f' % random.uniform(36.1, 37.0)
tem_afte = '%.1f' % random.uniform(36.0, 36.8)

dr = webdriver.Safari()  # open safari

print('打开网站')
url = 'http://ehall.sicnu.edu.cn/qljfw/sys/lwReportEpidemicUndergraduate/*default/index.do#/'
dr.get(url)
if dr.current_url != 'http://ehall.sicnu.edu.cn/qljfw/sys/lwReportEpidemicUndergraduate/*default/index.do#/':
    print('需要重新登录')
    dr.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/div/ins').click()
    # by name
    dr.find_element_by_name('username').send_keys('在这里输入你的学号')
    dr.find_element_by_name('password').send_keys('在这里输入你的密码', Keys.ENTER)
while True:
    try:
        time.sleep(10)
        dr.find_element_by_xpath('//*[@id="app"]/div/button').click()
        dr.find_element_by_class_name('mint-button geuhjrnk mt-btn-primary mint-button--normal').click()
        break
    except:
        pass
# while True:
#     try:
#         time.sleep(2)
#         dr.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div/div/div/div/a/div[2]').click()
#         break
#     except:
#         pass
while True:
    try:
        dr.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/a/div[2]/div[2]/input').send_keys(
            Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
        dr.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/a/div[2]/div[2]/input').send_keys(
            tem_morn)
        dr.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/a/div[2]/div[2]/input').send_keys(
            Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
        dr.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/a/div[2]/div[2]/input').send_keys(
            tem_noon)
        dr.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div/a/div[2]/div[2]/input').send_keys(
            Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
        dr.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div/a/div[2]/div[2]/input').send_keys(
            tem_afte)
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/button').click()
        break
    except:
        pass
time.sleep(2)
while True:
    try:
        # dr.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[2]').click()
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div/div/div/div/a').click()
        break
    except:
        pass

print('要关了,确认一下')
input()

dr.quit()
print('关了')
