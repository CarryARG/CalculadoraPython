print("Hola mundo")
a = 0
b = 0
c = 0
a = int(input("ingrese valor de a: "))
b = int(input("ingrese valor de b: "))
c = int(input("ingrese valor de c: "))
resolvente_positivo = ((-b) + ((b**2 - 4 * a * c) ** 1 / 2)) / (2 * a)
resolvente_negativo = ((-b) - ((b**2 - 4 * a * c) ** 1 / 2)) / (2 * a)
print("el valor de la resolvente positiva es: ", resolvente_positivo)
print("el valor de la resolvente negativa es: ", resolvente_negativo)
resto1 = a % 2
print("el resto de a es igual a: ", resto1)

resto2 = b % 2
print("el resto de b es igual a: ", resto2)


resultado = resto1 == resto2

if resultado is True:
    print("el resto de a y b son iguales")
elif resultado is False:
    print("el resto de a y b no son iguales")

# Calcularemos la hipotenusa
hipotenusa = (a**2 + b**2) ** (1 / 2)
print("la hipotenusa de esos dos valores es igual a: {:.2f}".format(hipotenusa))
