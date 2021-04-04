
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import selenium

from bs4 import BeautifulSoup

from secret import IC_ID, IC_PW

# create webdriver object
driver = webdriver.Chrome()
# get IC login
driver.get("https://infinitecampus.naperville203.org/campus/portal/students/naperville.jsp")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys(IC_ID)
password.send_keys(IC_PW)

driver.find_element_by_xpath("//input[@type='submit']").click()

driver.get("https://infinitecampus.naperville203.org/campus/nav-wrapper/student/portal/student/grades")
time.sleep(1)
driver.switch_to.frame(0)
time.sleep(1)

# search_grades_card = driver.find_elements_by_class_name("ellipsis-container")
# search_grades_cards = driver.find_elements(By.TAG_NAME, "div") 

# search_grades_card = driver.find_elements(By.CLASS_NAME, "grades__flex-row--nowrap ng-star-inserted")
#type(search_grades_card[0])
#print(search_grades_card[1].get_attribute('class'))
# print(len(search_grades_card))

# search_grades_cards = driver.find_elements_by_xpath("//div[@class='collapsible-card grades__card']")
# search_rows = search_grades_cards[0].find_elements_by_xpath("//span[@*] | //a[@*]")
# print(BeautifulSoup(search_grades_cards[0].get_attribute('innerHTML'), 'html.parser').prettify())


#print(BeautifulSoup(search_spans[0].get_attribute('innerHTML'), 'html.parser').prettify())
"""
print(BeautifulSoup(search_grades_cards[0].get_attribute('innerHTML'), 'html.parser').prettify())
print(BeautifulSoup(search_grades_cards[1].get_attribute('innerHTML'), 'html.parser').prettify())
"""
search_grades_cards = driver.find_elements_by_xpath("//div[@class='collapsible-card grades__card']")

for element in search_grades_cards:
    all_divs = element.find_elements(By.TAG_NAME, "div") 
    course_name = all_divs[0].find_elements_by_class_name("ellipsis-container")
    print(course_name[0].text)

# for element in search_grades_cards:
#     # print(BeautifulSoup(element.get_attribute('outerHTML'), 'html.parser').prettify())
    
#     # print(element.get_attribute('outerHTML'))
#     # print(element.get_attribute('class'))
#     # print(element.get_attribute('id'))
#     # print(element.get_attribute('text'))
    

#     if element.get_attribute('class') == 'grades__flex-row__item grades__flex-row__item--left':
#         print(element.text)
#         if element.text == "Semester Grade":
#             row_info = element.find_element_by_xpath('..')
#             # print("ya")
#             semester_grade = row_info.find_element_by_class_name("grading-score__row-spacing")
#             print(element.text + ":", semester_grade.text)


# for element in search_grades_card:
#     # print(element.get_attribute('class'))
#     # print(element.get_attribute('id'))
#     # print()
#     if element.get_attribute('class') == 'grades__flex-row--nowrap':
#         text_field = element.find_element(By.CLASS_NAME, "grades__flex-row__item grades__flex-row__item--left")
#         print(text_field.text)
#         if text_field.text == "Semester Grade":
#             print("ya")
#             # semester_grade = big_padre.find_element_by_class_name("grading-score__row-spacing")
#             # print(semester_grade.text)
            
print("No more script")
time.sleep(30)

"""

delay = 30
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'collapsible-card grades__card')))
    print("Page is ready!")
    print(myElem)
except TimeoutException:
    print("Loading took too much time!")
"""

# elements = driver.find_elements_by_class_name("grading-score__row-spacing")
# print(len(elements))
# driver.find_element_by_name(name)