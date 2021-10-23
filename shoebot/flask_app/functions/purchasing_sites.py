from typing import final
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from flask import session

def amazon():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()

    url = session['link']
    email = 'application4742@gmail.com'
    password = "MyTestAccount"
    cvv = '770'

    driver.minimize_window()
    driver.maximize_window()
    driver.minimize_window()
    driver.maximize_window()

    driver.get(url)

    try:
        # logging in
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "nav-link-accountList"))).click()
        email_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "ap_email")))
        email_input.click()
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        password_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "ap_password")))
        password_input.click()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        #ordering
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "add-to-cart-button"))).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="attach-sidesheet-view-cart-button"]/span/input'))).click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "proceedToRetailCheckout"))).click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "placeYourOrder1"))).click() 
    
    # except :

    finally:
        driver.close()
    return True

def bestbuy():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()

    url = session['link']
    email = 'timmywang4742@gmail.com'
    password = "4N2:5D:TKmFnwe-"
    cvv = '770'

    driver.minimize_window()
    driver.maximize_window()
    driver.minimize_window()
    driver.maximize_window()

    driver.get(url)
    try:
    # logging in
        click_account_btn = WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.CLASS_NAME, "account-button")))
        click_account_btn.click()
        click_sign_in_btn = WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.CLASS_NAME, "sign-in-btn")))
        click_sign_in_btn.click()
        email_input = WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.NAME, "fld-e")))
        email_input.click()
        email_input.send_keys(email)
        password_input = WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.NAME, "fld-p1")))
        password_input.click()
        password_input.send_keys(password)
        WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.CLASS_NAME, "cia-form__controls__submit"))).click()

        # checking out
        WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.CLASS_NAME, "add-to-cart-button"))).click()
        WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a"))).click()
        WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button"))).click()
        cvv_input = WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.ID, "cvv")))
        cvv_input.click()
        cvv_input.send_keys(cvv)
        WebDriverWait(driver, 1500).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/div[2]/button"))).click()
    
    finally:
        driver.close()
    return True


        