from cafe24 import SODAM_SOFT_URL

from time import sleep
from random import randrange

def RefreshSodamPage(driver):
    sleep(randrange(3, 5))
    driver.get(SODAM_SOFT_URL)
    sleep(randrange(3, 5))
    driver.refresh()
    sleep(randrange(3, 5))