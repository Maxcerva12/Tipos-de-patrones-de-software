class State:
    def encender(self):
        pass
    def apagar(self):
        pass

class Encendida(State):
    def encender(self):
        return self
    
    def apagar(self):
        print("\n==========Desactivando=============")
        print("Apagando la Lampara")
        return Apagada()

class Apagada(State):
    def encender(self):
        print("\n==========Activando=============")
        print("Encendiendo la Lampara")
        return Encendida()
    def apagar(self):
        return self
        
class Lampara:
    def __init__(self):
        self.estado = Apagada()
        self.nombre_estado = "Apagada"
        
    def cambiar_estado(self):
        #isinstance()  es una función que verifica si un objeto es una instancia de una clase específica. 
        if isinstance(self.estado, Encendida):
            print("La Lampara ya está encendida")
        elif isinstance(self.estado, Apagada):
            print("La Lampara ya está apagada")
        else:
            self.estado = self.estado.apagar()
            self.nombre_estado = "Apagada"
        self.mostrar_estado()
            
    def mostrar_estado(self):
        print(f"El estado actual de la Lampara es: {self.nombre_estado}")
        print("=======================")

class Control:
    def __init__(self):
        self.lampara = Lampara()
    def menu(self):
        print("\n Sistema del control de la Lampara ")
        print("=====================================")
        print("1. Encender la bombilla")
        print("2. Apagar la bombilla")
        print("3. Salir")
    def ejecutar(self, opcion):
        if opcion == 1:
            self.lampara.estado = self.lampara.estado.encender()
            self.lampara.nombre_estado = "Encendida"
        elif opcion == 2:
            self.lampara.estado = self.lampara.estado.apagar()
            self.lampara.nombre_estado = "Apagada"
        elif opcion == 3:
            print("Saliendo del sistema de control 🎚️")
            exit()
        else:
            print("Opción inválida")

control = Control()
while True:
    control.menu()
    opcion = int(input("Ingrese una opción: "))
    control.ejecutar(opcion)
    control.lampara.mostrar_estado()

    