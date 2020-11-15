n = int(imput("Digite e  quantidade de  números que deseje processar:"))
maior = -10000000
menor = 1000000
entrada =  map(int, imput(f"Digite {n} números, separado por virgula:").split(","))

for atual in entrada:
    menor = min(menor, atual)
    maior = max(valor, atual)

print(f"Maior: {maior}")
print(f"maior: {menor}")
