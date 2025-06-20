import tkinter as tk

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.set(str(num1 + num2))
    except ValueError:
        resultado.set("Las entradas deben ser numericas")

def restar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.set(str(num1 - num2))
    except ValueError:
        resultado.set("Las entradas deben ser numericas")

def multiplicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.set(str(num1 * num2))
    except ValueError:
        resultado.set("Las entradas deben ser numericas")

def dividir():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        if num2 == 0:
            resultado.set(str("El divisor no puede ser 0"))
        else:
            resultado.set(str(num1 / num2))
    except ValueError:
        resultado.set("Las entradas deben ser numericas")


def borrar_campos():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.set("")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Basica")
ventana.geometry("500x150")
ventana.configure(bg="grey")

# Variables
resultado = tk.StringVar()

# Widgets
tk.Label(ventana, text="Primer numero", bg="lightblue").place(x=10, y=20)
entrada1 = tk.Entry(ventana, bg="white")
entrada1.place(x=130, y=20)

tk.Label(ventana, text="Segundo numero", bg="lightblue").place(x=10, y=50)
entrada2 = tk.Entry(ventana, bg="white")
entrada2.place(x=130, y=50)

tk.Button(ventana, text="Sumar", command=sumar).place(x=300, y=10)
tk.Button(ventana, text="Restar", command=restar).place(x=300, y=40)
tk.Button(ventana, text="Multiplicar", command=multiplicar).place(x=400, y=10)
tk.Button(ventana, text="Dividir", command=dividir).place(x=400, y=40)
tk.Button(ventana, text="Borrar", command=borrar_campos, bg="pink").place(x=350, y=80)

tk.Label(ventana, text="Resultado", bg="red").place(x=10, y=90)
tk.Entry(ventana, textvariable=resultado, bg="white", width=30).place(x=130, y=90)

ventana.mainloop()