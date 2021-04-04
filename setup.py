import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from secret import IC_ID, IC_PW
from schemas import Student, Course, Grade
from create_profile import login

student = Student("Bob", "Ross")

driver = webdriver.Chrome()

login(driver)

driver.get("https://infinitecampus.naperville203.org/campus/nav-wrapper/student/portal/student/grades")
time.sleep(1)
driver.switch_to.frame(0)
time.sleep(1)

search_grades_cards = driver.find_elements_by_xpath("//div[@class='collapsible-card grades__card']")
for element in search_grades_cards:
    all_divs = element.find_elements(By.TAG_NAME, "div") 
    course_name = all_divs[0].find_elements_by_class_name("ellipsis-container")
    print(course_name[0].text)
    course = Course(course_name[0].text)
    student.add_course(course)