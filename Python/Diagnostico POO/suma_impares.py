n = int(input("Ingresa un numero entero positivo: "))
suma = 0
for i in range (1, n +1):
    if i % 2 != 0:
        suma += i
print("La suma de los numeros imprares de 1 a ", n, "es: ", suma)       