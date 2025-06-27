import tkinter as tk
from tkinter import Entry
from PIL import Image, ImageTk

# Ventana principal
ventana = tk.Tk()
ventana.title("SOPhyy - Login")
ventana.geometry("1440x1024")
ventana.configure(bg="#CB6CE6")  # fondo morado

# Marco blanco central
fondo_login_img = Image.open("fondo_login.png").resize((500, 500))
fondo_login = ImageTk.PhotoImage(fondo_login_img)
fondo_label = tk.Label(ventana, image=fondo_login, bg="#CB6CE6", bd=0)
fondo_label.place(relx=0.5, rely=0.5, anchor="center")

# Logo imagen
imagen_logo = Image.open("Logo_login.png").resize((400, 200))
logo = ImageTk.PhotoImage(imagen_logo)
logo_label = tk.Label(ventana, image=logo, bg="white")
logo_label.place(x=500, y=150)

# Ícono usuario
usuario_icon = ImageTk.PhotoImage(Image.open("user_login.png").resize((50, 50)))
tk.Label(ventana, image=usuario_icon, bg="white").place(x=460, y=355)

# Entrada usuario 
frame_usuario = tk.Frame(ventana, bg="black", width=300, height=40)
frame_usuario.place(x=530, y=355)
entrada_usuario = Entry(frame_usuario, font=("Arial", 12), bd=0, relief="flat", fg="gray")
entrada_usuario.insert(0, "Usuario")
entrada_usuario.place(x=2, y=2, width=296, height=36)

# Ícono contraseña
clave_icon = ImageTk.PhotoImage(Image.open("password_login.png").resize((50, 50)))
tk.Label(ventana, image=clave_icon, bg="white").place(x=460, y=420)

# Entrada contraseña 
frame_clave = tk.Frame(ventana, bg="black", width=300, height=40)
frame_clave.place(x=530, y=420)
entrada_clave = Entry(frame_clave, font=("Arial", 12), bd=0, relief="flat", fg="gray", show="*")
entrada_clave.insert(0, "Contraseña")
entrada_clave.place(x=2, y=2, width=296, height=36)

# Botón Entrar como imagen
boton_img = Image.open("Button_Entrar.png").resize((150, 60))
boton_img_tk = ImageTk.PhotoImage(boton_img)
boton = tk.Button(ventana, image=boton_img_tk, bd=0, relief="flat", cursor="hand2",
                  bg="white", activebackground="white",
                  command=lambda: print("Botón Entrar presionado"))
boton.place(x=600, y=510)

ventana.mainloop()