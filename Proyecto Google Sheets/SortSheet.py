#ordena sin mostrar en pantalla
import random 
import time 
import gspread #modulo para interactuar con googleShees
from oauth2client.service_account import ServiceAccountCredentials #importa la clase ServiceAccountCredentials del modulo oauth2client

# Configuración de las credenciales de Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] #alcance de las credenciales
KEY_FILE = 'key.json' #archivo clave para acceder a googlesheets
SPREADSHEET_ID = '1aXOEaRk3uYrC9_xgrBZR0F1PPqiDJXdCoFTsZNPDuXI'

creds = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, SCOPES) #obtiene las credenciales del googlesheets a partir del archivo clave
client = gspread.authorize(creds) #autoriza con las credenciales
sheet = client.open_by_key(SPREADSHEET_ID).sheet1 #abre la hoja de calculo correspondiente a la ID especificada y selecciona la primera hoja

def initArray(size=10, maxValue=100, seed=3.14159):
        #Create an Array of the specified size with a fixed sequence of 'random' elements
    arr = [random.randrange(maxValue) for _ in range(size)]
    return arr

# Agregar números aleatorios en la columna A
numbers = initArray() # llama a la funcion 'initArray' para obtener un arreglo de numeros aleatorios
time.sleep(0.1)
sheet.update('A2:A11', [[num] for num in numbers])

# Ordenar mediante BubbleSort y escribir en la columna C
arr = numbers.copy() # crea una copia del arreglo de numeros aleatorios
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]: # verifica si el elemento actual es mayor que el siguiente
            time.sleep(0.1)
            arr[j], arr[j+1] = arr[j+1], arr[j] # intercambia los elementos
sheet.update('C2:C11', [[num] for num in arr])

# Ordenar mediante SelectionSort y escribir en la columna E
arr = numbers.copy() # crea una copia del arreglo de numeros aleatorios
for i in range(len(arr)):
    min_idx = i # Se establece el índice mínimo como el actual
    for j in range(i+1, len(arr)): # Se itera la lista "arr" desde el índice siguiente al actual hasta el final
        if arr[j] < arr[min_idx]: # Si el elemento actual es menor que el mínimo, se actualiza el mínimo
            time.sleep(0.1)
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i] # Se intercambia el elemento actual con el mínimo
sheet.update('E2:E11', [[num] for num in arr])

# Ordenar mediante InsertionSort y escribir en la columna G
arr = numbers.copy()# crea una copia del arreglo de numeros aleatorios
for i in range(1, len(arr)):
    key_item = arr[i] # Se guarda el elemento actual como el "elemento clave"
    j = i - 1 #índice del elemento anterior como el índice actual menos uno
    while j >= 0 and arr[j] > key_item: # Se itera mientras el índice actual sea mayor o igual a cero y el elemento anterior sea mayor que el "elemento clave"
        time.sleep(0.1)
        arr[j + 1] = arr[j] # Se desplaza el elemento anterior al índice siguiente
        j -= 1
    arr[j + 1] = key_item # Se inserta el "elemento clave" en su posición correcta
sheet.update('G2:G11', [[num] for num in arr])