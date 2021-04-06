import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from secret import IC_ID, IC_PW, SHEET_NAME, DRIVER_PATH
from datetime import datetime
from login import login 
import gspread

def add_grades(): # get list of course grades
    my_options = webdriver.ChromeOptions()
    my_options.headless = True
    driver = webdriver.Chrome(DRIVER_PATH, options=my_options)
    login(driver)

    driver.get("https://infinitecampus.naperville203.org/campus/nav-wrapper/student/portal/student/grades")
    time.sleep(1)
    driver.switch_to.frame(0)
    time.sleep(1)
    grade_finder = driver.find_elements(By.TAG_NAME, "div")

    daily_grades = []
    date_time = datetime.now().strftime("%m/%d/%Y")    
    daily_grades.append(date_time)
    
    for element in grade_finder:
        if element.get_attribute('class') == 'grades__flex-row__item grades__flex-row__item--left':
            #  print(element.text)
            if element.text == "Semester Grade":
                row_info = element.find_element_by_xpath('..')
                # print("ya")
                semester_grade = row_info.find_element_by_class_name("grading-score__row-spacing")
                grade_as_num = semester_grade.text.strip("(%)")
                daily_grades.append(float(grade_as_num)/100)

    gc = gspread.service_account(filename="creds.json")
    sh = gc.open(SHEET_NAME).sheet1
    sh.append_row(daily_grades, 'USER_ENTERED')

add_grades()