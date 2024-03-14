#Inputs
precio = int(input('Ingrese el Precio de Suscripción:\n>'))
usuarios = int(input('Ingrese el Número de Usuarios:\n>'))
gastos = int(input('Ingrese los Gastos Totales:\n>'))

#Cálculo utilidades
utilidades = precio * usuarios - gastos

# Output
print(f'Las utilidades son {utilidades}')
