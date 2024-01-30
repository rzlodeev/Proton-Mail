# from pyvirtualdisplay import Display
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import pyautogui

from dotenv import load_dotenv
from time import sleep
import os

load_dotenv()


# noinspection PyDeprecation
def send_proton_email(email_to, email_subject, email_message):
    driver = ''
    display = ''
    try:
        # display = Display(visible=0, size=(1920, 1080))   # Used to create a virtual display to be able to run selenium in a terminal without GUI
        # display.start()

        # Open page
        driver = webdriver.Firefox()
        driver.get('https://mail.protonmail.com/login')
        sleep(5)

        # Enter login and password
        account_username = os.getenv('ACCOUNT_USERNAME')
        driver.find_element(By.ID, 'username').send_keys(account_username)
        account_password = os.getenv('ACCOUNT_PASSWORD')
        driver.find_element(By.ID, 'password').send_keys(account_password)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/form/button').click()
        sleep(10)

        # Clicking on "New mail" button
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/button').click()
        except NoSuchElementException:
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div/header/button[2]').click()
        sleep(2)

        # Typing message
        driver.switch_to.active_element.send_keys(email_to)
        pyautogui.typewrite('\n\t')
        driver.switch_to.active_element.send_keys(email_subject)
        pyautogui.typewrite('\t\t')
        driver.switch_to.active_element.send_keys(email_message)
        sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/div/footer/div/div[1]/button[1]').click()
        sleep(5)

        driver.quit()
        # display.stop()
        print('E-mail Sent!')
        del email_subject
        del email_message
        del driver
        del display
    except Exception as err:
        driver.quit()
        # display.stop()
        print('\nError Occurred while sending e-mail!!')
        status = (str(err), f'{traceback.format_exc()}', 'Error Origin: Proton Mail Script')
        print(status)
        del err
        del status
        del driver
        # del display


send_proton_email('ex@ex.com', 'test', 'testmsg')
# TEST
