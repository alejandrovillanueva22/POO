from empleado import Empleado, Gerente, Tecnico
e1 = Empleado("Rich", 15000.00) #asignar empleado
g1 = Gerente("Carlos", 30000.00, "Marketing")#asignar gerente
t1 = Tecnico("Jesus", 20000.00, "Automotriz")#asignar tecnico

e1.mostrar_info()
g1.mostrar_info()
t1.mostrar_info()