n = int(input("Quantas pessoas? "))

jogadores = {}
for i in range(n):
    nome = input("Nome do jogador: ")
    pontos = main()
    jogadores[nome] = pontos
    print(nome, "fez", pontos, "pontos")

for i in jogadores:
    # printa o capeão
    if jogadores[i] == max(jogadores.values()):
        print(f"{i} é o campeão! com {jogadores[i]} pontos")
a