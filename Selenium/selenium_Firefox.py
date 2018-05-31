from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://google.co.in")

driver.find_element_by_id("lst-ib").send_keys("Naga Sai Manoj")
driver.find_element_by_name("Google Search").click()

driver.quit()
