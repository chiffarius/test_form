import allure
import driver_commands as dc
import time

@allure.title("generate form from template successfully")
def test_generate_form_from_template(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["link_to_generate_reg_form"])
    dc.uielement_click(driver, data_bag["locator"]["use_as_template"])
    dc.uielement_click(driver, data_bag["locator"]["navigate_to_publish_tab"])
    data_bag["test_data"]["testlink"] = dc.element_text(driver, data_bag["locator"]["public_link_to_form"])
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    assert dc.text_in_block_exists(driver, data_bag["locator"]["registration_form_header"],"Music School","text")


@allure.title("submit form successfully")
def test_submit_form_successfully(driver, data_bag):
    dc.driver_get(driver,data_bag["test_data"]["testlink"])
    dc.uifield_sendkeys(driver,data_bag["locator"]["first_name"],data_bag["test_data"]["first_name"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["last_name"], data_bag["test_data"]["last_name"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["month_of_birth"], "j")
    dc.uifield_sendkeys(driver, data_bag["locator"]["day_of_birth"], "1")
    dc.uifield_sendkeys(driver, data_bag["locator"]["year_of_birth"], "1")
    dc.uifield_sendkeys(driver, data_bag["locator"]["instrument"], "v")
    dc.uielement_click(driver, data_bag["locator"]["first_checkbox_of_days"])
    dc.scroll_element_into_view(driver,data_bag["locator"]["submit_button"])
    dc.uielement_click(driver, data_bag["locator"]["submit_button"])
    assert dc.text_in_block_exists(driver, data_bag["locator"]["submission_success_text"],"Your submission has been received.","text")