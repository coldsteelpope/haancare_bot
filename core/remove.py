from selenium.webdriver.common.by import By

from time import sleep
from core import getPaymentListURL
from core import SHIPPED_BEGIN_LIST_PAGE_URL, SHIPPED_END_LIST_PAGE_URL

def removeSpecialCustomers(driver):
    shops = [
        "shop1",
        "shop3",
        "shop4",
        "shop5"
    ]

    for shop in shops:
        sleep(3)
        driver.get(getPaymentListURL(shop))
        
        sleep(3)
        specialCustomerOption = driver.find_element(By.XPATH, '//*[@id="QA_deposit1"]/div[2]/table/tbody/tr[7]/td[2]/div/div[2]/ul/li/ul/li[1]/label/input')
        driver.execute_script("arguments[0].click();", specialCustomerOption)
        
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search_button"]').click()
        
        sleep(3)
        theNumberOfCustomers = 0
        try:
            theNumberOfCustomers = int(driver.find_element(By.XPATH, '//*[@id="tabNumber"]/div[1]/div[1]/div/strong').text)
            if theNumberOfCustomers != 0:
                driver.find_element(By.XPATH, '//*[@id="allChk"]').click()
                
                checkBtn = driver.find_element(By.XPATH, '//*[@id="ePaymentOkBtn"]/span')
                driver.execute_script("arguments[0].click();", checkBtn)

                driver.switch_to.alert.accept()
                sleep(3)
                driver.switch_to.alert.accept()
        except:
            pass

def searchEventAmount(driver, eventAmount):
    try:
        driver.find_element(By.XPATH, '//*[@id="mainSearch"]/div/select/option[25]').click()
        driver.find_element(By.XPATH, '//*[@id="sBaseSearchBox"]').send_keys(eventAmount)
        driver.find_element(By.XPATH, '//*[@id="search_button"]').click()
    except:
        driver.find_elements(By.XPATH, '//*[@id="sBaseSearchBox"]')[1].send_keys(eventAmount)
        driver.find_element(By.XPATH, '//*[@id="search_button"]').click()


def removeEventsInShippedBeginListPage(driver, eventAmount):
    sleep(5)
    driver.get(SHIPPED_BEGIN_LIST_PAGE_URL)

    sleep(3)
    searchEventAmount(driver, eventAmount)
    
    sleep(3)
    shippedReadyListTable = driver.find_element(By.XPATH, '//*[@id="shipedReadyList"]')
    shippedListElements = shippedReadyListTable.find_elements(By.TAG_NAME, 'tr')

    sleep(3)
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
            sleep(3)
            driver.switch_to.alert.accept()
        else:
            print(f"[-] {eventAmount}원 주문건 없음")
    except:
        pass

def removeEventsInShippedEndListURL(driver, eventAmount):
    sleep(5)
    driver.get(SHIPPED_END_LIST_PAGE_URL)
    searchEventAmount(driver, eventAmount)

    sleep(3)
    theNumberOfElements = 0    
    try:
        theNumberOfElements = int(driver.find_element(By.XPATH, '//*[@id="tabNumber"]/div[1]/div[1]/div/strong').text)
        
        if theNumberOfElements != 0:
            allClickElement = driver.find_element(By.XPATH, '//*[@id="allChk"]')
            driver.execute_script("arguments[0].click();", allClickElement)

            shipEndBtn = driver.find_element(By.XPATH, '//*[@id="eShippedEndBtn"]')
            driver.execute_script("arguments[0].click();", shipEndBtn)

            driver.switch_to.alert.accept()
            sleep(3)
            driver.switch_to.alert.accept()
    except:
        pass

