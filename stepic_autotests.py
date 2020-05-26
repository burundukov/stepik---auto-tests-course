# The task solution from test  https://stepik.org/lesson/228249/step/3?unit=200781

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    sum = str(num1 + num2)

    Select(browser.find_element_by_tag_name("select")).select_by_value(sum)

    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()

finally:
    time.sleep(8)
    browser.quit()
