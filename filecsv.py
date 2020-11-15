#!/usr/bin/env python
import csv

def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimiter=',')
        # List Comprehention
        lista_pessoas = [item for item in leitor]
        print(lista_pessoas)
        # Outro jeito de fazer a consulta:
        for item in lista_pessoas:
            print(item)

ler_arquivo()
