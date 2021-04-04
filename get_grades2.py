import gspread
import schemas
import pandas as pd
from secret import SHEET_NAME

gc = gspread.service_account(filename="creds.json")
sh = gc.open(SHEET_NAME).sheet1

"""
daily_grades = []
for course in student.courses:
    daily_grades.append(course.get_grade(-1))

sh.append_row(daily_grades)
"""