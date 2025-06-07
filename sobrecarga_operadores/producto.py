class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        if isinstance (nombre, str):
            self.nombre = nombre
        else:
            self.nombre = "nombre no valido"
        if isinstance(precio, float) and precio >= 0:
            self.precio = precio
        else:
            self.precio = 0.0
        if isinstance(cantidad, int) and cantidad >= 0:
            self.cantidad = cantidad
        else:
            self.cantidad = 0
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Cantidad: {self.cantidad}"
    def __add__ (self,otra):
        if isinstance(otra, Producto) and self.nombre == otra.nombre:
            nueva_cantidad = self.cantidad + otra.cantidad
            return Producto(self.nombre, self.precio, nueva_cantidad)
    def __mul__(self, cantidad):
        if isinstance(cantidad, int) and cantidad >= 0:
            return self.precio * cantidad
    def __eq__(self, otro):
        return isinstance(otro, Producto) and self.nombre == otro.nombre and self.precio == otro.precio
    def __del__(self):
        print(f"Eliminando producto: {self.nombre}")