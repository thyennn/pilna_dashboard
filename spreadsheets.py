from Google import Create_Service

API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CLIENT_SECRET_FILE = "client_secret.json"
SPREADSHEET_ID_1 = "1uEXuVbtiuMr_uyQiX_cwZ5kw4kur8eKxD-Ai1nmLPPM"
SPREADSHEET_ID_2 = "1mVbkX1ApiLXiC17K2Sqsyi2ayGmJHndgS7CNEB_-zp8"
SHEET_ID = "0"


class GSheets:

    def __init__(self):
        self.ekipa = [
            ["Mateusz Godlewski", False, 0],
            ["Patryk Włodarczyk", False, 0],
            ["Jakub Błoch", False, 0],
            ["Przemysław Klucha", False, 0],
            ["Mikołaj Ogłaza", False, 0],
            ["Nikola Malinowska", False, 0],
            ["Krzysztof Dębski", False, 0],
            ["Jakub Trzmielewski", False, 0],
            ["Mateusz Gręda", False, 0]
        ]
        self.update_data(1)

    def update_data(self, start: int):

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID_2,
            majorDimension='ROWS',
            range='Pilna Pomoc!' + f"A{start}:G{start + 30000}"
        ).execute()

        count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        statuses = [False, False, False, False, False, False, False, False, False]

        for row in result['values']:
            if len(row) >= 5:
                for wariato in self.ekipa:
                    if wariato[0] in row[4]:
                        index = self.ekipa.index(wariato)
                        count[index] += 1
                        if row[3].strip() == "W trakcie":
                            statuses[index] = True
                        break
            if len(row) == 0:
                break

        for x in range(9):
            self.ekipa[x][2] = count[x]
            self.ekipa[x][1] = statuses[x]
