maisvelho = 0
media = 0
soma = 0
nome_maisvelho = ""
maisnovo = 0
nome_maisnovo = ""


for c in range(1, 5):
    print("===== {}ª PESSOA =====".format(c))
    nome = str(input("Nome:"))
    idade = int(input("Idade:"))
    soma+=idade

    if c == 1:
        maisvelho = idade
        maisnovo = idade
        nome_maisvelho = nome
        nome_maisnovo = nome
    elif idade > maisvelho:
            maisvelho = idade
            nome_maisvelho = nome
    elif idade < maisnovo:
            maisnovo = idade
            nome_maisnovo = nome

media = soma / 4
print("A média de idade do grupo é {}.".format(media))
print("A pessoa mais velha do grupo tem {} anos e seu nome é {}.".format(maisvelho, nome_maisvelho))
print("A pessoa mais nova do grupo tem {} anos e seu nome é {}.".format(maisnovo, nome_maisnovo))
