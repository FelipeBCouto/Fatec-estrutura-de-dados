"""
ALGORITMO DE ORDENALÃO MERGE SORT
No processo de ordenação, esse algoritmo "demsonta" a lista original, contendo N elementos, até obter N listas com apenas um elemento cada uma. Em seguida, usando a técnica de mesclagem (menge), "remonta" a lista, desta vez com os elementos já em ordem.
"""

# Variáveis de estatística
divisoes = juncoes = comparacoes = 0

def merge_sort(lista):
    
    global divisoes, juncoes, comparacoes

    # Para que possa have divisão da lista, esta deve ter mais de um elemento
    if len(lista) > 1: # lembrando que len começa em 1

        # Encontra a posição do meio da lista, para fazer a divisão em duas metades
        meio = len(lista) // 2 # ex. lista com 20 elementos: meio = 10

        # Tira uma cópia da primeira metade da lista

        sublista_esq = lista[:meio] # os dois pontos ( : ) se refere a qual parte da lista esse vetor está recebendo. Como está a esquerda, será da posição 0 até a posição do valor contido na variável "meio"

        # Tira uma cópia da segunda metade da lista
        sublista_dir = lista[meio:] # ao contrário da variável anterior, os dois pontos estão à direita, então esse vetor receberá do valor referente a variável meio até o final da lista

        divisoes += 1 # número de divisões

        # Chamamos recursivamente a função para que ela continue repartindo cada uma das sublistas em duas partes menores.
        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)

        # AQUI COMEÇA A MESCLAGEM ORDENADA DAS DUAS SUBLISTAS
        pos_esq = pos_dir = 0
        ordenada = [] # Lista vazia

        # Compara os elementos das sublistas entre si e insere na lista ordenada (criada acima) o menor dentre dois elementos
        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):

            comparacoes += 1
            
            # O menor elemento está na sublista da esquerda
            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:

                # "Desce" o elemento da esqueda para a subllista ordenada
                ordenada.append(sublista_esq[pos_esq])
                pos_esq += 1 # incrementa o pos_esq

            # O menor elmento está na sublista da direita
            else:

                # Desce o eelemento da direita para a subllista ordenada
                ordenada.append(sublista_dir[pos_dir])
                pos_dir += 1 # incrementa o pos_dir

        # Como um dos lados sempre terminará primeiro, armazendo seus valores na lista "ordenada", fazendo com que o while deixe de repetir (***ver condição do laço***), a sublista que não terminou de passar seus valores os armazenará em outra lista, criada a seguir: 
        sobra = [] # lista vazia

        # Sobra à esquerda
        if (pos_esq < pos_dir): 
            sobra = sublista_esq[pos_esq:]
        # Sobra à direita
        else: 
            sobra = sublista_dir[pos_dir:]

        juncoes += 1 # número de junções

        # Técnicamente os valores salvos na lista "ordenada" são menores quando em comparação aos da lista "sobra", criada após o laço "while". Então, o retorno devolve a lista "ordenada" + "sobra", o que garante a ordenação dos valores.
        return ordenada + sobra
    
    else:
        return lista
    
################################################################################################

# Teste com vetor de 10 números
nums = [6, 4, 2, 0, 9, 5, 1, 8, 3, 7]

# Reseta as variáveis de estatística
divisoes = juncoes = comparacoes = 0

resultado = merge_sort(nums)

print("Lista original: ", nums)
print("Lista ordenada: ", resultado)
print(f"Divisões: {divisoes}, junções: {juncoes}, comparações: {comparacoes}")

################################################################################################

from time import time 
import sys
sys.dont_write_bytecode = True # impede a criação de cache

from data.nomes_desord import nomes

nomes = nomes

divisoes = juncoes = comparacoes = 0

hora_ini = time()
merge_sort(nomes)
hora_fim = time()

#print("Nomes ordenados: ", nomes)
print(f"Divisões: {divisoes}, junções: {juncoes}, comparações: {comparacoes}")
print(f"Tempo gasto = {(hora_fim - hora_ini) * 1000} ms")

################################################################################################

divisoes = juncoes = comparacoes = 0

import tracemalloc

tracemalloc.start()		# Inicia a medição de memória
hora_ini = time()
resultado = merge_sort(nomes)
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print("Nomes ordenados: ", resultado)
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Divisões: {divisoes}, junções: {juncoes}, comparações: {comparacoes}")