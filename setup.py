import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from secret import SHEET_NAME
from login import login 
import gspread

def add_courses():
    driver = webdriver.Chrome()
    login(driver)

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
    sh = gc.open(SHEET_NAME).sheet1
    sh.append_row(courses)

add_courses()