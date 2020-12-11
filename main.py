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

    small_imgs=driver.find_elements_by_xpath('//*[@id="da_brand"]//img')
    counter=0
    for i in small_imgs:
        counter+=1
        s1=i.get_attribute('src')
        print(i.get_attribute('src'))
        req = urllib.request.urlretrieve(s1, "small_img_"+str(counter) +'_'+ time.strftime('%m-%d-%I%p-%M-%S', time.localtime(time.time())) + ".jpg")

    
    big_imgs = driver.find_elements_by_xpath('//*[@id="da_top"]//img')
    print(big_imgs)
    if(len(big_imgs)==0):
        driver.switch_to.frame('da_iframe_time')
        big_imgs = driver.find_elements_by_xpath('//*[@id="da_timeboard"]//img')
    print(big_imgs)
    counter=0
    for i in big_imgs:
        counter+=1
        s1=i.get_attribute('src')
        print(i.get_attribute('src'))
        req = urllib.request.urlretrieve(s1, "big_img_"+str(counter) +'_'+ time.strftime('%m-%d-%I%p-%M-%S', time.localtime(time.time())) + ".jpg")

    driver.quit()

    threading.Timer(10, naver_scraping).start()

def mobile_naver_scraping():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://m.naver.com/')
    time.sleep(3)
    
    mobile_small_img=driver.find_elements_by_xpath('//*[@id="main_search_specialda_1"]//img')
    print(mobile_small_img)
    seq=0
    for i in mobile_small_img:
        seq=seq+1
        mobile_small_img_link=i.get_attribute('src')
        print(mobile_small_img_link)
        req = urllib.request.urlretrieve(mobile_small_img_link, time.strftime('%Y-%m-%d_naverM_%H시_', time.localtime(time.time()))+str(seq)+ ".jpg")
    
    driver.quit()

    threading.Timer(10, mobile_naver_scraping).start()

def youtube_scraping():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.youtube.com/')
    time.sleep(3)
    
    ad_link=driver.find_element_by_xpath('//*[@id="click-target"]').get_attribute('href')
    print(ad_link)
    
    driver.get(ad_link)
    time.sleep(3)
    ad_subject=driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
    print(ad_subject)
    f=open("youtube_ad_list.txt",'a', encoding='utf8')
    f.writelines(time.strftime('%Y-%m-%d_youtube_%H시', time.localtime(time.time()))+' '+ad_subject+' LINK : '+ad_link+'\n')
    f.close()
    driver.quit()

    threading.Timer(10, youtube_scraping).start()

mobile_naver_scraping()
                        
