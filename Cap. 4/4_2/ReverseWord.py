
from SimpleStack import *

stack = Stack(100) # Crear una pila para contener las letras
palabra = input("Palabra a invertir: ") #Pedir al usuario que ingrese una palabra para invertir

for let in palabra: # Recorrer las letras de la palabra ingresada
    if not stack.isFull(): # Agregar las letras a la pila si esta no está llena
        stack.push(let)

revertir = '' # Construir la versión invertida de la palabra

while not stack.isEmpty(): # Al ir sacando elementos de la pila hasta que esté vacía
    revertir += stack.pop()

print('El inverso de ', palabra, 'es', revertir) #Imprimir la palabra original y su versión invertida


clean_word = ''.join(e.lower() for e in palabra if e.isalpha()) #Eliminar caracteres no alfabéticos y convertir todo a minúsculas

for let in clean_word: # Agregar las letras limpias a la pila
    if not stack.isFull(): #Agregar letras a la pila si no está llena
        stack.push(let)

revertir = '' # "Construir la versión invertida"

while not stack.isEmpty(): # Al ir sacando elementos de la pila hasta que esté vacía
    revertir += stack.pop()

# Verificar si la palabra invertida es igual a la original
if clean_word == revertir:
    print(palabra, 'es un palíndromo.')
else:
    print(palabra, 'no es un palíndromo.')