import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class DocumentsPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.actions = ActionChains(self.driver)


    create_btn_xpath = "//button[text()='Create']"
    title_xpath = "//input[@name='title']"
    access_btn_xpath = "//button[text()='Public']"
    dropdown_option_xpath = "//div[@class='twelve wide field']"
    dropdown_text_xpath = "//div[@class='selected item']/span[text()='hh ytt']"
    tags_xpath = "//div[@class='ui fluid multiple search selection dropdown']/input"
    description_xpath = "//textarea[@name='description']"
    contacts_xpath = "//div[@name='contact']/input"
    company_xpath = "//div[@name='company']/input"
    deal_xpath = "//div[@name='deal']/input"
    case_xpath = "//div[@name='case']/input"
    task_xpath = "//div[@name='task']/input"
    identifier_xpath = "//input[@name='identifier']"
    save_btn_xpath = "//button[text()='Save']"
    document_xpath = "//i[@class='file icon']"
    document_icon_xpath = "//i[@class='file icon']//parent::a/span"
    search_bar_xpath = "//input[@name='search']"
    submit_btn_xpath =  "//button[@name='submit']"
    contacts_reopen_xpath = "//span[text()='Contacts']"


    def wait_until_element_click(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.create_btn_xpath))).click()

    def enter_title(self,title):
        self.driver.find_element(By.XPATH, self.title_xpath).click()
        self.driver.find_element(By.XPATH, self.title_xpath).clear()
        self.driver.find_element(By.XPATH, self.title_xpath).send_keys(title)

    def click_access_btn_select_dropdown(self):
        self.driver.find_element(By.XPATH, self.access_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.dropdown_option_xpath ).click()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH,self.dropdown_text_xpath).is_displayed()
        self.driver.find_element(By.XPATH,self.dropdown_text_xpath ).click()
        self.driver.find_element(By.XPATH, self.dropdown_option_xpath).click()

    def enter_description(self,description):
        self.driver.find_element(By.XPATH, self.description_xpath).click()
        self.driver.find_element(By.XPATH, self.description_xpath).clear()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.description_xpath))).send_keys(description)

    def enter_contact(self,contact):
        self.driver.find_element(By.XPATH, self.contacts_xpath).click()
        self.driver.find_element(By.XPATH, self.contacts_xpath).clear()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.contacts_xpath))).send_keys(contact)

    def enter_company(self,company):
        self.driver.find_element(By.XPATH, self.company_xpath).click()
        self.driver.find_element(By.XPATH, self.company_xpath).clear()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.company_xpath))).send_keys(company)

    def enter_deal(self,deal):
        self.driver.find_element(By.XPATH, self.deal_xpath).click()
        self.driver.find_element(By.XPATH, self.deal_xpath).clear()
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.deal_xpath))).send_keys(deal)

    def enter_case(self,case):
        self.driver.find_element(By.XPATH, self.case_xpath).click()
        self.driver.find_element(By.XPATH, self.case_xpath).clear()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.case_xpath))).send_keys(case)

    def enter_task(self,task):
        self.driver.find_element(By.XPATH, self.task_xpath).click()
        self.driver.find_element(By.XPATH, self.task_xpath).clear()
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.task_xpath))).send_keys(task)
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.task_xpath).send_keys(Keys.ENTER)

    def enter_identifier(self,identifier):
        self.driver.find_element(By.XPATH, self.identifier_xpath).click()
        self.driver.find_element(By.XPATH, self.identifier_xpath).clear()
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.identifier_xpath))).send_keys(identifier)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_btn_xpath).click()
        time.sleep(2)

    def reopen_document_page(self):
        menu_icon2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.document_xpath)))
        self.actions.move_to_element(menu_icon2).perform()

    def click_document_icon(self):
        document_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.document_icon_xpath)))
        document_link.click()

    def search_document(self,doc_name):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "search"))).send_keys(doc_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@name='submit']").click()
        time.sleep(2)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH,self.submit_btn_xpath).click()

    def click_on_contact_text(self):
        contacts_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.contacts_reopen_xpath)))
        contacts_link.click()

