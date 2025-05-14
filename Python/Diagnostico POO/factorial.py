def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n - 1)
num = int(input("Ingresa un número entero no negativo: "))
if num >= 0:
    print("El factorial de", num, "es:", factorial(num))
else:
    print("Debes ingresar un número no negativo.")
