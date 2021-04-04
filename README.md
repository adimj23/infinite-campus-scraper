# infinite-campus-scraper

# Required Libraries
- selenium
- pandas

# Setting up some constants
1. In secret-template.py, replace all lines with your info.
2. Rename the file to secret.py

# Linking your Google Sheet
1. Go to console.cloud.google.com in your browser using your desire Google Account.
2. Create New Project. Give it whatever name you like. Click Create.
3. Once the project has been created, via the search bar, enable the Google Drive API and Google Sheets API for this project.
4. In the credentials tab, click CREATE CREDENTIALS. Click Service Account and give it whatever name you like. Click CONTINUTE and DONE.
5. For this new service account, click on the pen and click ADD KEY > CREATE NEW KEY > JSON. Save this file in the folder as this app.
6. Rename this file to "creds.json"
7. In Google Drive, create and title a new Google Sheet. You will need this name later.
8. Open creds.json and copy the "client_email" value and share your Sheet with this email.
