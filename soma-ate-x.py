numero = int(input("Digite um número maior que 1:"))

contador = 1
soma = 0

while contador <= numero:
    #print(contador)
    soma += contador
    contador += 1

else:
    print("Finalizou o laço.")

print(f"A some de 1 até {numero} é de: {soma}")