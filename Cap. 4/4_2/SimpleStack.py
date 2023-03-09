class Stack(object):
    def __init__(self, max):
        # Constructor
        self.__stackList = [None] * max  # La pila se almacena como una lista
        self.__top = -1  # No hay elementos inicialmente

    def push(self, item):
        # Agregar un elemento a la cima de la pila
        if self.__top >= len(self.__stackList) - 1:
             # Si la pila está llena, levantar una excepción personalizada
            raise Exception("La pila está llena")

        # Incrementar el puntero de la pila y agregar el elemento a la lista
        self.__top += 1  # Avanzar el puntero
        self.__stackList[self.__top] = item  # Almacenar el elemento

    def pop(self):
        # Extraer y devolver el elemento superior de la pila
        if self.__top < 0:
        # Si la pila está vacía, levantar una excepción personalizada
            raise Exception('La pila está vacía')

        # Eliminar el elemento superior de la pila
        top = self.__stackList[self.__top]  # Elemento superior
        # Eliminar la referencia al elemento
        self.__stackList[self.__top] = None
        self.__top -= 1  # Disminuir el puntero
        return top  # Devolver el elemento superior

    def peek(self):
        # Devolver el elemento superior
        if not self.isEmpty():  # Si la pila no está vacía
            # Devolver el elemento superior
            return self.__stackList[self.__top]

    def isEmpty(self):
        # Comprobar si la pila está vacía
        return self.__top < 0

    def isFull(self):
        # Comprobar si la pila está llena
        return self.__top >= len(self.__stackList) - 1

    def __len__(self):
        # Devolver el número de elementos en la pila
        return self.__top + 1

    def __str__(self):
        # Convertir la pila a una cadena
        ans = "["  # Empezar con el corchete izquierdo
        for i in range(self.__top + 1):  # Recorrer los elementos actuales
            if len(ans) > 1:  # Excepto después del corchete izquierdo, separar los elementos con una coma
                ans += ", "
            # Agregar la forma de cadena del elemento
            ans += str(self.__stackList[i])
        ans += "]"  # Cerrar con el corchete derecho
        return ans
