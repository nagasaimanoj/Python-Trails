import time

from selenium.webdriver import Chrome

driver = Chrome()

driver.get("https://www.amazon.in/gp/product/B06X6KPCJT")
time.sleep(5)

driver.find_element_by_id("add-to-cart-button").click()
time.sleep(5)

driver.find_element_by_id("hlb-view-cart-announce").click()
time.sleep(5)
