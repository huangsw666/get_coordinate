# coding:utf-8
from selenium import webdriver
from time import sleep
import re

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/@0,0,11z")

u_list = [
    "立陶宛米科拉斯 罗梅里斯大学",
    "卢森堡大学",
    "美国北卡罗来纳大学",
    "美国北卡罗来纳大学教堂山分校",
    "美国北卡罗来纳大学夏洛特分校",
    "早稻田大学"
]
pattern = re.compile(r'@-?\d+\.\d+,-?\d+\.\d+')
fail_list = []
success_list = []
result = []
for university in u_list:
    try:
        driver.find_element_by_id("searchboxinput").clear()
        driver.find_element_by_id("searchboxinput").send_keys(university)
        driver.find_element_by_id("searchbox-searchbutton").click()
    except:
        try:
            sleep(10)
            driver.find_element_by_id("searchboxinput").clear()
            driver.find_element_by_id("searchboxinput").send_keys(university)
            driver.find_element_by_id("searchbox-searchbutton").click()
        except:
            continue
    else:
        print("")
    # driver.implicitly_wait(30)
    i = 0
    while i < 30:
        i = i + 1
        sleep(0.5)
        page_url = driver.current_url
        # print(page_url)
        result0 = pattern.findall(page_url)
        if len(result0) == 1:
            if result0 != result:
                break
    # sleep(15)
    # page_url1 = driver.current_url
    # sleep(10)
    # page_url2 = driver.current_url
    # currentPageUrl = page_url2
    #
    # if page_url1 == page_url2:
    #     print("加载完了1")
    # else:
    #     sleep(15)
    #     page_url3 = driver.current_url
    #     currentPageUrl = page_url3
    #     if page_url2 == page_url3:
    #         print("加载完了2")
    #     else:
    #         sleep(10)
    #         print("加载完了3")
    #         currentPageUrl = driver.current_url

    # print(university)
    try:
        result = result0
        each = [university, result]
        print(each)
        if len(result) == 0:
            fail_list.append(each)
        else:
            success_list.append(each)
    except UnicodeEncodeError:
        continue

print("fail list:")
for fail in fail_list:
    print(fail)
    with open("fail list.txt", "a", encoding='utf-8') as output:
        output.write(str(fail))

print("success list:")
for success in success_list:
    print(success)
    with open("success list.txt", "a", encoding='utf-8') as output:
        output.write(str(success))
