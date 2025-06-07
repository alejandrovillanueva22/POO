from producto import Producto

p1 = Producto("Laptop", 12000.00, 5)
p2 = Producto("Laptop", 12000.00, 3)
p3 = Producto("Mouse", 200.00, 2)

print(p1)  
print(p2) 
print(p3)  


p4 = p1 + p2
print(p4) 


print(p3 * 3)  


print(p1 == p2) 
print(p1 == p3)  

# Eliminar productos
del p1
del p2
del p3
del p4
