# instantiate an empty dict
context_data = {"users": {}, "test_data": {}, "locator": {}}

# Test_data
context_data["test_data"]["link_to_generate_reg_form"] = "https://www.jotform.com/form-templates/music-school-registration-form"
context_data["test_data"]["testlink"] = ""

context_data["test_data"]["first_name"] = "John"
context_data["test_data"]["last_name"] = "Smith"

# Locators by XPath
context_data["locator"]["use_as_template"] = "/html[@class='no-js']/body[@class='no-header modal-open']/div[@class='modal template-detail'][1]/div[@class='modal-wrapper']/div[@class='template-detail-wrapper']/div[@class='container']/div[@class='modal-header']/div[@class='button-wrapper']/button[@class='cta-usetemplate ']"
context_data["locator"]["navigate_to_publish_tab"] = "//a[@id='siteNav_id_publish']"
context_data["locator"]["public_link_to_form"] = "//div[@class='copyLink-input js-copyInpt']"
context_data["locator"]["registration_form_header"] = "//h1[@id='header_1']"

context_data["locator"]["first_name"] = "//input[@id='first_3']"
context_data["locator"]["last_name"] = "//input[@id='last_3']"
context_data["locator"]["name_error"] = "//div[@id='cid_3']/div[@class='form-error-message']"

context_data["locator"]["month_of_birth"] = "//select[@id='input_4_month']"
context_data["locator"]["day_of_birth"] = "//select[@id='input_4_day']"
context_data["locator"]["year_of_birth"] = "//select[@id='input_4_year']"
context_data["locator"]["date_of_birth_error"] = "//div[@id='cid_4']/div[@class='form-error-message']"

context_data["locator"]["instrument"] = "//select[@id='input_5']"
context_data["locator"]["instrument_error"] = "//div[@id='cid_5']/div[@class='form-error-message']"

context_data["locator"]["first_checkbox_of_days"] = "//label[@id='label_input_6_0']"
context_data["locator"]["day_error"] = "//div[@id='cid_6']/div[@class='form-error-message']"

context_data["locator"]["month_to_start_from"] = "//input[@id='month_7']"
context_data["locator"]["month_to_start_error"] = "//div[@id='cid_7']/div[@class='form-error-message']"
context_data["locator"]["submit_button"] = "//button[@id='input_2']"

context_data["locator"]["submission_success_text"] = "/html/body[@class='thankyou']/div[@id='stage']/div/p"
