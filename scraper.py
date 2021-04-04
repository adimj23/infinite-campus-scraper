from selenium import webdriver
  
# create webdriver object
driver = webdriver.Chrome()
# get google.co.in
driver.get("https://infinitecampus.naperville203.org/campus/portal/students/naperville.jsp")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("-----")
password.send_keys("-----")

driver.find_element_by_xpath("//input[@type='submit']").click()

driver.get("https://infinitecampus.naperville203.org/campus/nav-wrapper/student/portal/student/grades")

# driver.implicitly_wait(10)

# elements = driver.find_element_by_xpath("//input[@titletext='Grades']")

# print(driver.window_handles)
# print(elements)

