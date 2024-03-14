#Inputs
precio = int(input('Ingrese el Precio de Suscripción:\n>'))
usuarios = int(input('Ingrese el Número de Usuarios:\n>'))
gastos = int(input('Ingrese los Gastos Totales:\n>'))

#advertir que u_anterior debe ser distinto de cero
u_anterior = int(input('Ingrese las utilidades anteriores. Este valor debe ser distinto de 0:\n>'))

#Cálculo utilidades
utilidades = precio * usuarios - gastos
#Razón
ratio = utilidades / u_anterior

# Output
print(f'Las utilidades son: {utilidades}' )
print(f'La razón de utilidades es de un: {ratio:.2f}%')
