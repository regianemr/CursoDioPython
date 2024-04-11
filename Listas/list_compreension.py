numeros = [2, 5, 36, 48, 10, 13, 16, 55]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
quadrado = [numero ** 2 for numero in numeros]

print(pares)
print(impares)
print(quadrado)
