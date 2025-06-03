import time

from selenium.webdriver.common import actions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.actions = ActionChains(self.driver)

    url = "https://ui.cogmento.com/"
    login_email_NAME = "email"
    login_password_NAME = "password"
    btn_XPATH = "//div[text()='Login']"
    users_icon_XPATH = "//i[@class='users icon']"
    contacts_icon_XPATh = "//span[text()='Contacts']"

    def click_url(self):
        self.driver.get(self.url)

    def enter_email(self,email):
        """

        :rtype: None
        """
        self.driver.find_element(By.NAME, self.login_email_NAME).click()
        self.driver.find_element(By.NAME, self.login_email_NAME).clear()
        self.driver.find_element(By.NAME, self.login_email_NAME).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.NAME, self.login_password_NAME).click()
        self.driver.find_element(By.NAME, self.login_password_NAME).clear()
        self.driver.find_element(By.NAME, self.login_password_NAME).send_keys(password)

    def click_btn(self):
        self.driver.find_element(By.XPATH, self.btn_XPATH).click()

    def click_users_icon(self):
        menu_icon = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.users_icon_XPATH)))
        self.actions.move_to_element(menu_icon).perform()

    def click_contacts_element(self):
        contacts_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.contacts_icon_XPATh)))
        contacts_link.click()


