from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

my_options = webdriver.ChromeOptions()
my_options.headless = True

file = open('secret.json', "r")
obj = json.load(file)

driver = webdriver.Chrome(options=my_options)

def login(driver, id, pw):
    # get IC login
    driver.get("https://infinitecampus.naperville203.org/campus/portal/students/naperville.jsp")
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys(id)
    password.send_keys(pw)
    driver.find_element_by_xpath("//input[@type='submit']").click()

def add_courses(driver, filename):
    driver.get("https://infinitecampus.naperville203.org/campus/nav-wrapper/student/portal/student/grades")
    time.sleep(1)
    driver.switch_to.frame(0)
    time.sleep(1)
    search_grades_cards = driver.find_elements_by_xpath("//div[@class='collapsible-card grades__card']")
    courses = ["Date"]
    for element in search_grades_cards:
        all_divs = element.find_elements(By.TAG_NAME, "div") 
        course_name = all_divs[0].find_elements_by_class_name("ellipsis-container")
        courses.append(course_name[0].text)

    # add courses to google sheet
    gc = gspread.service_account(filename="creds.json")
    sh = gc.open(filename).sheet1
    sh.append_row(courses)
    print("Course names added.")

def add_grades(driver, filename): # get list of course grades
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
            if element.text == "Semester Grade":
                row_info = element.find_element_by_xpath('..')
                try:
                    semester_grade = row_info.find_element_by_class_name("grading-score__row-spacing")
                    grade_as_num = semester_grade.text.strip("(%)")
                    daily_grades.append(float(grade_as_num)/100)
                except:
                    daily_grades.append(1)

    gc = gspread.service_account(filename="creds.json")
    sh = gc.open(filename).sheet1
    sh.append_row(daily_grades, 'USER_ENTERED')
    print("Grades Updated.")

login(driver, obj["IC_ID"], obj["IC_PW"])

if obj["IS_NEW_TERM"]:
    add_courses(driver, obj["SHEET_NAME"])

    file = open("secret.json", "w")
    obj["IS_NEW_TERM"] = False
    json.dump(obj, file, sort_keys=True, indent=4)
    
add_grades(driver, obj["SHEET_NAME"])

driver.quit();
