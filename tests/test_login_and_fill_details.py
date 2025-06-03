# from selenium import webdriver
#
# from page_object_model.Contacts import ContactsPage
# from page_object_model.DocumentsPage import DocumentsPage
# from page_object_model.LoginPage import LoginPage
# import openpyxl
#
#
# class TestLogin:
#     def test_login(self):
#         workbook = openpyxl.load_workbook("C:/Users/rvina/OneDrive/Desktop/Automation_Project1_Page_Object_Model/Book1.xlsx")      # Read Excel data
#         sheet = workbook["login_data"]                                                                  # Sheet
#
#         for row in sheet.iter_rows(min_row=1, values_only=True):
#             if not row or all(cell is None for cell in row):
#                 continue
#
#             username,password = row
#
#
#         driver = webdriver.Chrome()
#         driver.maximize_window()                                                 # open url
#         login_page = LoginPage(driver)
#         login_page.click_url()
#
#         login_page.enter_email(username)                                       # login with valid credentials
#         login_page.enter_password(password)
#         login_page.click_btn()
#
#         login_page.click_users_icon()                                           # opening contact tab and create a contact
#
#         login_page.click_contacts_element()                                     # clicking the element
#         contacts_page = ContactsPage(driver)
#         contacts_page.click_create_btn_in_contacts_page()                          #  wait and click the create button in contacts page
#
#         contacts_page.enter_the_firstname("Vinay")                                 #  entering details
#         contacts_page.enter_the_lastname("Relangi")
#         contacts_page.enter_the_middle_name("VR")
#
#         contacts_page.enter_company_name("Company")
#         contacts_page.enter_tag("Tags")
#         contacts_page.click_access_btn()
#         contacts_page.enter_the_email("vin@gmail.com")
#         contacts_page.enter_Category()
#         contacts_page.enter_status()
#         contacts_page.enter_into_textarea("some detailed information")
#         contacts_page.enter_into_social_channels()
#         contacts_page.enter_address("IND")
#         contacts_page.enter_city("KKD")
#         contacts_page.enter_state("AP")
#         contacts_page.enter_zip("533004")
#         contacts_page.enter_country()
#         contacts_page.enter_mobile("123123123")
#         contacts_page.random_text_XPATH("random text in the fields")
#         contacts_page.enter_positon('Manual Tester')
#         contacts_page.enter_department("IT")
#         contacts_page.enter_supervisor("supervisor")
#         contacts_page.enter_assistant("assistant")
#         contacts_page.enter_referral("persons")
#         contacts_page.enter_source()
#         contacts_page.click_toggles()
#         contacts_page.enter_dob_date("25")
#         contacts_page.enter_dob_month()
#         contacts_page.enter_dob_year("2001")
#         contacts_page.enter_identifier("Identify something")
#         contacts_page.click_save_btn()
#         contacts_page.open_document_tab()
#
#         documents_page = DocumentsPage(driver)
#         documents_page.wait_until_element_click()
#         documents_page.enter_title("Manual and Automation")
#         documents_page.click_access_btn_select_dropdown()
#         documents_page.enter_description("decsription")
#         documents_page.enter_contact("825224552466")
#         documents_page.enter_company("company")
#         documents_page.enter_deal("deal")
#         documents_page.enter_case("case")
#         documents_page.enter_task("task")
#         documents_page.enter_identifier("identifier")
#         documents_page.click_save()
#         documents_page.reopen_document_page()
#         documents_page.click_document_icon()
#         documents_page.search_document("Manual and Automation")
#         documents_page.click_search_btn()
#         documents_page.click_on_contact_text()
#         contacts_page.search_contact("vinay")
#
#
