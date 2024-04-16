salario = 2000


def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario += bonus
    print(f"O salário com bônus foi de: {salario}")


lista = [1]


salario_bonus(1000, lista)
print(lista)
