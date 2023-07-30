"""
ALGORITMO DE ORDENAÇÃO: SELECTION SORT
Isola (seleciona) o primeiro elemento da lista e, em seguida, encontra o menor valor no restante da lista. Se o valorencontrado for menor que o valor previamente selecionado, efetua a troca entre eles. Continuando, seleciona o sergundo elemento da lista, buscando pelo menor valor das posições subsequentes. Faz a troca entre os dois valores, se necessário. Op rocesso se repete até que o penúltimo elemento da lista seja isolado, comparado com o último e feita a troca entre eles, se for o caso.
Conforme pôde ser observado no método Bubble Sort, a função que mais consome processamento é a troca entre os valores. Logo, diferente dele, o Selection Sort realiza SOMENTE UMA TROCA POR PASSADA.
Não obstante, o NÚMERO DE COMPARAÇÕES É DIMINUÍDO A CADA PASSADA.
Além disso, diferente do bubble short, o número de passadas é DETERMINADO pelo tamanho da lista, o que também ajuda na velocidade de execução.

dado n = número de elementos da lista:
máximo de comparações = (n ^ 2 - n) / 2
máximo de trocas = n - 1
máximo de passadas n - 1
"""

comps = trocas = passadas = 0 # variáveis de estatística

def Selection_sort(lista):
    
    global comps, trocas, passadas
    comps = trocas = passadas = 0

    # Loop que vai da primeira até a penúltima posição
    for pos_sel in range(len(lista) - 1): # único parâmetro = começa no 0 e vai até len(lista) - 1
        passadas += 1

        # encontra o menor valor na sublista à frente de pos_sel
        pos_menor = pos_sel + 1 # a cada passada do primeiro loop, pos_sel += 1, até o penúltimo. Ou seja, os valores de pos_menor são 1, 2, 3, 4... até o penúltimo + 1

        for pos in range(pos_sel + 2, len(lista)): # vai da 2ª até a última posição da lista
            # se o valor encontrado na posição pos for MENOR que o valor da posição pos_menor, então pos_menor passa a ser pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos 
        
        comps += 1
        # compara os elementos das posições pos_menor e pos_sel. Se o valor do primeiro for MENOR que o valor do segundo, efetua a troca
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1


# teste com um vetor de 10 números:
nums = [6,4,2,0,9,5,1,8,3,7]
Selection_sort(nums)
print("lista ordenada: ", nums)
print(f"comparações:{comps}; trocas: {trocas}; passadas: {passadas}")

pior_caso = [9,0,1,2,3,4,5,6,7,8] # esse é o pior caso visto que o 9 precisará trocar por todas as posições antes de atingir a sua
Selection_sort(pior_caso)
print("lista ordenada: ", pior_caso)
print(f"comparações:{comps}; trocas: {trocas}; passadas: {passadas}")

melhor_caso = [0,1,2,3,4,5,6,7,8,9] # mesmo no melhor caso, haverá o mesmo número de trocas e comparações do que nas listas acima
Selection_sort(melhor_caso)
print("lista ordenada: ", melhor_caso)
print(f"comparações:{comps}; trocas: {trocas}; passadas: {passadas}")

from time import time 
import sys
sys.dont_write_bytecode = True # impede a criação de cache

from data.nomes_desord import nomes

# pega apenas os 25k primeiros nomes
nomes = nomes[:25000]

hora_ini = time()
Selection_sort(nomes)
hora_fim = time()

print(f"Tempo gasto = {(hora_fim - hora_ini) * 1000} ms")