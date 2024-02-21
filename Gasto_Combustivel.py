# Variaveis
modelo = ""
autonomia = 0
distancia_percorrida = 0
valor_combustivel = 0.0
total_gasto = 0.0
litros_usados = 0.0

# Inicio do sistema

print()
print("-----------------------------------------")
print("         CONSUMO DE COMBUSTÍVEL          ")
print("-----------------------------------------")
print()
modelo = input("Digite o modelo do veículo: " + modelo)
autonomia = int(input("Digite a autonomia do veículo: "))
distancia_percorrida = int(input("Digite a distância percorrida pelo veículo: "))
valor_combustivel = float(input("Digite o valor do combustível: "))

# Calculos
litros_usados = distancia_percorrida / autonomia
total_gasto = litros_usados * valor_combustivel

# Resultado
print()
print("-----------------------------------------")
print("               RESULTADO                 ")
print("-----------------------------------------")
print()
print("Modelo do veículo: " + modelo)
print("fAutonomia do veículo: {autonomia}" + " Km/L") 
print("fDistância percorrida: {distancia_percorrida}"  + " Km")
print("fValor do combustível: R${valor_combustivel}")
print()
print("-----------------------------------------")
print(f"Quantidade de combustível ultilizado: {litros_usados:.2f}" + "L")
print(f"Total gasto com a viagem: R${total_gasto:.2f}")
print("-----------------------------------------")
print()
