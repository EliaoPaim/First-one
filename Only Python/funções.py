fluxo_caixa = []

print("_________________")
print("@ Fluxo Caixa")
print("_________________")
print("1 - adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro numero para encerrar #\n")

def adicionar_transação():
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    fluxo_caixa.append({
            "nome": nome,
            "valor": valor
            
        })

while True:
    opção = int(input("Digite 1a opção: "))

    if opção == 1:
        adicionar_transação()
    elif opção == 2:
        adicionar_transação()
    else:
        break

    total = 0
    for fc in fluxo_caixa:
        print("Nome:", fc['nome'], ", Valor: R$", fc['valor'])
        total = total + fc['valor']

    print("Saldo atual: R$", total)