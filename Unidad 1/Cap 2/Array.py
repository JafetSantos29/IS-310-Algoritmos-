class Array(object):

 def __init__(self, initialSize): 
    self.__a = [None] * initialSize 
    self.__nItems = 0 
 def __len__(self): 

    return self.__nItems 
 def get(self, n): 

    if 0 <= n and n < self.__nItems: 

        return self.__a[n] 

 def set(self, n, value): 
    if 0 <= n and n < self.__nItems: 

        self.__a[n] = value 

 def insert(self, item): 
    self.__a[self.__nItems] = item 
    self.__nItems += 1 
    
 def find(self, item): 
    for j in range(self.__nItems):
         if self.__a[j] == item: 
            return j 
            return -1 
        
 def search(self, item): 
     return self.get(self.find(item))
 
 def delete(self, item): 
     for j in range(self.__nItems): 
        if self.__a[j] == item: 
         self.__nItems =-1 
         for k in range(j, self.__nItems):
            self.__a[k] = self.__a[k+1] 
        return True 
        return False 
    
 def traverse(self, function=print):
    for j in range(self.__nItems): 
        function(self.__a[j])

#Metodo del ejercicio 2.1

 def getMaxNum(self):
   a=(max(self.__a))
   return a
   
 #Metodo del ejercicio 2.2, 

 def deleteMaxNum(self):
   a=(max(self.__a))
   for j in range(self.__nItems): 
      if self.__a[j] == a: 
       self.__nItems -=1
       #self.__a[a]= self.__a.append(None)
       
       for k in range(j, self.__nItems):
         self.__a[k] = self.__a[k+1] 
      print("Numero max eliminado")           
      return True 
      return False  
   
 #ejercicio 2.3
 
 def deletOrdenados(self):
    unico = []
    for i in self.__a:
       if i not in unico:
          unico.append(i)
          unico.sort() 
    self.__a=unico
          
    self.deleteMaxNum()
    print("ordenados de forma acedente")      
   
 #ejercicio 2.4
 
 def removeDups(self):
    unico=[]
    for i in self.__a:
      if i not in unico :
         unico.append(i)
         
    print(unico)
    
    #ejercicio 2.5
    def merge(self, item): # Eliminar cualquier ocurrencia
        j = self.find(self.__key(item))  # Intenta encontrar el item
        if j < self.__nItems and self.__a[j] == item: # Si se encuentra,
            self.__nItems -= 1 # Uno menos al final
            for k in range(j, self.__nItems): # Mover elementos más grandes a la izquierda
                self.__a[k] = self.__a[k+1]
                return True # Devuelve el indicador de éxito
            return False # Hecho aquí; objeto no encontrado
    
   