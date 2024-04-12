numeros = set([1, 2, 3, 1, 2, 3, 4])
print(numeros)

fruta = set("abacaxi")
print(fruta)

carros = set(("palio", "celta", "gol", "palio"))
print(carros)

# Para acessar valores do set tem que converter para uma lista

numeros = list(numeros)
print(numeros[1])
print(numeros[3])

# Outra opção é percorrer o set
carros = set(("palio", "celta", "gol", "palio"))

for carro in carros:
    print(carro)

# Função enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Union - usado para unir conjuntos

conjunto_a = {1, 2}
conjunto_b = {3, 4}

uniao_de_conjuntos = conjunto_a.union(conjunto_b)
print(uniao_de_conjuntos)

# Intersection - unir a parte igual dos dois conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

interseccao_entre_conjuntos = conjunto_a.intersection(conjunto_b)
print(interseccao_entre_conjuntos)

# Difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

diferenca_entre_conjuntos1 = conjunto_a.difference(conjunto_b)
print(diferenca_entre_conjuntos1)

diferenca_entre_conjuntos2 = conjunto_b.difference(conjunto_a)
print(diferenca_entre_conjuntos2)


# Symmetric difference - todos os elementos que não estão na intersecção

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(diferenca_simetrica)

# add - se o elemento passado não estiver, será adicionado, e se já existir, será ignorado

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(45)
sorteio.add(7)

print(sorteio)

# discard - descarta um valor e se o valor não tiver, NÃO dará erro

conjunto_de_numeros = {1, 2, 3, 4, 5, 5, 6, 7, 8}
print(conjunto_de_numeros)
conjunto_de_numeros.discard(1)
print(conjunto_de_numeros)

# pop - tirar valores da lista - os valores da frente
# remove - tem que passar o valor para ser removido, se não existir esse valor, dará erro.
# len - serve para saber o tamanho do elemento
