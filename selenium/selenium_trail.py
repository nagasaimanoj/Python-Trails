from selenium.webdriver import Chrome

# driver object to handle webpage
driver = Chrome()
driver.get(r"https://person-crud.herokuapp.com/")

# getting count of records
list_len = len(driver.find_elements_by_class_name("row"))

# filling form
driver.find_elements_by_tag_name("input")[0].send_keys("test " + str(list_len))
driver.find_elements_by_tag_name("input")[1].send_keys(str(list_len))
driver.find_elements_by_tag_name("input")[2].click()

# displaying list
for each_row in driver.find_elements_by_class_name("row")[1:]:
    row = each_row.find_elements_by_class_name("col-lg-4")
    print(row[0].text, row[1].text)

# closing browser window
driver.quit()
