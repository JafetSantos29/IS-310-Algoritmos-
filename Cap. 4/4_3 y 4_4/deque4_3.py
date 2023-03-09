class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.size = 0
        self.left = 0
        self.right = -1
    
    def insertLeft(self, item):
        """Inserta un elemento en el lado izquierdo de la deque."""
        if self.isFull():
            raise Exception("Deque esta llena")
        self.left -= 1
        self.items[self.left] = item
        self.size += 1
    
    def insertRight(self, item):
        """Inserta un elemento en el lado derecho de la deque."""
        if self.isFull():
            raise Exception("Deque esta llena")
        self.right += 1
        self.items[self.right] = item
        self.size += 1
    
    def removeLeft(self):
        """Elimina y devuelve el elemento en el lado izquierdo de la deque."""
        if self.isEmpty():
            raise Exception("Deque esta vacia")
        item = self.items[self.left]
        self.left += 1
        self.size -= 1
        return item
    
    def removeRight(self):
        """Elimina y devuelve el elemento en el lado derecho de la deque."""
        if self.isEmpty():
            raise Exception("Deque esta vacia")
        item = self.items[self.right]
        self.right -= 1
        self.size -= 1
        return item
    
    def peekLeft(self):
        """Devuelve el elemento en el lado izquierdo de la deque sin eliminarlo."""
        if self.isEmpty():
            raise Exception("Deque esta vacia")
        return self.items[self.left]
    
    def peekRight(self):
        """Devuelve el elemento en el lado derecho de la deque sin eliminarlo."""
        if self.isEmpty():
            raise Exception("Deque esta vacia")
        return self.items[self.right]
    
    def isEmpty(self):
        """Devuelve True si la deque está vacía, False en caso contrario."""
        return self.size == 0
    
    def isFull(self):
        """Devuelve True si la deque está llena, False en caso contrario."""
        return self.size == self.capacity
