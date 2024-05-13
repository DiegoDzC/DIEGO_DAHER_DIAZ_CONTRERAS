import math

def area_rectangulo():
    print("Area de un rectangulo")
    lado_a = float(input("Lado A del Rectangulo: "))
    lado_b = float(input("Lado B del Rectangulo: "))

    rectangulo = lado_a * lado_b

    print("El area del rectangulo es: ",rectangulo,"cm2")

def area_triangulo():
    print("Area de un triángulo")
    lado_a = float(input("Lado A del Triángulo: "))
    lado_b = float(input("Lado B del Triángulo: "))
    lado_c = float(input("Lado C del Triángulo: "))

    perimetro = (lado_a + lado_b + lado_c)/2
    triangulo = (math.sqrt(perimetro * (perimetro - lado_a) * (perimetro - lado_b) * (perimetro - lado_c)))
    print("El area del Triángulo es: ",triangulo,"cm2")


def area_circulo():
    print("Area de un circulo")
    diametro = float(input("Cuanto mide el diametro del circulo: "))
    radio = diametro / 2
    circulo = math.pi * (radio * radio)
    print("El area del circulo es: ",circulo,"cm2")

print("Calculo de areas")
print("Selecciona el area de la figura que deseas Area")
print("1 - Rectangulo")
print("2 - Triangulo")
print("3 - Circulo")

opcion = input("Opción: ")

if opcion == "1":
    area_rectangulo()
elif opcion == "2":
    area_triangulo()
elif opcion == "3":
    area_circulo()
else:
    print("Opción invalida. Por favor elije una opcion disponible.")