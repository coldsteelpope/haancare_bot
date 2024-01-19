# ※유효기간임박상품※
# ※특가판매※

import time

from cafe24 import CreateChromeWebdriver
from cafe24 import LoginCafe24
from cafe24.removeEvents import RemoveEventsInShippedBeginListPage
from cafe24.removeEvents import RemoveEventsInShippedEndListURL
from cafe24.removeCustomers import RemoveSpecialCustomers
from cafe24.sodamSoft import RefreshSodamPage
from selenium import webdriver

from time import sleep

driver_path = "C:\p\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)

eventAmounts = [
    "★★★대박이벤트★★★",
    "배송비결제(할인적용가)/5999원",
    "※유효기간임박상품※",
    "※특가판매※",
    "※공동구매 특가판매※"
]


LoginCafe24(driver)
while True:
    RemoveSpecialCustomers(driver)
    for eventAmount in eventAmounts:
        RemoveEventsInShippedBeginListPage(driver, eventAmount)
        RemoveEventsInShippedEndListURL(driver, eventAmount)    
    RefreshSodamPage(driver)

driver.close()