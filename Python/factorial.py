def n_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares
lista = [3, 8, 20, 13, 18, 9, 7, 50]
resultado = n_pares(lista)
print("Los numeros pares son:", resultado)
