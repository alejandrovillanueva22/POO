password = "upbc2025"
intentos = 0
max_intentos = 3
while intentos < max_intentos:
    entrada = input ("Ingrese la contrasena: ")
    if entrada == password:
        print("Bienvenido!")
        break
    else: 
        intentos += 1
        print("Contrasena incorrecta. Intento ", intentos, "de ", max_intentos)
    if intentos == max_intentos: 
        print("Limite de intentos excedido. Sistema bloqueado.")
