class Empleado: #crear clase
    def __init__ (self, nombre, salario): #atributos
        self.nombre = nombre
        self.salario = salario
        if isinstance (nombre, str): #verificacion de tipos
            self.nombre = nombre
        else:
            self.nombre = "nombre no valido"
        if isinstance(salario, float) and salario >= 0:
            self.salario = salario
        else:
            self.salario = 420.00
    def mostrar_info (self): #metodo
        print (f" {self.nombre}, {self.salario}") 

class Gerente (Empleado): #crear calse con herencia
    def __init__ (self, nombre, salario, departamento): #agregar atributo adicional
        super().__init__ (nombre, salario) #herencia de atributos
        self.departamento = departamento #nuevo atributo
        if isinstance (departamento, str): #verificacion de tipos
            self.departamento = departamento
        else:
            self.departamento = "Departamento no valido"
    def mostrar_info (self):
        super().mostrar_info() #sobre escribir mostrar info
        print(f"Departamento: {self.departamento}") #imprimir nueva info

class Tecnico (Empleado): #crear calse con herencia
    def __init__ (self, nombre, salario, especialidad): #agregar atributo adicional
        super().__init__ (nombre, salario) #herencia de atributos
        self.especialidad = especialidad#nuevo atributo
        if isinstance (especialidad, str): #verificacion de tipos
            self.especialidad = especialidad
        else:
            self.especialidad = "Especialidad no valida"
    def mostrar_info (self):
        super().mostrar_info() #sobre escribir mostrar info
        print(f"Especialidad: {self.especialidad}") #imprimir nueva info