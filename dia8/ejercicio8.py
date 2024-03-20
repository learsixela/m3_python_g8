#for each
""" 
for variable in iterable:
"""

#funcion range(), el ultimo numero no es considerado
#valor de inicio por default es el cero [0-10[
for i in range(10):
    print(i)#0,1,2,3,4,5,6,7,8,9
    
print("-------------------------")
# se establece el valor de inicio [4-10[
for i in range(4,10):
    print(i) #4,5,6,7,8,9
    
print("-------------------------")

# el tercer valor corresponde a la frecuencia [4-10[
for i in range(4,10,4):
    print(i) #4,6,8
    
print("-------- ejercicio-----------------")
for i in range(0,21,2):
    print(i)

print("---------Leik----------------")    
for i in range(1,21,2):
    print(i+1)
    
print("\n")
for num in range(1, 21): 
    if num % 2 == 0: 
        print(num)

print("---------Sebastian----------------") 
contador = 1
while contador <= 20:
    if contador% 2 == 0: 
        print(contador)
    contador+=1
    
contador = 0
while contador <= 20:
    print(contador)
    contador+=2
    
    
""" LISTAS ITERABLES"""
# lista: conjunto de datos, ordenados segun su ingreso, separados por coma, 
# el primer elemento, esta en la posicion cero
#tamaño de la lista, es la cantidad de elementos
#lista.append(elemento) -> agregar el elemento al final de la lista
lista = [1,5,8,3,4]
print("---------listas----------------") 
for elemento in lista:#elemento= 4
    print(elemento)
    
print("---------string----------------") 
#String -> objeto 
texto = "Hola mundo!!"
for caracter in texto:
    print(caracter)


opciones = ['piedra','papel','tijeras']

for opcion in opciones:
    print(opcion)
    
"""
DICCIONARIO { clave: valor,}
no existen la posiciones
"""

diccionario = {
    "Nombre": "Carlos",
    "Apellido": "Santana",
    "Ocupacion": "Guitarrista"
}

print("---------diccionario----------------") 

for clave in diccionario:
    print(clave)
print("") 
for clave in diccionario:
    print(f"clave {clave} - valor {diccionario[clave]}")
    
print("")    
for valor in diccionario.values():
    print(f" el valor es {valor}")
    
print("") 
for clave, valor in diccionario.items():
    print(f"clave {clave} - valor {valor}")

print("")
for numero1 in range(11):
    print(f'\nTabla del {numero1}:------------------------------\n')
    for numero2 in range(1,11):
        print(f"{numero1} * {numero2} = {numero1*numero2}")

#for (let index = 0; index < 10; index++) {
#    console.log(index)
#}

for index in range(0,10,1):
    print(index)