import math

# Inputs
g = float(input('Ingrese la constante g: '))
r = float(input('Ingrese el radio en Kilómetros: '))*1000

# Cálculo de Velocidad de Escape
v_e = math.sqrt(2 * g * r)

# Output
print(f'La velocidad de escape es {v_e:.1f} m/s')
