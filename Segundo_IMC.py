#  Programa De IMC
# Desenvolvido por Maria

print("************************************")
print("*         Calculadora IMC          *")
print("************************************")
print()

# Criação Das Variáveis
nome = ""
peso = 0
altura = 0.0
imc = 0.0

#Entrada dos Dados

nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# Processar os Valores Para Obter O IMC
imc = peso / altura ** 2

classificacao = ""

if imc < 18.5:
    classificacao = "O peso está a baixo do peso"
elif imc >= 18.5 and imc <= 24.9:
    classificacao = "O peso está Normal"
elif imc >= 25 and imc <= 29.9:
    classificacao = "O peso está em Sobrepeso"
elif imc >= 30 and imc <= 34.9:
    classificacao = "O peso está em Obesidade Grau I"
elif imc >= 35 and imc <= 39.9:
    classificacao = "O peso está em Obesidade Grau II"
elif imc >= 40:
    classificacao = "O peso está em Obesidade Grau III ou Mórbita"
else:
    classificacao = "Inválido."

# Saida do processamento
print()
print("************************************")
print("*            Resultado             *")
print("************************************")
print("*                                  *")
print("NOME: " + nome)
print("PESO: " + str(peso) + "Kg")
print("ALTURA: " + str(altura) + "m")
print("IMC: " + str(imc))
print(f"Situação: {classificacao}")
