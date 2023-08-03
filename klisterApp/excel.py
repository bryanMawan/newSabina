import gspread


def add_row_to_google_sheets(spreadsheet_id, data, sheet_id):
    # Authenticate with Google Sheets API using service account credentials
    try:
        creds = gspread.service_account(filename='serviceAccount.json')
        print("Authenticated with Google Sheets API.")
    except gspread.exceptions.SpreadsheetNotFound:
        print("Google Sheets file not found. Make sure the file exists or create a new one.")
        return

    try:
        ## for chatgpt
        # Open the Google Sheets file by its ID
        sheet_title = ""
        spreadsheet = creds.open_by_key(spreadsheet_id)
        for worksheet in spreadsheet.worksheets():
            if worksheet.id == int(sheet_id):
                sheet_title = worksheet.title
        sheet = spreadsheet.worksheet(sheet_title)
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


def get_sheet_name(spreadsheet_key, sheet_id):
    # Authenticate with the service account
    creds = gspread.service_account(filename='serviceAccount.json')
    # Open the spreadsheet using the key
    title = ""
    try:
        spreadsheet = creds.open_by_key(spreadsheet_key)

        # Get the sheet by sheet ID (gid)
        for worksheet in spreadsheet.worksheets():
            if worksheet.id == int(sheet_id):
                title += str(worksheet.title)
        return title
    except gspread.exceptions.APIError as e:
        print(f"Error accessing the spreadsheet with URL: {spreadsheet_key}")
        return None


def extract_key_and_gid(url):
    # Extract the key from the URL
    key_start = url.find("/d/") + 3
    key_end = url.find("/", key_start)
    key = url[key_start:key_end]

    # Extract the gid from the URL
    gid_start = url.find("gid=") + 4
    gid_end = url.find("/", gid_start)
    if gid_end == -1:  # If gid is the last parameter in the URL
        gid_end = len(url)
    gid = url[gid_start:gid_end]

    return key, gid


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
