opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato:"))

if opcao == 1:
    valor = float(input("Informe o valor a ser sacado: "))

elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida")
