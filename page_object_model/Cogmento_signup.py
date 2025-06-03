from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class Cogmento_signup:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    sign_up_LINK_TEXT = "Sign Up"
    random_email_ID = "email-input"
    agree_check_XPATH = "//span[text()='I agree to the']"
    iframe_XPATH = "//iframe[contains(@title,'reCAPTCHA')]"
    captcha_XPATH = "recaptcha-checkbox-border"
    sign_in_btn_ID = "sign-in-button"

    def open_signup_page(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://ui.cogmento.com/")
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.sign_up_LINK_TEXT))).click()

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.random_email_ID).click()
        self.driver.find_element(By.ID, self.random_email_ID).clear()
        self.driver.find_element(By.ID, self.random_email_ID).send_keys(email)

    def click_agree_checkbox(self):
        self.driver.find_element(By.XPATH, self.agree_check_XPATH).click()

    def click_on_captcha(self):
        iframe = self.wait.until(EC.presence_of_element_located((By.XPATH, self.iframe_XPATH)))
        self.driver.switch_to.frame(iframe)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border"))).click()
        time.sleep(60)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "sign-in-btn").click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(),'noreply@mg.cogmento.com')]"))).click()
        iframe2 = self.wait.until(EC.presence_of_element_located((By.ID, "html_msg_body")))
        self.driver.switch_to.frame(iframe2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//td/a[text()='Click here to complete the account']"))).click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.window(self.driver.window_handles[-1])


