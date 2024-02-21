#Variaveis
lado_a = ""
lado_b = ""
lado_c = ""

#Numero de lados
print()
print("+---------------------------------------------+")
lado_a = int(input("Digite o valor do lado A: "))
lado_b = int(input("Digite o valor do lado B: "))
lado_c = int(input("Digite o valor do lado C: "))
print("+---------------------------------------------+")
print()

#Calculo
triangulo = ""
if lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    triangulo = "ISÓSCELES"
elif not (lado_a != lado_b) or (lado_a != lado_c) or (lado_b != lado_c):
    triangulo = "ESCALENO"
elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
    triangulo = "EQUILÁTERO"
else:
    print("Inválido.")

#Resultado
print("+---------------------------------------------+")
print("|                 RESULTADO                   |")
print("+---------------------------------------------+")
print()
print(f"Esse triângulo é {triangulo}")
