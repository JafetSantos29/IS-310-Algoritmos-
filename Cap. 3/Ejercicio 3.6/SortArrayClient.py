from SortArray import *  # Importar modulo SortArray
import random  # Importar modulo random
import timeit  # Importar modulo timeit

def initArray(size=100, maxValue=100, seed=3.14159):
    """Crea un Array del tamaño especificado con una secuencia fija de
    elementos "aleatorios"."""
    arr = Array(size)  # Crear objeto Array
    random.seed(seed)  # Establecer generador de numeros aleatorios
    for i in range(size):  # A un estado conocido, luego hacer un ciclo
        arr.insert(random.randrange(maxValue))  # Insertar numeros aleatorios
    return arr  # Devolver el Array lleno


arr = initArray()  # Crear el Array con initArray()
# Imprimir el contenido del Array
print("Array que contiene", len(arr), "elementos:\n", arr)

arr.insertionSortAndDedupe()
print('Array ordenado y sin duplicados contiene:')
print(arr)