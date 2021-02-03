from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')

driver.get('https://mwpt.mma.go.kr/caisBMHS/index_mwps.jsp?menuNo=22039')
driver.switch_to.frame('main')

def selectOptions(driver, elementsId, optionValue):
    option=driver.find_element_by_xpath('//*[@id="{}"]/option[@value="{}"]'.format(elementsId, optionValue))
    option.click()
    time.sleep(3)
    return

selectOptions(driver,'gun_gbcd', 1)
selectOptions(driver,'mojip_gbcd', 5)
selectOptions(driver,'iyyjsijak_yy', 2021)
selectOptions(driver,'iyyjsijak_mm', '06')
selectOptions(driver,'mojip_ij',4)

submit=driver.find_element_by_xpath('//*[@id="contents"]/div/form/div/p/span')
submit.click()
time.sleep(3)
result=driver.find_element_by_xpath('//*[@id="resultTbl"]/tbody/tr/td[4]').text
print(result)