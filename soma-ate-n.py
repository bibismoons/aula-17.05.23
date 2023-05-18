contador = 1
soma = 0

while contador <= 10:
    print(contador)
    soma = soma + contador #soma += contador
    contador += 1
    
print(f"A soma de 1 a 10 é: {soma}")