import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ContactsPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.actions = ActionChains(self.driver)

    create_btn_in_contacts_XPATH = "//button[text()='Create']"
    first_name_NAME = "first_name"
    last_name_NAME = "last_name"
    middle_name_NAME = "middle_name"
    company_name_XPATH = "//div/label[text()='Company']/following::input[1]"
    tag_XPATH = "//div/label[text()='Tags']//following::input[1]"
    access_btn_XPATH = "//button[text()='Public']"
    lock_btn_XPATH = "//div[@class='twelve wide field']"
    text_XPATH = "//div[@class='selected item']/span[text()='hh ytt']"
    email_XPATH = "//div/label[text()='Email']//following::input[1]"
    category_XPATH = "//label[text()='Category']//parent::div/div"
    contact_XPATH = "//label[text()='Category']//parent::div/div/div/div/span[text()='Contact']"
    status_XPATH = "//label[text()='Status']//parent::div/div"
    on_hold_XPATH = "//span[text()='On Hold']"
    textarea_XPATH = "//div[@class='ui field']/textarea"
    social_channels_XPATH = "//label[text()='Social channels']//parent::div/div/div/div/div[@class='ui selection dropdown']"
    social_options_XPATH = "//div[@class='visible menu transition']/div[3]"
    social_channel_text = "//*[@id='main-content']/div/div[2]/form/div[6]/div[1]/div/div/div/div[2]/div/input"
    address_XPATH = "//input[@name='address']"
    city_XPATH = "//input[@name='city']"
    state_XPATh = "//input[@name='state']"
    zip_XPATH = "//input[@name='zip']"
    country_XPATH = "//div[@name='country']"
    countries_option_XPATH = "//i[@class='in flag']//parent::div/span[text()='India']"
    mobile_XPATH = "//input[@placeholder='Number']"
    radom_text_XPATH = "//input[@placeholder='Home, Work, Mobile...']"
    position_XPATH = "//label[text()='Position']//parent::div/div/input[1]"
    department_XPATH = "//label[text()='Department']//parent::div/div/input[1]"
    supervisor_XPATh = "//label[text()='Department']//parent::div/div/input[1]"
    assistant_XPATh = "//label[text()='Assistant']//parent::div/div/input[1]"
    referral_XPATh = "//label[text()='Referred By']//parent::div/div/input[1]"
    source_xpath = "//label[text()='Source']//parent::div/div"
    source_options = "//span[text()='Google']"
    Call_toggle_btn_XPATH = "//label[text()='Do not Call']//parent::div/div"
    Text_toggle_btn_XPATH = "//label[text()='Do not Text']//parent::div/div"
    Email_toggle_btn_XPATH = "//label[text()='Do not Email']//parent::div/div"
    DOB_date_XPATH = "//input[@name='day']"
    DOB_month_XPATH = "//div[@name='month']"
    DOB_month_click_XPATH = "//div[@class='visible menu transition']/div[11]"
    DOB_year_XPATH = "//input[@name='year']"
    identifier_XPATH = "//input[@name='identifier']"
    save_btn_XPATh = "//button[text()='Save']"
    menu_icon2_XPATH = "//i[@class='file icon']"
    documents_link_XPATH = "//span[text()='Documents']"
    search_bar_in_contacts_page_xpath = "//input[@placeholder='Search']"


    def click_create_btn_in_contacts_page(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.create_btn_in_contacts_XPATH))).click()

    def enter_the_firstname(self,firstname):
        self.wait.until(EC.presence_of_element_located((By.NAME, self.first_name_NAME))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME, self.first_name_NAME))).clear()
        self.driver.find_element(By.NAME, self.first_name_NAME).send_keys(firstname)

    def enter_the_lastname(self,lastname):
        self.driver.find_element(By.NAME, self.last_name_NAME).click()
        self.driver.find_element(By.NAME, self.last_name_NAME).clear()
        self.driver.find_element(By.NAME, self.last_name_NAME).send_keys(lastname)

    def enter_the_middle_name(self,middle_name):
        self.driver.find_element(By.NAME, self.middle_name_NAME).click()
        self.driver.find_element(By.NAME, self.middle_name_NAME).clear()
        self.driver.find_element(By.NAME, self.middle_name_NAME).send_keys(middle_name)

    def enter_company_name(self,company_name):
        self.driver.find_element(By.XPATH, self.company_name_XPATH).click()
        self.driver.find_element(By.XPATH, self.company_name_XPATH).clear()
        self.driver.find_element(By.XPATH, self.company_name_XPATH).send_keys(company_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.company_name_XPATH).send_keys(Keys.ENTER)

    def enter_tag(self,tag):
        self.driver.find_element(By.XPATH, self.tag_XPATH).click()
        self.driver.find_element(By.XPATH, self.tag_XPATH).clear()
        self.driver.find_element(By.XPATH, self.tag_XPATH).send_keys(tag)
        self.driver.find_element(By.XPATH, self.tag_XPATH).send_keys(Keys.ENTER)

    def click_access_btn(self):
        self.driver.find_element(By.XPATH, self.access_btn_XPATH).click()
        self.driver.find_element(By.XPATH,self.lock_btn_XPATH).click()
        assert self.driver.find_element(By.XPATH, self.text_XPATH).is_displayed()
        self.driver.find_element(By.XPATH, self.text_XPATH).click()
        self.driver.find_element(By.XPATH, self.lock_btn_XPATH).click()

    def enter_the_email(self,Email):
        self.driver.find_element(By.XPATH, self.email_XPATH).click()
        self.driver.find_element(By.XPATH, self.email_XPATH).clear()
        self.driver.find_element(By.XPATH, self.email_XPATH).send_keys(Email)

    def enter_Category(self):
        self.driver.find_element(By.XPATH, self.category_XPATH).click()
        self.driver.find_element(By.XPATH, self.contact_XPATH).click()

    def enter_status(self):
        self.driver.find_element(By.XPATH, self.status_XPATH).click()
        self.driver.find_element(By.XPATH, self.on_hold_XPATH).click()

    def enter_into_textarea(self,textarea):
        self.driver.find_element(By.XPATH, self.textarea_XPATH).click()
        self.driver.find_element(By.XPATH, self.textarea_XPATH).clear()
        self.driver.find_element(By.XPATH, self.textarea_XPATH).send_keys(textarea)

    def enter_into_social_channels(self):
        self.driver.find_element(By.XPATH, self.social_channels_XPATH).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.social_options_XPATH))).click()
        self.driver.find_element(By.XPATH, self.social_channel_text).click()

    def enter_address(self,address):
        self.driver.find_element(By.XPATH, self.address_XPATH).click()
        self.driver.find_element(By.XPATH, self.address_XPATH).clear()
        self.driver.find_element(By.XPATH, self.address_XPATH).send_keys(address)

    def enter_city(self,city):
        self.driver.find_element(By.XPATH, self.city_XPATH).click()
        self.driver.find_element(By.XPATH, self.city_XPATH).clear()
        self.driver.find_element(By.XPATH, self.city_XPATH).send_keys(city)

    def enter_state(self,state):
        self.driver.find_element(By.XPATH, self.state_XPATh).click()
        self.driver.find_element(By.XPATH, self.state_XPATh).clear()
        self.driver.find_element(By.XPATH, self.state_XPATh).send_keys(state)

    def enter_zip(self,zip):
        self.driver.find_element(By.XPATH, self.zip_XPATH).click()
        self.driver.find_element(By.XPATH, self.zip_XPATH).clear()
        self.driver.find_element(By.XPATH, self.zip_XPATH).send_keys(zip)

    def enter_country(self):
        self.driver.find_element(By.XPATH, self.country_XPATH).click()
        self.driver.find_element(By.XPATH, self.countries_option_XPATH).click()

    def enter_mobile(self,number):
        self.driver.find_element(By.XPATH, self.mobile_XPATH).click()
        self.driver.find_element(By.XPATH, self.mobile_XPATH).clear()
        self.driver.find_element(By.XPATH, self.mobile_XPATH).send_keys(number)

    def random_text_XPATH(self,random_text):
        self.driver.find_element(By.XPATH, self.radom_text_XPATH).click()
        self.driver.find_element(By.XPATH, self.radom_text_XPATH).clear()
        self.driver.find_element(By.XPATH, self.radom_text_XPATH).send_keys(random_text)

    def enter_positon(self,position):
        self.driver.find_element(By.XPATH, self.position_XPATH).click()
        self.driver.find_element(By.XPATH, self.position_XPATH).clear()
        self.driver.find_element(By.XPATH, self.position_XPATH).send_keys(position)

    def enter_department(self,depart):
        self.driver.find_element(By.XPATH, self.department_XPATH).click()
        self.driver.find_element(By.XPATH, self.department_XPATH).clear()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.department_XPATH))).send_keys(depart)

    def enter_supervisor(self,sup):
        self.driver.find_element(By.XPATH,self.supervisor_XPATh).click()
        self.driver.find_element(By.XPATH,self.supervisor_XPATh).clear()
        self.driver.find_element(By.XPATH,self.supervisor_XPATh).send_keys(sup)

    def enter_assistant(self,assistant):
        self.driver.find_element(By.XPATH,self.assistant_XPATh).click()
        self.driver.find_element(By.XPATH,self.assistant_XPATh).clear()
        self.driver.find_element(By.XPATH,self.assistant_XPATh).send_keys(assistant)

    def enter_referral(self,referral):
        self.driver.find_element(By.XPATH,self.referral_XPATh).click()
        self.driver.find_element(By.XPATH,self.referral_XPATh).clear()
        self.driver.find_element(By.XPATH,self.referral_XPATh).send_keys(referral)

    def enter_source(self):
        self.driver.find_element(By.XPATH, self.source_xpath).click()
        self.driver.find_element(By.XPATH,self.source_options).click()

    def click_toggles(self):
        self.driver.find_element(By.XPATH,self.Call_toggle_btn_XPATH).click()
        self.driver.find_element(By.XPATH,self.Text_toggle_btn_XPATH).click()
        self.driver.find_element(By.XPATH, self.Email_toggle_btn_XPATH).click()

    def enter_dob_date(self,date):
        self.driver.find_element(By.XPATH, self.DOB_date_XPATH).click()
        self.driver.find_element(By.XPATH, self.DOB_date_XPATH).clear()
        self.driver.find_element(By.XPATH, self.DOB_date_XPATH).send_keys(date)

    def enter_dob_month(self):
        self.driver.find_element(By.XPATH, self.DOB_month_XPATH).click()
        self.driver.find_element(By.XPATH, self.DOB_month_click_XPATH).click()

    def enter_dob_year(self,year):
        self.driver.find_element(By.XPATH, self.DOB_year_XPATH).click()
        self.driver.find_element(By.XPATH, self.DOB_year_XPATH).clear()
        self.driver.find_element(By.XPATH, self.DOB_year_XPATH).send_keys(year)

    def enter_identifier(self,identifier):
        self.driver.find_element(By.XPATH, self.identifier_XPATH).send_keys(identifier)

    def click_save_btn(self):
        self.driver.find_element(By.XPATH,self.save_btn_XPATh).click()
        time.sleep(4)

    def open_document_tab(self):
        menu_icon2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.menu_icon2_XPATH)))
        self.actions.move_to_element(menu_icon2).perform()
        documents_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.documents_link_XPATH)))
        documents_link.click()

    def search_contact(self,con):
        self.driver.find_element(By.XPATH,self.search_bar_in_contacts_page_xpath).click()
        self.driver.find_element(By.XPATH, self.search_bar_in_contacts_page_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_bar_in_contacts_page_xpath).send_keys(con)
        self.driver.find_element(By.XPATH, self.search_bar_in_contacts_page_xpath).send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.quit()