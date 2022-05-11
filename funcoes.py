#sorteando paises
import random 
def sorteia_pais(dicionario):
    lista_paises = []
    for paises in dicionario.keys():
        lista_paises.append(paises)
    return random.choice(lista_paises)

#distancia de haversine   
from math import *
def haversine(r, x1, y1, x2, y2):
    d = 2*r*asin(((sin((radians(x2)-radians(x1))/2))**2 + cos(radians(x1))*cos(radians(x2))*(sin((radians(y2)-radians(y1))/2)**2))**(1/2))
    return d

#adicionando em uma lista ordenada
def adiciona_em_ordem(pais, distancia, lista):
    i = 0
    if lista == []:
        return [[pais, distancia]]
    for lista_paises in lista:
        if lista_paises[0] == pais:
            return lista
        if lista_paises[1] > distancia:
            lista.insert(i, [pais, distancia])
            break
        i += 1
    return lista

#esta na lista?
def esta_na_lista(pais, lista):
    for paises in lista:
        if pais in paises:
            return True
    return False

#normalizando bases de países  
def normaliza (base_de_paises):
    base_de_paises_normalizada = {}
    qual_continente = {}
    saida = {}
    for continentes, paises in base_de_paises.items():
        for pais, dados in paises.items():
            dados['continente'] = continentes
            saida[pais] = dados
    return saida

#sorteia letra com restrições
import random 
def sorteia_letra(palavra, restritas):
    palavra = palavra.lower()
    lista_palavra = []
    caracteres_especiais = ['.', ',', '-', ';', ' ']
    sorteada = ''
    ok = False
    for letra in palavra:
        if letra not in lista_palavra and letra not in restritas and letra not in caracteres_especiais:
            lista_palavra.append(letra)
            ok = True
    while ok:
        sorteada = random.choice(lista_palavra)
        ok = False
    return sorteada
    
