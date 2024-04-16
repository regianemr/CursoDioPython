def exibir_mensagem(nome):
    print(f"Seja bem-vindo, {nome}!")


def exibir_mensagem_2(nome="querido(a)"):
    print(f"Bem-vindo, {nome}!")


exibir_mensagem("Regi")
exibir_mensagem_2()
exibir_mensagem_2("Regiane")


def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 5, 2, 8]))
print(retorna_antecessor_e_sucessor(10))
