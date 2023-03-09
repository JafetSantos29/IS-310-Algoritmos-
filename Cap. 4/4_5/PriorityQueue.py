#eliminación rápida del elemento de mayor prioridad pero una inserción lenta de elementos nuevos
"""# Implementar una estructura de datos de cola de prioridad usando una lista de Python
def identity(x): return x # Función identidad
class PriorityQueue(object):
    def __init__(self, size, pri=identity): # Constructor
        self.__maxSize = size # Tamaño de la cola
        self.__que = [None] * size # Cola almacenada como una lista
        self.__pri = pri # Función para obtener la prioridad del elemento
        self.__nItems = 0 # no hay elementos en la cola

    def insert(self, item): # Insertar un elemento en la cola de prioridad si no está llena
        if self.isFull():
            raise Exception("Queue overflow") #desbordamiento de cola
        j = self.__nItems - 1 # Empezar desde el frente
        while j >= 0 and ( # Buscar el lugar por prioridad
            self.__pri(item) >= self.__pri(self.__que[j])
        ):
            self.__que[j+1] = self.__que[j] # Desplazar elementos al frente
            j -= 1 # Paso hacia la parte posterior
        self.__que[j+1] = item # Insertar el nuevo elemento al final
        self.__nItems += 1
        return True

    def remove(self): # Devolver el elemento del frente de la cola de prioridad, si no está vacía, y removerlo
        if self.isEmpty():
            raise Exception("Queue underflow") #subdesbordamiento de la cola
        self.__nItems -= 1 # Un elemento menos en la cola
        front = self.__que[self.__nItems] # Almacenar el elemento del frente
        self.__que[self.__nItems] = None # Remover la referencia al elemento
        return front

    def peek(self): # Devolver el elemento del frente
        return None if self.isEmpty() else self.__que[self.__nItems-1]

    def isEmpty(self): # Devolver verdadero si la cola está vacía
        return self.__nItems == 0

    def isFull(self): # Devolver verdadero si la cola está llena
        return self.__nItems == self.__maxSize

    def __len__(self): # Devolver el número de elementos en la cola
        return self.__nItems

    def __str__(self): # Convertir la cola de prioridad a una cadena de caracteres
        ans = "[" # Empezar con el corchete izquierdo
        for i in range(self.__nItems-1, -1, -1): # Loop desde el frente
            if len(ans) > 1: # Excepto el próximo al corchete izquierdo, separar los elementos con coma
                ans += ", "
            ans += str(self.__que[i]) # Agregar la forma de cadena del elemento
        ans += "]" # Cerrar con el corchete derecho
        return ans
"""

#tiempo de inserción rápido, O(1), pero una eliminación más lenta del elemento de mayor prioridad.
def identity(x): return x
class PriorityQueue: 
    def __init__(self, size): # Método constructor
        self.__maxSize = size # Tamaño máximo de la cola de prioridad
        self.__que = [None] * size # Cola almacenada como una lista
        self.__nItems = 0 # Contador de elementos en la cola inicializado en cero

    # Método para insertar un elemento en la cola de prioridad
    def insert(self, item):
        # Verificar si la cola de prioridad está llena
        if self.isFull():
            raise Exception("Queue overflow")
        # Insertar el nuevo elemento en la cola de prioridad
        self.__que[self.__nItems] = item
        # Incrementar el contador de elementos en la cola de prioridad
        self.__nItems += 1
        return True

    # Método para remover el elemento de mayor prioridad de la cola de prioridad
    def remove(self):
        # Verificar si la cola de prioridad está vacía
        if self.isEmpty():
            raise Exception("Queue underflow")
        # Encontrar el índice del elemento de mayor prioridad
        maxIndex = 0
        for i in range(1, self.__nItems):
            if self.__que[i] > self.__que[maxIndex]:
                maxIndex = i
        # Guardar el elemento de mayor prioridad
        front = self.__que[maxIndex]
        # Desplazar los elementos hacia atrás
        for i in range(maxIndex+1, self.__nItems):
            self.__que[i-1] = self.__que[i]
        # Disminuir el contador de elementos en la cola de prioridad
        self.__nItems -= 1
        # Retornar el elemento de mayor prioridad
        return front

    # Método para obtener el elemento de mayor prioridad sin removerlo
    def peek(self):
        return None if self.isEmpty() else self.__que[self.__nItems-1]

    # Método para verificar si la cola de prioridad está vacía
    def isEmpty(self):
        return self.__nItems == 0

    # Método para verificar si la cola de prioridad está llena
    def isFull(self):
        return self.__nItems == self.__maxSize

    # Método para obtener el número de elementos en la cola de prioridad
    def __len__(self):
        return self.__nItems

    # Método para convertir la cola de prioridad a una cadena de caracteres
    def __str__(self):
        ans = "["
        for i in range(self.__nItems-1, -1, -1):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__que[i])
        ans += "]"
        return ans
