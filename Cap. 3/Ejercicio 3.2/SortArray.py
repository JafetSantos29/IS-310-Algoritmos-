class Array(object):
    # Implementa una estructura de datos de array ordenable
    def __init__(self, initialSize):
        # Constructor
        self.__a = [None] * initialSize # El array almacenado como una lista
        self.__nItems = 0 # No hay elementos en el array inicialmente

    def __len__(self):
        # Definición especial para len()
        return self.__nItems # Retorna el número de elementos

    def get(self, n):
        # Retorna el valor en el índice n
        if 0 <= n and n < self.__nItems: # Verifica si n está dentro de los límites
            return self.__a[n] # solo devuelve el elemento si está dentro de los límites

    def set(self, n, value):
        # Establece el valor en el índice n
        if 0 <= n and n < self.__nItems: # Verifica si n está dentro de los límites
            self.__a[n] = value # Solo establece el elemento si está dentro de los límites

    def swap(self, j, k):
        # Intercambia los valores en 2 índices
        if (0 <= j and j < self.__nItems and # Verifica si los índices están dentro de los límites
                0 <= k and k < self.__nItems):
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):
        # Inserta un elemento al final
        if self.__nItems >= len(self.__a): # Si el array está lleno,
            raise Exception("Array overflow") # lanza una excepción
        self.__a[self.__nItems] = item # El elemento va al final actual
        self.__nItems += 1 # Incrementa el número de elementos

    def find(self, item):
        # Encuentra el índice del elemento
        for j in range(self.__nItems): # Entre los elementos actuales
            if self.__a[j] == item: # Si se encuentra el elemento
                return j # entonces devuelve el índice del elemento
        return -1 # No se encontró, devuelve -1

    def search(self, item):
        # Busca el elemento y lo retorna si se encuentra
        return self.get(self.find(item))

    def delete(self, item):
        # Borra la primera ocurrencia del elemento
        for j in range(self.__nItems): # del elemento
            if self.__a[j] == item: # Si se encuentra el elemento
                self.__nItems -= 1 # Uno menos al final
                for k in range(j, self.__nItems): # Mueve los elementos desde la derecha a la izquierda
                    self.__a[k] = self.__a[k+1]
                return True # Retorna una bandera de éxito
        return False # Si llegó aquí, entonces no se encontró el elemento

    def traverse(self, function=print):
        # Recorre todos los elementos y aplica una función
        for j in range(self.__nItems): # y aplica una función
            function(self.__a[j])

    def __str__(self): # Función especial para str()
        ans = "[" # Encerrar en corchetes
        for i in range(self.__nItems): # Ciclo a través de los elementos
            if len(ans) > 1: # Excepto al lado izquierdo del corchete
                ans += ", " # Separar elementos con coma
            ans += str(self.__a[i]) # Agregar representación en string del elemento
        ans += "]" # Cerrar con corchete derecho
        return ans

    def bubbleSort(self):
    # Recorre la lista de elementos desde el final hacia el principio
        for last in range(self.__nItems-1, 0, -1):
            # Compara cada elemento adyacente y los intercambia si están en el orden incorrecto
            for inner in range(last):
                if self.__a[inner] > self.__a[inner+1]:
                    # Intercambia los elementos
                    self.swap(inner, inner+1)   # La lista está ahora ordenada

    def selectionSort(self): # Ordenar seleccionando el mínimo y moviéndolo a la izquierda
        for outer in range(self.__nItems-1): # El ciclo externo llega hasta el penúltimo
            min = outer # Suponer que el mínimo está en el lado izquierdo
            for inner in range(outer+1, self.__nItems): # Buscar hacia la derecha
                if self.__a[inner] < self.__a[min]: # Si encontramos un nuevo mínimo
                    min = inner # Actualizar el índice del mínimo
            # __a[min] es el más pequeño entre __a[outer]...__a[__nItems-1]
            self.swap(outer, min) # Intercambiar el más pequeño con el que está en la izquierda

    def insertionSort(self): # Ordenar insertando repetidamente
        for outer in range(1, self.__nItems): # Marcar un elemento
            temp = self.__a[outer] # Guardar el elemento marcado en temp
            inner = outer # El ciclo interno comienza en la marca
            while inner > 0 and temp < self.__a[inner-1]: # Si el elemento marcado es menor que el elemento anterior
                self.__a[inner] = self.__a[inner-1] # Desplazar el elemento a la derecha
                inner -= 1 # Actualizar el índice del ciclo interno
            self.__a[inner] = temp # Mover el elemento marcado al 'hueco'

    #Agrega el metodo mediana
    def median(self):
        middle_index = self.__nItems // 2  # Índice del elemento del medio.
        if self.__nItems % 2 == 0:  # Si el número de elementos es par.
            # Se suman los elementos del medio y se divide entre 2 para obtener su media.
            return sum(self.__a[middle_index - 1:middle_index + 1]) / 2
        else:  # Si el número de elementos es impar.
            # Se devuelve el elemento del medio.
            return self.__a[middle_index]