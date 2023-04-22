import random
def multiplicativeHash(key):
    # Función de hashing multiplicativa
    hashVal = 0
    byteMask = 0xFF
    prime1 = 53
    prime2 = 89
    while key > 0:
        byte = key & byteMask
        hashVal = hashVal * prime1 + (byte + prime2)
        key >>= 8
    return hashVal

def doubleHashProbe(start, key, size):
    # Generador para determinar el intervalo de búsqueda desde una segunda función hash de la clave
    yield start % size # Devuelve el índice de la primera celda
    step = multiplicativeHash(key) % 19 + 1 # Obtiene el tamaño del paso para esta clave
    for i in range(1, size): # Itera sobre todas las celdas restantes usando el paso desde la segunda función hash de la clave
        yield (start + i * step) % size

def insertKeys():
    # Inserta 20 claves enteras aleatorias en una tabla hash
    tableSize = 23
    smallPrime = 19
    hashTable = [None] * tableSize
    keys = [random.randint(0, 99999) for _ in range(20)]
    for key in keys:
        index = multiplicativeHash(key) % tableSize
        if hashTable[index] is None:
            hashTable[index] = key
            print(f"{key} se ha insertado en la posición {index}")
        else:
            print(f"Colisión para {key} en la posición {index}")
            for i in doubleHashProbe(index, key, tableSize):
                if hashTable[i] is None:
                    hashTable[i] = key
                    print(f"{key} se ha insertado en la posición {i}")
                    break
    print(hashTable)
