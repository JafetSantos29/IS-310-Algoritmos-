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

for test in ['initArray().oddEvenSort()', 'initArray().bubbleSort()']:
    elapsed = timeit.timeit(test, number=100, globals=globals())
    print(test, "tomó", elapsed, "seconds", flush=True)

# Imprimir el contenido del Array
print("Array que contiene", len(arr), "elementos:\n", arr)

arr.deduplicate()
arr.oddEvenSort()
arr.insertionSort()  # Ordenar el Array con insertionSort()
# Imprimir el contenido del Array ordenado
print('El array ordenado contiene:\n', arr)

print("El Valor a la mitad es: ", arr.median())