import random

def doubleHashProbe(start, key, size):
    # Generador para determinar el intervalo de búsqueda desde una segunda función hash de la clave
    yield start % size # Devuelve el índice de la primera celda
    step = doubleHashStep(key, size) # Obtiene el tamaño del paso para esta clave
    for i in range(1, size): # Itera sobre todas las celdas restantes usando el paso desde la segunda función hash de la clave
        yield (start + i * step) % size

def doubleHashStep(key, size):
    # Determina el tamaño del paso para una clave dada usando un método de hashing multiplicativo
    PRIME_1 = 17
    PRIME_2 = 19
    hash_val = 0
    for byte in key.to_bytes((key.bit_length() + 7) // 8, byteorder='big'):
        hash_val = (hash_val * PRIME_1 + byte + PRIME_2) % size
    return 1 + ((size - key) % (size - 1))

def primeBelow(n):
    # Encuentra el número primo más grande por debajo de n
    n -= 1 if n % 2 == 0 else 2 # Empieza con un número impar por debajo de n
    while (3 < n and not is_prime(n)): # Mientras n sea mayor que 3 o no sea primo, pasa al siguiente número impar
        n -= 2
    return n # Devuelve el número primo o 3

def is_prime(n):
    # Comprueba si un número es primo
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_table():
    # Genera una tabla de inserción de 20 valores aleatorios
    SIZE = 31
    PRIME = primeBelow(SIZE)
    table = [None] * SIZE
    keys = random.sample(range(100000), 20)
    for key in keys:
        print(f"Inserción de clave: {key}")
        idx = key % SIZE
        if table[idx] is None:
            table[idx] = key
            print(f"  Insertado en índice {idx}")
        else:
            print(f"  Colisión en índice {idx}")
            for i in doubleHashProbe(idx, key, SIZE):
                if table[i] is None:
                    table[i] = key
                    print(f"  Insertado en índice {i}")
                    break
                else:
                    print(f"  Intento en índice {i}")
    print("Tabla de inserción final:")
    for i, val in enumerate(table):
        print(f"  Índice {i}: {val}")

generate_table()
