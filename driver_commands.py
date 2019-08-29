import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import time


# Basic driver commands a.k.a. moves

@allure.step('Navigation to {1}')
def driver_get(driver, testlink):
    driver.get(testlink)


@allure.step('Setting browser resolution to {1}x{2}')
def driver_get_window_size(driver, width, height):
    driver.set_window_size(width, height)


@allure.step('Element click on element with xpath - {1}')
def uielement_click(driver, elempath):
    explicit_wait_for_element_visibility(driver, elempath)
    driver.find_element_by_xpath(elempath).click()


@allure.step('hover on element with xpath - {1}')
def uielement_hover(driver, elempath):
    explicit_wait_for_element_visibility(driver, elempath)
    element_to_hover_over = driver.find_element_by_xpath(elempath)
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()


@allure.step('Check if the element is visible - xpath - {1}')
def element_visible(driver, elempath):
    wait = WebDriverWait(driver, 20, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH, elempath)))
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, elempath)))
    except NoSuchElementException or TimeoutException:
        return False
    return True

@allure.step('Type in the field - {2}')
def uifield_sendkeys(driver, elempath, stringtotype):
    explicit_wait_for_element_visibility(driver, elempath)
    driver.find_element_by_xpath(elempath).send_keys(stringtotype)


@allure.step('Choose value from a dropdown')
def dropdown_choose_value(driver, elempath, value):
    uielement_click(driver, elempath)
    uielement_click(driver, value)


@allure.step("Scroll element into view")
def scroll_element_into_view(driver, elempath):
    element = driver.find_element_by_xpath(elempath)
    driver.execute_script("arguments[0].scrollIntoView();", element)


def explicit_wait_for_element_visibility(driver, elempath):
    wait = WebDriverWait(driver, 20, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH, elempath)))


@allure.step('Getting text of element')
def element_text(driver, elempath):
    wait = WebDriverWait(driver, 20, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH, elempath)))
    for i in range(0, 22):
        try:
            text = driver.find_element_by_xpath(elempath).text
        except StaleElementReferenceException:
            pass
    return text


@allure.step('Getting attribute value of element')
def element_value(driver, elempath):
    wait = WebDriverWait(driver, 20, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH, elempath)))
    return driver.find_element_by_xpath(elempath).get_attribute("value")


@allure.step('Getting attribute value of element - {2}')
def element_attribute(driver, elempath, attribute_name):
    wait = WebDriverWait(driver, 20, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH, elempath)))
    return driver.find_element_by_xpath(elempath).get_attribute(attribute_name)


def count_elements(driver, locator_block):
    return len(driver.find_elements_by_xpath(locator_block))


@allure.step('Run command in JS console - {1}')
def run_in_console(driver, command):
    driver.execute_script(command)


@allure.step('close current tab')
def close_current_tab(driver):
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

@allure.step('close current tab_and_save_url')
def close_current_tab_and_save_url(driver):
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    url = driver.current_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    return url

@allure.step('Check if {2} the {3} is present in the desired place')
def text_in_block_exists(driver, locator_block, test_data, test_data_type):
    elements_in_block = driver.find_elements_by_xpath(locator_block)
    print(test_data)
    for element in elements_in_block:
        print(element)
        print(element.text)
        print(element.get_attribute('href'))
        if test_data_type == "text" and test_data in element.text:
            return True
        if test_data_type == "link" and test_data == element.get_attribute('href'):
            return True
    return False


@allure.step('Compare current url to expected {1}')
def compare_current_url(driver, expected_url):
    time.sleep(1)
    print(expected_url)
    print(driver.current_url)
    if expected_url in driver.current_url:
        return True
    else:
        return False
