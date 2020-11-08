from selenium import webdriver
import time
import urllib.request
import json
import os
import threading
import time
 
def naver_scraping():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.naver.com/')
    time.sleep(3)

    small_imgs=driver.find_elements_by_xpath('//*[@id="da_brand"]/div/a/div/img')
    counter=0
    for i in small_imgs:
        counter+=1
        s1=i.get_attribute('src')
        print(i.get_attribute('src'))
        req = urllib.request.urlretrieve(s1, "small_img_"+str(counter) + time.strftime('%m-%d-%H', time.localtime(time.time())) + ".jpg")

    driver.switch_to.frame('da_iframe_time')
    big_img = driver.find_element_by_xpath('//*[@id="ac_banner_a"]/img').get_attribute('src')
    print(big_img)
    req = urllib.request.urlretrieve(big_img, "big_img_" + time.strftime('%m-%d-%H', time.localtime(time.time())) + ".jpg")

    driver.quit()

    threading.Timer(5, naver_scraping).start()

naver_scraping()
                        
