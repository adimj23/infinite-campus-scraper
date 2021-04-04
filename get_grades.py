import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from secret import IC_ID, IC_PW
from schemas import Student, Courses, Grade

search_grades_cards = driver.find_elements_by_xpath("//div[@class='collapsible-card grades__card']")