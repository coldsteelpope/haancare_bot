from selenium.webdriver.common.by import By
from cafe24 import LoginCafe24, shippedBeginListPageURL, shippedEndListPageURL, shippedCompleteListOrdNumURL

import random
import time

def SearchEventAmount(driver, eventAmount):
    try:
        driver.find_element(By.XPATH, '//*[@id="mainSearch"]/div/select/option[25]').click()
        driver.find_element(By.XPATH, '//*[@id="sBaseSearchBox"]').send_keys(eventAmount)
        driver.find_element(By.XPATH, '//*[@id="search_button"]').click()
    except:
        driver.find_elements(By.XPATH, '//*[@id="sBaseSearchBox"]')[1].send_keys(eventAmount)
        driver.find_element(By.XPATH, '//*[@id="search_button"]').click()



def RemoveEventsInShippedBeginListPage(driver, eventAmount):
    time.sleep(random.randrange(5, 7))

    driver.get(shippedBeginListPageURL)
    time.sleep(random.randrange(5, 7))

    SearchEventAmount(driver, eventAmount)
    time.sleep(random.randrange(5, 7))
    
    shippedReadyListTable = driver.find_element(By.XPATH, '//*[@id="shipedReadyList"]')
    shippedListElements = shippedReadyListTable.find_elements(By.TAG_NAME, 'tr')

    theNumberOfElements = 0
    
    try:
        theNumberOfElements = int(driver.find_element(By.XPATH, '//*[@id="QA_prepareNumber2"]/div[2]/div[1]/div/strong').text)
        if theNumberOfElements != 0:
            index = -1

            for shippedListElement in shippedListElements:
                optionsInShippedListElement = shippedListElement.find_elements(By.TAG_NAME, 'option')
                inputInShippedListElement = shippedListElement.find_element(By.XPATH, f'//*[@id="invoice_no_{int(index/2)}"]')
                
                if len(optionsInShippedListElement) != 0:
                    optionsInShippedListElement[1].click()

                inputInShippedListElement.click()
                if inputInShippedListElement.text != '.':
                    inputInShippedListElement.send_keys('.')

                index += 1

            allClickElement = driver.find_element(By.XPATH, '//*[@id="allChk"]')
            driver.execute_script("arguments[0].click();", allClickElement)

            shipStartBtn = driver.find_element(By.XPATH, '//*[@id="eShipStartBtn"]')
            driver.execute_script("arguments[0].click();", shipStartBtn)

            driver.switch_to.alert.accept()
            time.sleep(random.randrange(3, 5))
            driver.switch_to.alert.accept()
        else:
            print(f"[-] {eventAmount}원 주문건 없음")
    except:
        pass


def RemoveEventsInShippedEndListURL(driver, eventAmount):
    time.sleep(random.randrange(5, 7))
    driver.get(shippedEndListPageURL)
    SearchEventAmount(driver, eventAmount)

    time.sleep(random.randrange(5, 7))

    try:
        theNumberOfElements = 0
        theNumberOfElements = int(driver.find_element(By.XPATH, '//*[@id="tabNumber"]/div[1]/div[1]/div/strong').text)
        
        if theNumberOfElements != 0:
            allClickElement = driver.find_element(By.XPATH, '//*[@id="allChk"]')
            driver.execute_script("arguments[0].click();", allClickElement)

            shipEndBtn = driver.find_element(By.XPATH, '//*[@id="eShippedEndBtn"]')
            driver.execute_script("arguments[0].click();", shipEndBtn)

            driver.switch_to.alert.accept()
            time.sleep(random.randrange(3, 5))
            driver.switch_to.alert.accept()
    except:
        pass
