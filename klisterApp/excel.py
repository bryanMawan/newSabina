import gspread
import re


def add_row_to_google_sheets(spreadsheet_id, data):
    # Authenticate with Google Sheets API using service account credentials
    try:
        creds = gspread.service_account(filename='serviceAccount.json')
        print("Authenticated with Google Sheets API.")
    except gspread.exceptions.SpreadsheetNotFound:
        print("Google Sheets file not found. Make sure the file exists or create a new one.")
        return

    try:
        # Open the Google Sheets file by its ID
        sheet = creds.open_by_key(spreadsheet_id).sheet1
        print("Google Sheets file opened.")
    except gspread.exceptions.WorksheetNotFound:
        print("Worksheet not found. Creating a new worksheet.")
        sheet = creds.create(spreadsheet_id)
        sheet = sheet.sheet1
        print("New worksheet created.")

    # Create headers if the sheet is empty
    if len(sheet.get_all_values()) == 0:
        headers = list(data.keys())
        sheet.append_row(headers)
        sheet.format("A1:{}".format(chr(65 + len(headers) - 1)), {
            "textFormat": {
                "bold": True
            }
        })
        print("Headers added.")

    # Append the data to a new row
    row_data = list(data.values())
    sheet.append_row(row_data)
    print("Data added.")

    print("Google Sheets updated.")


def get_sheet_name(spreadsheet_id):
    # Authenticate with Google Sheets API using service account credentials
    try:
        creds = gspread.service_account(filename='serviceAccount.json')
        print("Authenticated with Google Sheets API.")
    except gspread.exceptions.SpreadsheetNotFound:
        print("Google Sheets file not found. Make sure the file exists or create a new one.")
        return None

    try:
        # Open the Google Sheets file by its ID
        spreadsheet = creds.open_by_key(spreadsheet_id)
        print("Google Sheets file opened.")
        # Get the name of the first sheet in the spreadsheet
        sheet_name = spreadsheet.get_worksheet(0).title
        return sheet_name
    except gspread.exceptions.WorksheetNotFound:
        print("Worksheet not found.")
        return None


def extract_key_from_url(url):
    # Regular expression pattern to match the key in the Google Sheets URL
    pattern = r'/spreadsheets/d/([a-zA-Z0-9-_]+)'
    
    # Search for the key using the pattern
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None


# Example usage
data = {
    "name": "John Doe",
    "age": 30,
    "stadsdel": "Stadsområde Centrum",
    "idrott": "Football",
    "önskad idrott": "Tennis",
    "in a union": True
}

# spreadsheet_id = "1_aObUyZon_fAFbXmA5bXfo5wkc-xZQ5TNE17KTAY8VQ"
# add_row_to_google_sheets(spreadsheet_id, data)
