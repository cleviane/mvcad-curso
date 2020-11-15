lista_vazia = []

lista_numeros = [10,2,3,6]

lista_string = ['alini', 'pri']

lista_mista = [1, 'alini', lista_numeros]

print(lista_mista.count('alini'))

print(lista_mista.index(1))

print(lista_numeros.sort())

dev = []



#

devs = ['andorinha', 'amelia', 'azaleia', 'melissa', 'violeta']
num_letra_a = 0

for nome in devs:
    # Se a primeira letra for a
    if nome[0] == 'a':
        num_letra_a += 1

print(num_letra_a)




presentes = int(input("Quantas pessoas estavam presentes? "))
lista = []
index = 0
while (index < presentes):
    nomes = input("Digite o nome da aluna presente: ")
    index += 1
    lista.append(nomes)
lista.sort()
print("Participantes por ordem alfabética: ")
print("\n".join(lista))



tupla = (1, 3)
dicionario = {
    'nome': "alini",
    'idade': 30,
    'cidade': 'blumenau',
    'hobies': ['dorama', 'programar'],
    'friorenta': False
}

lista_coisas = [tupla, dicionario]


quantidade = int(input("Quantos números você quer escolher? "))

index = 0
lista = []
while (index < quantidade):
    proximo = int(input("Digite o proximo número: "))
    index += 1
    lista.append(proximo)
lista.sort()
n = len(lista)
ultimo = n - 1
print(lista)
print(f"Menor: {lista[0]} , Maior: {lista[ultimo]} ")



# nova parte


def escrever_cabecalho(lista_cabecalho):
    with open(nome_arquivo, 'a') as file:
        escritor = csv.DictWriter(file, fieldnames=lista_cabecalho)
        escritor.writeheader()


def escrever_linhas(lista_cabecalho, lista_linhas):
    with open(nome_arquivo, 'a') as file:
        escritor = csv.DictWriter(file, fieldnames=lista_cabecalho)
        escritor.writerows(lista_linhas)


# escrever_cabecalho(lista_cabecalho)

pessoa1 = {
    'nome': 'jess3',
    'idade': 30
}
lista_cabecalho = ['nome', 'idade']
nome_arquivo = 'mvcad-exemplo-dict.csv'

escrever_linhas(lista_cabecalho, [pessoa1])
