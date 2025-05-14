def numero_mayor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

respuesta = numero_mayor(5, 9, 3)
print("El numero mayor es:", respuesta)
