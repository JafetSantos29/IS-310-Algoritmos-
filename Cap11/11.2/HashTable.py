import random

class HashTable:
    def __init__(self, size, probe):
        self.size = size
        self.probe = probe
        self.table = [None] * self.size
        self.count = 0

    def hash_function(self, key):
        #return hash_function_3(key, self.size) # change to hash_function_2 for the other function
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

    def hash_function_3(num, size):
        num_str = str(num)
        chunks = [num_str[i:i+3] for i in range(0, len(num_str), 3)]
        hash_val = sum([int(chunk) for chunk in chunks])
        return hash_val % size

    def hash_function_2(num, size):
        num_str = str(num)
        chunks = [num_str[i:i+2] for i in range(0, len(num_str), 2)]
        hash_val = sum([int(chunk) for chunk in chunks])
        return hash_val % size

def linear_probe(index):
    return (index + 1) % ht.size

def quadratic_probe(index):
    return (index + 1 ** 2) % ht.size

def double_hash_probe(index):
    return (index + hash(index)) % ht.size

# Inicializamos los valores para el experimento
max_load_factors = [0.5, 0.7, 0.9]
probe_types = [linear_probe, quadratic_probe, double_hash_probe]

# Generate 1000 random 10-digit integers
key_set = random.sample(range(1000000000), 1000)

for load_factor in max_load_factors:
    for probe in probe_types:
        ht = HashTable(103, probe)
        for i in range(int(103 * load_factor)):
            ht.insert(key_set[i])
        displaced = ht.displaced_keys()
        print("Tipo de sonda: {}, Factor de carga máximo: {}, Claves desplazadas: {}".format(probe.__name__, load_factor, displaced))
