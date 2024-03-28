def sumar(x,y):
    """Realiza la impresion de la suma de dos numeros

    Args:
        x (int): primer numero
        y (int): segundo numero
    """
    print(f"El resultado de la suma es {x + y}")
    
if (__name__ == '__main__'):
    x = int(input("Ingrese el primer número: "))
    y = int(input("Ingrese el segundo número: "))
    print("Llamado el metodo sumar()")
    sumar(x, y)
    