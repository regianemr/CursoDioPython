nome = "rEgIanE"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

# Cortando espaços em branco
print(texto)
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

# Junção e centralização
menu = "Python"
print("###" + menu + "###")
print(menu.center(14, "#"))

# Uso do join
print("p-y-t-h-o-n")
print("-".join(menu))
