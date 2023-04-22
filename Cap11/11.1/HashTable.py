import random

class HashTable:
    def __init__(self):
        self.size = 128  # inicialización con tamaño de 128
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.max_load_factor = 0.7

    def __growTable(self):
        # Duplicar tamaño de la tabla
        self.size *= 2
        new_keys = [None] * self.size
        new_values = [None] * self.size

        # Volver a hashear todas las llaves en la nueva matriz de hash
        for i in range(len(self.keys)):
            if self.keys[i] is not None:
                new_index = hash(self.keys[i]) % self.size
                while new_keys[new_index] is not None:
                    new_index = (new_index + 1) % self.size
                new_keys[new_index] = self.keys[i]
                new_values[new_index] = self.values[i]

        self.keys = new_keys
        self.values = new_values

    def insert(self, key, value):
        # Verificar si necesitamos redimensionar la tabla
        if self.__loadFactor() > self.max_load_factor:
            self.__growTable()

        # Insertar la llave en la tabla
        index = hash(key) % self.size
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def __loadFactor(self):
        return sum(1 for key in self.keys if key is not None) / float(self.size)
    
def test_hash_table():
    # Definimos las claves a insertar en la tabla hash
    keys = [random.randint(0, 1000000) for _ in range(200)]

    # Creamos una instancia de la tabla hash con un tamaño inicial de 128
    ht = HashTable(128)

    # Insertamos todas las claves en la tabla hash
    for key in keys:
        ht.insert(key, "value")

    # Imprimimos el número de desplazamientos para cada esquema de sonda y factor de carga
    for scheme in ["linear", "quadratic", "double"]:
        for load_factor in [0.5, 0.7, 0.9]:
            try:
                ht.set_probing_scheme(scheme)
                ht.set_load_factor(load_factor)
                for key in keys:
                    ht.find(key)
                print(f"{scheme} scheme with {load_factor} load factor: {ht.total_displacements} displacements")
            except Exception as e:
                print(f"Exception occurred for {scheme} scheme with {load_factor} load factor: {e}")

test_hash_table()
