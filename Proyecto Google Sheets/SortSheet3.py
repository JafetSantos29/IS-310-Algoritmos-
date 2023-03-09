import random
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de las credenciales de Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY_FILE = 'key.json'
SPREADSHEET_ID = '1aXOEaRk3uYrC9_xgrBZR0F1PPqiDJXdCoFTsZNPDuXI'

creds = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# Formato para las celdas que están siendo comparadas
highlighted_format = {
    "backgroundColor": {
        "red": 1,
        "green": 0.6,
        "blue": 0.6
    }
}

# Formato por defecto de las celdas
default_format = {
    "backgroundColor": {
        "red": 1,
        "green": 1,
        "blue": 1
    }
}


def initArray(size=10, maxValue=100, seed=3.14159):
    # Create an Array of the specified size with a fixed sequence of 'random' elements
    arr = [random.randrange(maxValue) for _ in range(size)]
    return arr


# Agregar números aleatorios en la columna A
numbers = initArray()
sheet.update('A2:A11', [[num] for num in numbers])

# Ordenar mediante BubbleSort y escribir en la columna C
arr = numbers.copy()
for i in range(len(arr)):
    for j in range(len(arr)-1):
        # Resaltar las celdas que están siendo comparadas
        sheet.format('C' + str(j+2) + ':C' + str(j+3), highlighted_format)
        if arr[j] > arr[j+1]:
            time.sleep(0.2)  # pausa de 0.20 segundos
            arr[j], arr[j+1] = arr[j+1], arr[j]
            # actualizar la celda correspondiente
            sheet.update('C' + str(j+2), [[arr[j]]])
            # actualizar la celda correspondiente
            #sheet.update('C' + str(j+3), [[arr[j+1]]])
            sheet.update('C' + str(j+3), [[str(arr[j+1])]])
        # Regresar las celdas al formato por defecto
        sheet.format('C' + str(j+2) + ':C' + str(j+3), default_format)
sheet.update('C2:C11', [[num] for num in arr])

# Ordenar mediante SelectionSort y escribir en la columna E
arr = numbers.copy()
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
            # Resaltar las celdas que están siendo comparadas
        sheet.format('E' + str(j+1) + ':E' + str(min_idx+2), highlighted_format)
        if arr[j] < arr[min_idx]:
            min_idx = j
            time.sleep(0.2)  # pausa de 0.20 segundos
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            sheet.update('E' + str(i+2), [[arr[i]]])  # actualizar la celda correspondiente
            # actualizar la celda correspondiente
            sheet.update('E' + str(min_idx+2), [[arr[min_idx]]])
        # Regresar las celdas al formato por defecto
    sheet.format('E' + str(i+2) + ':E' + str(min_idx+2), default_format)
sheet.update('E2:E11', [[num] for num in arr])

# Ordenar mediante InsertionSort y escribir en la columna G
arr = numbers.copy()
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j] :
        # Resaltar las celdas que están siendo comparadas
        sheet.format('G' + str(j+2) + ':G' + str(i+1), highlighted_format)
        time.sleep(0.2)  # pausa de 0.20 segundos
        arr[j+1] = arr[j]
        sheet.update('G' + str(j+3), [[arr[j]]])  # actualizar la celda correspondiente
        j -= 1
    arr[j+1] = key
    sheet.update('G' + str(j+2), [[key]])  # actualizar la celda correspondiente
    # Regresar las celdas al formato por defecto
    sheet.format('G' + str(j+2) + ':G' + str(i+2), default_format)
sheet.update('G2:G11', [[num] for num in arr])