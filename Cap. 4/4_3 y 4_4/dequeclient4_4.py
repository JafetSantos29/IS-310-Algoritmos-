"""from deque import *
# Crear una deque de capacidad 5
d = Deque(5)

# Insertar elementos en la deque
d.insertLeft(1)
d.insertLeft(2)
d.insertRight(3)
d.insertRight(4)

# Mostrar el contenido de la deque
print("Contenido de la deque:", end=" ")
while not d.isEmpty():
    print(d.removeLeft(), end=" ")
print()

# Insertar elementos en la deque nuevamente
d.insertLeft(5)
print("Primer elemento de la deque:", d.peekLeft())  # Agregando esta línea
d.insertRight(6)

# Mostrar el contenido de la deque nuevamente
print("Contenido de la deque:", end=" ")
while not d.isEmpty():
    print(d.removeRight(), end=" ")
print()"""

from deque4_3 import *

# Crear una deque de capacidad 5
d = Deque(5)

# Insertar elementos en la deque
d.insertLeft(1)
d.insertLeft(2)
d.insertRight(3)
d.insertRight(4)

# Mostrar el contenido de la deque original
print("Contenido original de la deque:", end=" ")
for i in range(d.left, d.right+1):
    print(d.items[i], end=" ")
print()

# Eliminar un elemento a la derecha y mostrar la deque actualizada
d.removeRight()
print("Contenido de la deque después de eliminar un elemento a la derecha:", end=" ")
for i in range(d.left, d.right+1):
    print(d.items[i], end=" ")
print()

# Eliminar un elemento a la izquierda y mostrar la deque actualizada
d.removeLeft()
print("Contenido de la deque después de eliminar un elemento a la izquierda:", end=" ")
for i in range(d.left, d.right+1):
    print(d.items[i], end=" ")
print()

# Insertar elementos en la deque nuevamente
d.insertLeft(5)
d.insertRight(6)

# Mostrar el contenido de la deque actualizada
print("Contenido de la deque después de insertar elementos:", end=" ")
for i in range(d.left, d.right+1):
    print(d.items[i], end=" ")
print()
