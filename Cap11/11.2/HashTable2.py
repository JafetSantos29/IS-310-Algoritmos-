"""import random

class HashTable:
    def __init__(self, size, probe):
        self.size = size
        self.probe = probe
        self.table = [None] * self.size
        self.count = 0

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None:
            hash_value = self.probe(hash_value)
        self.table[hash_value] = key
        self.count += 1

    def search(self, key):
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None:
            if self.table[hash_value] == key:
                return hash_value
            hash_value = self.probe(hash_value)
        return None

    def displaced_keys(self):
        displaced = 0
        for key in self.table:
            if key is not None and self.hash_function(key) != self.table.index(key):
                displaced += 1
        return displaced

def linear_probe(index):
    return (index + 1) % ht.size

def quadratic_probe(index):
    return (index + 1 ** 2) % ht.size

def double_hash_probe(index):
    return (index + hash(index)) % ht.size

# Folding functions
def fold_three_digits(key):
    result = 0
    while key > 0:
        result += key % 1000
        key //= 1000
    return result

def fold_two_digits(key):
    result = 0
    while key > 0:
        result += key % 100
        key //= 100
    return result

def fold_k_digits(key, k):
    str_key = str(key)
    groups = [str_key[i:i+k] for i in range(0, len(str_key), k)]
    folded = sum(int(group) for group in groups)
    return folded

# Generate 1000 random 10-digit integers
key_set = random.sample(range(10000000000), 1000)

# Initialize the values for the experiment
max_load_factors = [0.5, 0.7, 0.9]
probe_types = [linear_probe, quadratic_probe, double_hash_probe]

# Test folding with three digits
for load_factor in max_load_factors:
    for probe in probe_types:
        ht = HashTable(103, probe)
        for i in range(int(103 * load_factor)):
            key = fold_three_digits(key_set[i])
            ht.insert(key)
        displaced = ht.displaced_keys()
        print("Folding con tres dígitos, Tipo de sonda: {}, Factor de carga máximo: {}, Claves desplazadas: {}".format(probe.__name__, load_factor, displaced))

# Test folding with two digits
for load_factor in max_load_factors:
    for probe in probe_types:
        ht = HashTable(103, probe)
        for i in range(int(103 * load_factor)):
            key = fold_two_digits(key_set[i])
            ht.insert(key)
        displaced = ht.displaced_keys()
        print("Folding con dos dígitos, Tipo de sonda: {}, Factor de carga máximo: {}, Claves desplazadas: {}".format(probe.__name__, load_factor, displaced))

"""

import random

class HashTable:
    def __init__(self, size, probe):
        self.size = size                  # Tamaño de la tabla hash
        self.probe = probe                # Tipo de sonda utilizada (función de prueba)
        self.table = [None] * self.size   # Inicializar la tabla hash con valores nulos
        self.count = 0                    # Contador de elementos en la tabla hash

    def hash_function(self, key):
        return key % self.size             # Función hash básica que usa el módulo para determinar el índice

    def insert(self, key):
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None:
            hash_value = self.probe(hash_value)    # Utiliza la función de sonda para resolver colisiones
        self.table[hash_value] = key               # Inserta la clave en la tabla hash
        self.count += 1                            # Aumenta el contador de elementos en la tabla hash

    def search(self, key):
        hash_value = self.hash_function(key)
        while self.table[hash_value] is not None:
            if self.table[hash_value] == key:      # Busca la clave en la tabla hash
                return hash_value
            hash_value = self.probe(hash_value)
        return None

    def displaced_keys(self):
        displaced = 0
        for key in self.table:
            if key is not None and self.hash_function(key) != self.table.index(key):
                displaced += 1                      # Cuenta las claves desplazadas en la tabla hash
        return displaced

def linear_probe(index):
    return (index + 1) % ht.size                    # Función de sonda lineal

def quadratic_probe(index):
    return (index + 1 ** 2) % ht.size                # Función de sonda cuadrática

def double_hash_probe(index):
    return (index + hash(index)) % ht.size           # Función de sonda hash doble

# Funciones de plegado
def fold_three_digits(key):
    result = 0
    while key > 0:
        result += key % 1000  # se obtienen los tres últimos dígitos de la clave y se suman a result
        key //= 1000 # se descartan los tres últimos dígitos de la clave
    return result # se devuelve el resultado del plegamiento

def fold_two_digits(key):
    result = 0
    while key > 0:
        result += key % 100 # se obtienen los dos últimos dígitos de la clave y se suman a result
        key //= 100 # se descartan los dos últimos dígitos de la clave
    return result # se devuelve el resultado del plegamiento

def fold_k_digits(key, k):
    str_key = str(key) # se convierte la clave en una cadena de texto
    groups = [str_key[i:i+k] for i in range(0, len(str_key), k)] # se divide la cadena de texto en grupos de k dígitos
    folded = sum(int(group) for group in groups)  # se suman los valores de cada grupo
    return folded # se devuelve el resultado del plegamiento

# Genera 1000 enteros aleatorios de 10 dígitos
key_set = random.sample(range(10000000000), 1000)

# Inicializa los valores para el experimento
max_load_factors = [0.5, 0.7, 0.9]
probe_types = [linear_probe, quadratic_probe, double_hash_probe]

# Test folding with three digits
for load_factor in max_load_factors:
    for probe in probe_types:
        ht = HashTable(103, probe) # se crea una tabla hash con 103 espacios y el tipo de sonda especificado
        for i in range(int(103 * load_factor)):  # se insertan las claves correspondientes al factor de carga máximo
            key = fold_three_digits(key_set[i]) # se aplica plegamiento con tres dígitos a la clave correspondiente
            ht.insert(key) # se inserta la clave en la tabla hash
        displaced = ht.displaced_keys() # se obtiene la cantidad de claves desplazadas
        print("Folding con tres dígitos, Tipo de sonda: {}, Factor de carga máximo: {}, Claves desplazadas: {}".format(probe.__name__, load_factor, displaced))

# Test folding with two digits
for load_factor in max_load_factors:
    for probe in probe_types:
        ht = HashTable(103, probe)
        for i in range(int(103 * load_factor)):
            key = fold_two_digits(key_set[i])
            ht.insert(key)
        displaced = ht.displaced_keys()
        print("Folding con dos dígitos, Tipo de sonda: {}, Factor de carga máximo: {}, Claves desplazadas: {}".format(probe.__name__, load_factor, displaced))