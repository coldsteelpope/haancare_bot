from selenium.webdriver.common.by import By
from time import sleep

haancareURL = f'https://www.hanisamall.kr/admin'

def login(driver, haancare_id, haancare_pw):
    driver.get(haancareURL)
    alertAccept(driver)
    driver.find_element(By.XPATH, '//*[@id="mall_id"]').send_keys(haancare_id)
    driver.find_element(By.XPATH, '//*[@id="userpasswd"]').send_keys(haancare_pw)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/section/div/form/div/div[2]/button').click()
    

def alertAccept(driver):
    try:
        driver.switch_to.alert.accept()
    except:
        pass