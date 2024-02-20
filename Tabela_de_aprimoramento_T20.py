from tabulate import tabulate

lista_aumento = [300, 3000, 9000, 18000]
lista_cd = [5, 10, 15, 20]

dados = [
    ["Arma", "Preço (T$)", "Simples ou Complexo?"],
    ["Adaga", 2, "Simples"],
    ["Espada Curta", 10, "Simples"],
    ["Foice", 4, "Simples"],
    ["Clava", 0, "Simples"],
    ["Lança", 2, "Simples"],
    ["Maça", 12, "Simples"],
    ["Bordão", 0, "Simples"],
    ["Pique", 2, "Simples"],
    ["Azagaia", 1, "Simples"],
    ["Besta Leve", 35, "Simples"],
    ["Funda", 0, "Simples"],
    ["Arco Curto", 30, "Simples"],
    ["Machadinha", 6, "Complexo"],
    ["Cimitarra", 15, "Complexo"],
    ["Espada Longa", 15, "Complexo"],
    ["Florete", 20, "Complexo"],
    ["Machado de Batalha", 10, "Complexo"],
    ["Mangual", 8, "Complexo"],
    ["Martelo de Guerra", 12, "Complexo"],
    ["Picareta", 8, "Complexo"],
    ["Tridente", 15, "Complexo"],
    ["Alabarda", 10, "Complexo"],
    ["Alfange", 75, "Complexo"],
    ["Gadanho", 18, "Complexo"],
    ["Lança Montada", 10, "Complexo"],
    ["Machado de Guerra", 20, "Complexo"],
    ["Montante", 50, "Complexo"],
    ["Arco Longo", 100, "Complexo"],
    ["Besta Pesada", 50, "Complexo"],
    ["Chicote", 2, "Complexo"],
    ["Espada Bastarda", 35, "Complexo"],
    ["Katana", 100, "Complexo"],
    ["Machado Anão", 30, "Complexo"],
    ["Corrente de espinhos", 25, "Complexo"],
    ["Machado Táurico", 50, "Complexo"],
    ["Rede", 20, "Complexo"],
    ["Pistola", 250, "Complexo"],
    ["Mosquete", 500, "Complexo"],
]

tabela = tabulate(dados, headers="firstrow", tablefmt="rounded_grid")
print(tabela)
seg = str(input("Podemos seguir ou quer continuar olhando a tabela? Digite avançar ou ficar ")).upper()
while seg != "FICAR" or "AVANÇAR":
    print("Por favor, digite apenas avançar ou ficar\n")
    seg = str(input("Podemos seguir ou quer continuar olhando a tabela? Digite avançar ou ficar ")).upper()
    while seg == "FICAR":
        seg = str(input("Podemos seguir ou quer continuar olhando a tabela? ")).upper()
print()

prop = str(input("Você quer criar ou aprimorar um equipamento? ")).upper()

if prop == "CRIAR":
    pre = int(input("Quanto custa sua arma de acordo com a tabela? "))
    sc = str(input("Sua arma é simples ou complexa? ")).upper()
    qnt = int(input("Com quantos aprimoramentos você pretende criar? (Escolha de 1 a 4) "))
    if sc == "SIMPLES":
        cd = 15 + (qnt * 5)
        print("A CD de fabricação deste item é: ", cd)
        if qnt == 1:
            ts = 300
        elif qnt == 2:
            ts = 3000
        elif qnt == 3:
            ts = 9000
        else:
            ts = 18000
        prefim = (pre + ts)/3
        print("Você irá gastar T$", prefim, "com fabricação deste item.")
    if sc == "COMPLEXA":
        cd = 20 + (qnt * 5)
        print("A CD de fabricação deste item é: ", cd)
        if qnt == 1:
            ts = 300
        elif qnt == 2:
            ts = 3000
        elif qnt == 3:
            ts = 9000
        else:
            ts = 18000
        prefim = (pre + ts)/3
        print("Você irá gastar T$",prefim,"com fabricação deste item.")
if prop == "APRIMORAR":
    print("Para aprimorar, você paga apenas a diferença dos valores entre uma melhoria e outra\n")
    qtd = int(input("Quantos aprimoramentos seu equipamento já possui? (Digite de 1 a 4)\n "))
    adc = int(input("Quantos aprimoramentos quer adiconar? (Escolha entre 1 e 4)\n "))
    apfim = qtd + adc
    if apfim > 4:
        print("Você não pode adicionar mais que 4 aprimoramentos ao mesmo item")
        exit()
    sc = str(input("Sua arma é simples ou complexa?\n ")).upper()
    pre = int(input("Quanto custa sua arma de acordo com a tabela?\n "))
    if sc == "SIMPLES":
        cd = 15 + (adc * 5)
        print("A CD para aprimorar será de", cd)
        print()
        if qtd == 1:
            ts = (pre+(lista_aumento[3 if adc == 3 else 2 if adc == 2 else 1]-lista_aumento[0]))/3
            print("Você irá gastar T$", ts)
        elif qtd == 2:
            ts = (pre+(lista_aumento[3 if adc == 2 else 2]-lista_aumento[1]))/3
            print("Você irá gastar T$", ts)
        elif qtd == 3:
            ts = (pre+(lista_aumento[3]-lista_aumento[2]))/3
            print("Você irá gastar T$", ts)
        else:
            print("Você não pode aprimorar seu item, não sei nem como chegou nessa etapa aqui.")
    if sc == "COMPLEXA":
        cd = 20 + (adc * 5)
        print("A CD para aprimorar será de", cd)
        print()
        if qtd == 1:
            ts = (pre+(lista_aumento[3 if adc == 3 else 2 if adc == 2 else 1]-lista_aumento[0]))/3
            print("Você irá gastar T$",ts)
        elif qtd == 2:
            ts = (pre+(lista_aumento[3 if adc == 2 else 2]-lista_aumento[1]))/3
            print("Você irá gastar T$", ts)
        elif qtd == 3:
            ts = (pre+(lista_aumento[3]-lista_aumento[2]))/3
            print("Você irá gastar T$", ts)
        else:
            print("Você não pode aprimorar seu item, não sei nem como chegou nessa etapa aqui.")

print()
print("Espero que tenha gostado, me esforcei bastante para fazer da melhor forma que consegui :)")
