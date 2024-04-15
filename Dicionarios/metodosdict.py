contatos = {
    "regianemelo1995@gmail.com": {"nome": "Regiane", "telefone": "9172-2420"}}

# copy
copia = contatos.copy()
copia["regianemelo1995@gmail.com"] = {"nome": "Regi"}

print(contatos["regianemelo1995@gmail.com"])
print(copia["regianemelo1995@gmail.com"])

# fromkeys - cria chaves e valores

# keys - retorna o valor das chaves
novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys())

# pop - remove e retorna o valor que removeu
resultado = contatos.pop("regianemelo1995@gmail.com")
print(resultado)

resultado = contatos.pop("regianemelo1995@gmail.com", "Não encontrado")
print(resultado)

# setdefault - adiciona chaves e não altera a chave já existente
contatos = {"nome": "Regiane", "telefone": "9172-2420"}
contatos.setdefault("nome", "Gleison")
print(contatos)

contatos.setdefault("idade", 28)
print(contatos)

# update - deixa atualizar o dicionario em um novo dicionario
contatos = {
    "regianemelo1995@gmail.com": {"nome": "Regiane", "telefone": "9172-2420"}}

contatos.update({"regianemelo1995@gmail.com": {"nome": "Regi"}})
print(contatos)

# passando um novo dicionario
contatos.update(
    {"gleison@gmail.com": {"nome": "Gleison", "telefone": "9999-0000"}})
print(contatos)

# Values - retorna os valores do dicionario
novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.values())

# in - método de verificação, forma de saber se uma chave existe
contatos = {
    "regianemelo1995@gmail.com": {"nome": "Regiane", "telefone": "9172-2420"},
    "gleison@gmail.com": {"nome": "Gleison", "telefone": "9999-0000"}}

resultado = "regianemelo1995@gmail.com" in contatos
print(resultado)

resultado = "elayne@gmail.com" in contatos
print(resultado)

resultado = "telefone" in contatos["gleison@gmail.com"]
print(resultado)

# Del - retira o valor do dicionário passando o objeto que quer remover
contatos = {
    "regianemelo1995@gmail.com": {"nome": "Regiane", "telefone": "9172-2420"},
    "gleison@gmail.com": {"nome": "Gleison", "telefone": "9999-0000"}}

del contatos["gleison@gmail.com"]["telefone"]
print(contatos)
