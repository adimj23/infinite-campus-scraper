from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import selenium

# create webdriver object
driver = webdriver.Chrome()
# get IC login
driver.get("https://infinitecampus.naperville203.org/campus/portal/students/naperville.jsp")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

execfile("secret.py")

username.send_keys(IC_ID)
password.send_keys(IC_PW)

driver.find_element_by_xpath("//input[@type='submit']").click()

driver.get("https://infinitecampus.naperville203.org/campus/nav-wrapper/student/portal/student/grades")

time.sleep(2)

# size = len(driver.find_elements(By.TAG_NAME, "iframe"))

driver.switch_to.frame(0)

table_rows = driver.find_elements(By.CLASS_NAME, "grades__row clickable router-link-reset ng-star-inserted")
print("Cards:")
print()

for element in table_rows:
    print(element.get_attribute('class'))
    print(element.get_attribute('id'))
    for subelement in element.find_elements(By.TAG_NAME,"div"):
        print("\n" + subelement.get_attribute('class'))
        print("\n" + subelement.get_attribute('id'))
    print("=====")

print("No more script")

time.sleep(5)