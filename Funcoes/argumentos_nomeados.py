def salvar_carro(marca, modelo, ano, placa):
    # salvar carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}-{modelo}-{ano}-{placa}")


salvar_carro("Palio", "Fiat", 1999, "ABC-1234")
# nomeado
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-123")

salvar_carro(**{"marca": "Fiat", "modelo": "Palio",
             "ano": 1999, "placa": "ABC-1234"})
