import openpyxl
import pytest


from page_object_model.Cogmento_signup import Cogmento_signup
from page_object_model.Signup_and_login import Signup_and_login
import random, string


@pytest.mark.usefixtures("setup_and_teardown")
class Test_Signup_and_login:
    def test_Signup_and_login(self):
        workbook = openpyxl.load_workbook("C:/Users/rvina/OneDrive/Desktop/Automation_Project1_Page_Object_Model/Book1.xlsx")  # Read Excel data
        sheet = workbook["signup_data"]  # Sheet

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if not row or all(cell is None for cell in row):
                continue

            company_name, first_name,last_name,password,password_confirm= row[:5]

        register_page = Signup_and_login(self.driver)                                  # Step 1: Open Mailinator
        register_page.click_popup_btn()

        random_letters = ''.join(random.choices(string.ascii_lowercase, k=5))          # Step 2: Generate Email and Copy
        register_page.enter_input(random_letters)
        register_page.click_on_go_btn()

        cogmento_page = Cogmento_signup(self.driver)                                   # Step 3: Sign Up Page
        cogmento_page.open_signup_page()
        add = random_letters + '@mailinator.com'
        cogmento_page.enter_email(add)
        cogmento_page.click_agree_checkbox()

        cogmento_page.click_on_captcha()                                               # Step 4: Captcha & email confirmation

        register_page.enter_company_name(company_name)                                    # Step 5: Signup and entering details
        register_page.enter_first_name(first_name)
        register_page.enter_last_name(last_name)
        register_page.enter_password(password)
        register_page.enter_password_confirm(password_confirm)
        register_page.enter_submit_button()

        register_page.enter_login_email(add)
        register_page.enter_login_password("Vinay111")
        register_page.click_login_btn()

