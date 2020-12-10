"""
    Ejemplo 01
    Ingreso de datos por teclado
"""
# Proceso para pedir el ingreso de información del usuario
nombre = input("Ingrese nombre del persona: ")
edad = int(input("Ingrese edad de persona: "))
sueldo = float(input("Ingrese el sueldo de la persona: "))

mensajeFinal = "Nombre:%s\nEdad:%d\nSueldo:%.2f\n" % (nombre,edad, sueldo)

print(mensajeFinal)
# print mensajeFinal # era valido en python2