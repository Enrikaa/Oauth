import os
from Google import Create_Service

class Sheet:
    def __init__(self, client_name):
        'client1.amocrm.com'
        self.CLIENT_SECRET_FILE = ""

    def create_service(self):
        self.googleService = Create_Service(self.CLIENT_SECRET_FILE,'sheets','v4',['https://www.googleapis.com/auth/spreadsheets'])

    def create_document(self):
        self.sheets_file1 = self.googleService.spreadsheets().create().execute()
        self.getId = self.sheets_file1['spreadsheetId']
        self.myspreadsheets = self.googleService.spreadsheets().get(spreadsheetId=self.sheets_file1['spreadsheetId']).execute()
        print('---------------------------------------------')
        print(self.myspreadsheets['spreadsheetUrl'])

    def update_info(self): 

        worksheet_name = 'Sales North!'
        cell_range_insert = 'B2'
        values = (
            ('Col A', 'Col B', 'Col C', 'Col D'),
            ('1column', '2column', '3column', '4column')
        )
        value_range_body = {
            'majorDimension': 'ROWS',
            'values': values
        }
        self.googleService.spreadsheets().values().update(
            spreadsheetId=self.getId,
            valueInputOption='USER_ENTERED',
            range=worksheet_name + cell_range_insert,
            body=value_range_body
        ).execute()  


client_name = 'Client_secret'
sheet = Sheet(client_name) # , api_service_name, api_version, scopes)
sheet.create_service()
sheet.create_document()
sheet.update_info()
