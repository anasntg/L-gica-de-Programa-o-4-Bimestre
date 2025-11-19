a = 1
soma_pares = 0
soma_impares = 0
while (a <= 10):
    n = int(input("Digite um Número:"))
    if n % 2 == 0:
        soma_pares = soma_pares + n
    else:
        soma_impares = soma_impares + n
    a = a + 1
print("A SOMA DOS NÚMEROS PARES É:", soma_pares)
print("A SOMA DOS NÚMEROS ÍMPARES É:", soma_impares)