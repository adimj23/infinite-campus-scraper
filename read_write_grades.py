import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from secret import IC_ID, IC_PW, SHEET_NAME
from schemas import Student, Course, Grade
from create_profile import login
from datetime import date
import gspread
import schemas
import pandas as pd

driver = webdriver.Chrome()

login(driver)

driver.get("https://infinitecampus.naperville203.org/campus/nav-wrapper/student/portal/student/grades")
time.sleep(1)
driver.switch_to.frame(0)
time.sleep(1)
grade_finder = driver.find_elements(By.TAG_NAME, "div")
print("Cards:")
print()

counter = 0
for element in grade_finder:
    if element.get_attribute('class') == 'grades__flex-row__item grades__flex-row__item--left':
        #  print(element.text)
        if element.text == "Semester Grade":
            row_info = element.find_element_by_xpath('..')
            # print("ya")
            semester_grade = row_info.find_element_by_class_name("grading-score__row-spacing")
            grade_as_int = semester_grade.text.strip("(%)")
            print(element.text + ":", grade_as_int)
            
    counter += 1


gc = gspread.service_account(filename="creds.json")
sh = gc.open(SHEET_NAME).sheet1

"""
daily_grades = []
for course in student.courses:
    daily_grades.append(course.get_grade(-1))

sh.append_row(daily_grades)
"""
