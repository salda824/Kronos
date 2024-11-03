import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def forms_to_sheets():
    # Define los alcances de acceso para Google Sheets
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    # Carga las credenciales de la cuenta de servicio con los scopes
    creds = Credentials.from_service_account_file("rich-phenomenon-440300-k7-a74460cbe849.json", scopes=scopes)
    client = gspread.authorize(creds)

    # Accede a la hoja de Google Sheets
    sheet = client.open("Postulacion").sheet1
    data = pd.DataFrame(sheet.get_all_records())
    
    return data
