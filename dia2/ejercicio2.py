#la separacion de los float es un punto (.)
#la division entre integers, el resultado es un float

print(4/2) #2.0
print(5/2) #2.5
print(5/3.5)#1.4285714285714286
print(2.4*4)#9.6

nombre = "Mijail"
año = "2024"
print(3*nombre)#MijailMijailMijail
print(año*2)#20242024
#print(nombre/2)#no se puede dividir un string

# Interpolacion de cadenas(otra forma de imprimir) print(f" {nombre_variable}")
mes = 3
dia = 7

print(f"Hola {nombre}, El año es {año} del mes {mes} y el dia {dia} ")

#string.format
#print("".format())
print("Hola {}, El año es {} del mes {} y el dia {}".format(nombre,año,mes,dia))

#interpolacion con % (%s para string y %d para numeros)
print("Hola %s, El año es %s del mes %d y el dia %d" %(nombre, año, mes,dia))

#Metodo count -> busca y cuanta cuantas veces se encuentra un caracter en un string
print("Saitama".count("a"))
print(nombre.count("i"))
#Metodos upper-> todo el string a mayuscula y lower -> todo el string a miniscula
print("Saitama".upper())#SAITAMA
print("SaItAmA".lower())#saitama
print(nombre.upper())#MIJAIL
print(nombre.lower())#mijail
#Metodo title -> solo la primera "letra" a mayuscula
print("14564saItAmA".title())#14564Saitama

# len() -> contar los caracteres de una string
print(len(" israel palma 2024"))#18

#join -> unir string separados en un solo string
print(", ".join(["mijail","palma","loren"]))

#imprimir en mas de una linea (\n)
print("escribir\ncualquier\ncosas")
"""
escribir
cualquier
cosas
"""

