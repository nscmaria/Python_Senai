# Média Final
print("*****************************")
print("*       Média Final         *")
print("*****************************")
print()

# Variáveis
nome = ""
nota_1 = 0.0
nota_2 = 0.0
nota_3 = 0.0
nota_4 = 0.0
media = 0.0

# Dados
nome = input("Digite o nome do aluno: ")
nota_um = float(input("Digite a nota do Bimestre 1: " ))
nota_dois = float(input("Digite a nota do Bimestre 2: " ))
nota_tres = float(input("Digite a nota do Bimestre 3: " ))
nota_quatro = float(input("Digite a nota do Bimestre 4: " ))

# Calculo
media = (nota_um + nota_dois + nota_tres + nota_quatro) / 4

#Aprovado ou Reprovado
situacao = ""
if media >= 7.0:
    situacao = "APROVADO"
elif media < 5:
    situacao = "REPROVADO"
else:
    situacao = "para a RECUPERAÇÃO"

# Saida da nota
print()
print("*************************************")
print("        Resultado da Média          *")
print("*************************************")
print("*                                   *")

print(f"{nome}, você foi {situacao}, sua nota final é {media}")
