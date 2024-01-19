from selenium.webdriver.common.by import By

import time
import random

def GetPaymentListURL(shop):
    return f"https://haancare1.cafe24.com/admin/php/{shop}/s/payment_list.php"

def RemoveSpecialCustomers(driver):
    shops = [
        "shop1",
        "shop3",
        "shop4",
        "shop5"
    ]

    for shop in shops:
        time.sleep(random.randrange(3, 4))
        driver.get(GetPaymentListURL(shop))

        time.sleep(random.randrange(3, 4))
        specialCustomerOption = driver.find_element(By.XPATH, '//*[@id="QA_deposit1"]/div[2]/table/tbody/tr[7]/td[2]/div/div[2]/ul/li/ul/li[1]/label/input')
        driver.execute_script("arguments[0].click();", specialCustomerOption)
        
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="search_button"]').click()
        time.sleep(random.randrange(3, 4))

        theNumberOfCustomers = 0
        try:
            theNumberOfCustomers = int(driver.find_element(By.XPATH, '//*[@id="tabNumber"]/div[1]/div[1]/div/strong').text)
            if theNumberOfCustomers != 0:
                driver.find_element(By.XPATH, '//*[@id="allChk"]').click()
                
                checkBtn = driver.find_element(By.XPATH, '//*[@id="ePaymentOkBtn"]/span')
                driver.execute_script("arguments[0].click();", checkBtn)

                driver.switch_to.alert.accept()
                time.sleep(random.randrange(3, 4))
                driver.switch_to.alert.accept()
        except:
            pass
    driver.get(GetPaymentListURL(shops[0]))