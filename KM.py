print("Cálculo de gasto!" + "\n")

gasolina = float(input("Qual valor da gasolina? "))
litro = float(input("Quantos KM seu carro faz com 1 litro? "))
percorreu = float(input("Quantos KM tem sua viagem ? "))
velocidade = float(input("Qual sua velocidade média? "))

media1 = percorreu / litro
print(f"Seu carro vai gastar:{media1:.2f} litro(s)")
media2 = media1 * gasolina
print(f"Você vai gastar: R${media2:.2f} reais")
divisao = percorreu / velocidade
print(f"Você vai levar: {divisao} horas/minutos!")
