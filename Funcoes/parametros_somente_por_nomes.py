def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Após a barra é escolha: ou passa argumentos nomeados ou não. Porém antes da barra é obrigatório ser posicional.


criar_carro("Palio", 1999, "ABC-123", marca="Fiat",
            motor="1.0", combustivel="Gasolina")  # valido

# criar_carro(modelo="Palio", ano=1999, placa="ABC-123", marca="Fiat",
#             motor="1.0", combustivel="Gasolina")  # inválido
