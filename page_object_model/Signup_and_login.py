import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Signup_and_login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)


    subscribe_popup_XPATH = "//div[text()='Request Subscription Trial']//parent::div/button"
    inbox_field_ID = "inbox_field"
    go_btn_XPATh = "//button[@class='primary-btn']"
    company_name_NAME = "account_name"
    first_name_NAME = "first_name"
    last_name_NAME = "last_name"
    password_NAME = "password"
    password_confirmation_NAME = "password_confirm"
    submit_NAME = "action"
    login_email_NAME = "email"
    login_password_NAME = "password"
    login_btn_XPATH = "//div[text()='Login']"


    def click_popup_btn(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.subscribe_popup_XPATH))).click()

    def enter_input(self,text_name):
        self.driver.find_element(By.ID, self.inbox_field_ID).click()
        self.driver.find_element(By.ID, self.inbox_field_ID).clear()
        self.driver.find_element(By.ID, self.inbox_field_ID).send_keys(text_name)
        self.driver.find_element(By.ID, self.inbox_field_ID).send_keys(Keys.CONTROL,'a')
        self.driver.find_element(By.ID, self.inbox_field_ID).send_keys(Keys.CONTROL, 'c')

    def click_on_go_btn(self):
        self.driver.find_element(By.XPATH, self.go_btn_XPATh).click()

    def enter_company_name(self,company_name_NAME):
        self.driver.find_element(By.NAME, self.company_name_NAME).click()
        self.driver.find_element(By.NAME, self.company_name_NAME).clear()
        self.driver.find_element(By.NAME, self.company_name_NAME).send_keys(company_name_NAME)

    def enter_first_name(self,first_name_NAME):
        self.driver.find_element(By.NAME, self.first_name_NAME).click()
        self.driver.find_element(By.NAME, self.first_name_NAME).clear()
        self.driver.find_element(By.NAME, self.first_name_NAME).send_keys(first_name_NAME)

    def enter_last_name(self,last_name_NAME):
        self.driver.find_element(By.NAME, self.last_name_NAME).click()
        self.driver.find_element(By.NAME, self.last_name_NAME).clear()
        self.driver.find_element(By.NAME, self.last_name_NAME).send_keys(last_name_NAME)

    def enter_password(self,password_NAME):
        self.driver.find_element(By.NAME, self.password_NAME).click()
        self.driver.find_element(By.NAME, self.password_NAME).clear()
        self.driver.find_element(By.NAME, self.password_NAME).send_keys(password_NAME)

    def enter_password_confirm(self,password_confirmation_NAME):
        self.driver.find_element(By.NAME, self.password_confirmation_NAME).click()
        self.driver.find_element(By.NAME, self.password_confirmation_NAME).clear()
        self.driver.find_element(By.NAME, self.password_confirmation_NAME).send_keys(password_confirmation_NAME)

    def enter_submit_button(self):
        self.driver.find_element(By.NAME, self.submit_NAME).click()

    def enter_login_email(self,login_email):
        self.driver.find_element(By.NAME, self.login_email_NAME).click()
        self.driver.find_element(By.NAME, self.login_email_NAME).clear()
        self.driver.find_element(By.NAME, self.login_email_NAME).send_keys(login_email)

    def enter_login_password(self,login_password):
        self.driver.find_element(By.NAME, self.login_password_NAME).click()
        self.driver.find_element(By.NAME, self.login_password_NAME).clear()
        self.driver.find_element(By.NAME, self.login_password_NAME).send_keys(login_password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_XPATH).click()
        self.driver.quit()

