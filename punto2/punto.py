ecuacion = lambda numero1, numero2: 1 if numero1 > numero2 else -1
numero=ecuacion(3,5)

resultado = lambda numero: print('El primer numero es mayor') if numero == 1 else print('El segundo numero es mayor')
resultado(numero)
