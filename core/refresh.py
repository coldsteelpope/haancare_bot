from core import SODAM_SOFT_URL

from time import sleep

def refreshSodamPage(driver):
    sleep(3)
    driver.get(SODAM_SOFT_URL)
    sleep(3)
    driver.refresh()
    sleep(3)