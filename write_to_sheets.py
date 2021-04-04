import gspread
import schemas
from secret import SHEET_NAME

gc = gspread.service_account(filename="creds.json")

sh = gc.open('IC-scraper-test').sheet1
# sh.update('A1', 'woah')
# sh.append_row(['first', 'second', 'third'])

spreadsheet = {
    'properties': {
        'title': "test sheet 1"
    }
}

spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                    fields='spreadsheetId').execute()
print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))