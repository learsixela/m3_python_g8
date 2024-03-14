#Inputs
precio = int(input('Ingrese el Precio de Suscripción:\n>'))
usuarios_normal = int(input('Ingrese el Número de Usuarios Normales:\n>'))
usuarios_premium = int(input('Ingrese el Número de Usuarios Premium:\n>'))
gastos = int(input('Ingrese los Gastos Totales:\n>'))


#Cálculo utilidades
utilidades = precio * usuarios_normal + (1.5 * precio) * usuarios_premium - gastos

# Output
print(f'Las utilidades son {utilidades}')
