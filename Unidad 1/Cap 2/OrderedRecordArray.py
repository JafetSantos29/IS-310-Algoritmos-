# Implementar una estructura de matriz ordenada de registros
def identity(x): # La función identidad
    return x
class OrderedRecordArray(object):
    #Este se modifica con el ejercicio 2.5
    """def __init__(self, initialSize, key=identity): # Constructor
        self.__a = [None] * initialSize #  La matriz almacenada como una lista
        self.__nItems = 0 # No hay elementos en la matriz inicialmente
        self.__key = key # La función de tecla obtiene la clave de registro"""
    
    def __len__(self):  # Definición especial para la función len()
        return self.__nItems  # Número de devolución de artículos

    def get(self, n): # Devuelve el valor en el índice n
        if n >= 0 and n < self.__nItems:  # Comprobar si n está dentro de los límites, y
            return self.__a[n] # solo devolver el elemento si está dentro de los límites
        raise IndexError("Index " + str(n) + " is out of range")
    
    def traverse(self, function=print): # Recorrer todos los elementos
        for j in range(self.__nItems):  # y aplicar una función 
           function(self.__a[j])
            
    def __str__(self): # Definición especial para str() func 
        ans = "["  # Rodeado por corchetes
        for i in range(self.__nItems): # Pasar por los elementos
            if len(ans) > 1:# Excepto al lado del corchete izquierdo,
                ans += ", " # elementos separados con coma
            ans += str(self.__a[i]) # Agregar forma de cadena del elemento
        ans += "]" # Cerrar con corchete derecho
        return ans

    def find(self, key): # Encuentra el índice en o justo debajo de ke
        lo = 0 # en lista ordenada
        hi = self.__nItems-1 # Buscar entre lo y hi
        while lo <= hi:
            mid = (lo + hi) // 2 # Selecciona el punto medio
            if self.__key(self.__a[mid]) == key: # ¿Lo encontramos?
                return mid # Ubicación de devolución del artículo
            elif self.__key(self.__a[mid]) < key: # ¿Está key en la mitad superior?
                lo = mid + 1 # Sí, eleva el límite lo
            else:
                hi = mid - 1 # No, pero podría estar en la mitad inferior
                return lo # Elemento no encontrado, devuelve el punto de inserción en su lugar
        
    def search(self, key):
        idx = self.find(key) # Busca un registro por su clave
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx] # y devolver el artículo si lo encuentra
    
    def insert(self, item): # Insertar elemento en la posición correcta
        if self.__nItems >= len(self.__a): # Si la matriz está llena,
            raise Exception("Array overflow") # generar excepción
        j = self.find(self.__key(item)) # Encuentra dónde debe ir el elemento
        for k in range(self.__nItems, j, -1): # Mover elementos más grandes a la derecha
            self.__a[k] = self.__a[k-1]
            self.__a[j] = item # Insertar el artículo
            self.__nItems += 1 # Incrementa el número de elementos
    
    def delete(self, item): # Eliminar cualquier ocurrencia
        j = self.find(self.__key(item))  # Intenta encontrar el item
        if j < self.__nItems and self.__a[j] == item: # Si se encuentra,
            self.__nItems -= 1 # Uno menos al final
            for k in range(j, self.__nItems): # Mover elementos más grandes a la izquierda
                self.__a[k] = self.__a[k+1]
                return True # Devuelve el indicador de éxito
            return False # Hecho aquí; objeto no encontrado
        
    #Ejercicio 2.5
    def __init__(self, key_func, records):
        self.key_func = key_func
        self.records = sorted(records, key=key_func)

    def merge(self, other):
        if self.key_func != other.key_func:
            raise ValueError("Cannot merge arrays with different key functions")
        # Create a new list big enough to hold the current list and the merging list
        merged_records = [None] * (len(self.records) + len(other.records))
        i = j = k = 0
        while i < len(self.records) and j < len(other.records):
            if self.key_func(self.records[i]) < self.key_func(other.records[j]):
                merged_records[k] = self.records[i]
                i += 1
            else:
                merged_records[k] = other.records[j]
                j += 1
            k += 1
        # Copy remaining elements of the current list
        while i < len(self.records):
            merged_records[k] = self.records[i]
            i += 1
            k += 1

        # Copy remaining elements of the merging list
        while j < len(other.records):
            merged_records[k] = other.records[j]
            j += 1
            k += 1

        self.records = merged_records
        
        #Ejercico 2.6
    def __init__(self, key_func, records):
        self.key_func = key_func
        self.records = sorted(records, key=key_func)

    def delete(self, item):
        index = None
        for i, record in enumerate(self.records):
            if self.key_func(record) == item:
                index = i
                break
            if index is not None:
                self.records = self.records[:index] + self.records[index+1:]
                
                #Ejercicio 2.7    
    def __init__(self, key_func, records, max_size=10, grow_factor=1.5):
        self.key_func = key_func
        self.records = sorted(records, key=key_func)
        self.max_size = max_size
        self.grow_factor = grow_factor

    def insert(self, record):
        if len(self.records) == self.max_size:
            self.max_size = int(self.max_size * self.grow_factor)
            self.records = self.records + [None] * (self.max_size - len(self.records))
            self.records[len(self.records)] = record
            self.records = sorted(self.records, key=self.key_func)
