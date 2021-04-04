from secret import IC_ID, IC_PW
from selenium import webdriver

def login(driver):
    # get IC login
    driver.get("https://infinitecampus.naperville203.org/campus/portal/students/naperville.jsp")
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys(IC_ID)
    password.send_keys(IC_PW)
    driver.find_element_by_xpath("//input[@type='submit']").click()