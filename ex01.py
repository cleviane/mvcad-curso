dev = ['amelia', 'azaleia', 'andorinha', 'margarida','rosa']
nome_com_a = 0

for nome in devs:
    if nome[0] == 'a':
        nome_com_a += 1


print(f"foram encontradas {nome_com_a} desenvolvedoras que começam com a letra A")
