from SimpleStack import *

# Crear una pila con una capacidad máxima de 10 elementos
stack = Stack(6)

# Agregar cada palabra de la lista a la pila
for word in ['May', 'the', 'force', 'be', 'with', 'you', "too"]:
    stack.push(word)

# Imprimir el número de palabras en la pila y los elementos en la pila
print('Después de agregar', len(stack),
      'palabras en la pila, contiene:\n', stack)

try:
    # Tratar de agregar un elemento adicional a la pila
    stack.push('be')
except Exception as e:
    print(e)

# Comprobar si la pila está llena
print('¿Está la pila llena?', stack.isFull())



# Sacar los elementos de la pila uno por uno y mostrarlos
print('Sacando elementos de la pila:')
while not stack.isEmpty():
    print(stack.pop(), end=' ')
print()

