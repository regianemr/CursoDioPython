conta_normal = False
conta_especial = True
saldo = 2000
saque = 250
cheque_especial = 350


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível fazer o saque.")

elif conta_especial:

    if saldo >= saque:
        print("Saque realizado!")
    else:
        print("Saldo insuficiente")

else:
    print("Erro")
