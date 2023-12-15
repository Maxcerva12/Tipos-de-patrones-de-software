from abc import ABC

#define una clase llamada  Figura  que hereda de la clase base abstracta  ABC 
class Figura(ABC): 
    def calcular_area(self):
        pass

class Triangulo(Figura):
    def calcular_area(self):
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = (base * altura) / 2
        print("El área del triángulo es:", round(area))

class Cuadrado(Figura):
    def calcular_area(self):
        a = float(input("Ingresa uno de los lados del cuadrado:"))
        area = a * a
        print("El área del cuadrado es:", round(area))

class Rectangulo(Figura):
    def calcular_area(self):
        base = float(input("Ingresa la base del rectangulo:"))
        altura = float(input("Ingresa la altura del rectangulo:"))
        area = base * altura
        print("El área del rectángulo es:", round(area))

class Circulo(Figura):
    def calcular_area(self):
        r = float(input("Ingresa el radio del círculo:"))
        area = 3.1416 * (r * r)
        print("El área del círculo es:", round(area))

class Salir(Figura):
    def calcular_area(self):
        print("Le agradecemos por utilizar nuestro medidor de Area📊")

class Accion_A_realizar:
    def __init__(self):
        self.opciones = {
            1: Triangulo(),
            2: Cuadrado(),
            3: Rectangulo(),
            4: Circulo(),
            5: Salir()
        }

    def ejecutar_opcion(self, opcion):
        if opcion in self.opciones:
            self.opciones[opcion].calcular_area()
        else:
            print("\nOpción inválida. Por favor, elige una opción válida.")
            print("=======================================================")

ejecutar = True
if ejecutar:
    contexto = Accion_A_realizar()
    opcion = 0

    while opcion != 5:
        print("\nElige una opción:")
        print("1 = Área del triángulo")
        print("2 = Área del cuadrado")
        print("3 = Área del rectángulo")
        print("4 = Área del círculo")
        print("5 = Salir")
        opcion = int(input("Ingrese Alguna opcion a realizar: "))

        contexto.ejecutar_opcion(opcion)