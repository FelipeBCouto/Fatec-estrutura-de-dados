"""
ALGORITMO DE ORDENAÇÃO: BUBBLE SORT v2
Percorre a lista a ser ordenada em sucessivas passadas, trocando dois elementos adjacentes sempre que o segundo for MENOR QUE o primeiro. Efetua tantas passadas quanto necessárias, até que, na última passada, nenhuma troca seja efetuada.
Há o MÍNIMO de 1 PASSADA.
Diferente da primeira versão, essa é OTIMIZADA, COM ENCOLHIMENTO DO PERCURSO A CADA PASSADA.
Todavia, ELE NÃO ALTERA O NÚMERO DE TROCAS, APENAS DE COMPARAÇÕES.
"""

# Variáveis de estatística
comps = trocas = passadas = 0

def Bubble_sort(lista):
    global comps, trocas, passadas
    comps = trocas = passadas = 0

    desloc = 1

    while True:
        trocou = False
        passadas += 1

        for pos in range(len(lista) - desloc): #desloc subtraindo o último valor a ser comparado 
            comps += 1

            if lista[pos + 1] < lista[pos]: 
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1] 
                trocou = True  
                trocas += 1

        if not trocou: 
            break      
        # aumenta o deslocamento para diminuir o tamanho da próxima passada
        desloc+=1

##############################################

# Teste com vetor de 10 números 

nums = [6, 4, 2, 0, 9, 5, 1, 8, 3, 7]
Bubble_sort(nums) # a função não pode ser chamada dentro de print
print("Lista ordenada", nums)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")

print("*" * 100)

# Pior caso de bubble sort: lista ao contrário

pior_caso = [9,8,7,6,5,4,3,2,1,0]
Bubble_sort(pior_caso)
print("Lista ordenada (pior caso): ", pior_caso)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")


print("*" * 100)

# Pior caso de bubble sort: lista já ordenada

melhor_caso = [0,1,2,3,4,5,6,7,8,9]
Bubble_sort(melhor_caso)
print("Lista ordenada (melhor caso): ", melhor_caso)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")


print("*" * 100)


# Ordenação de nomes

from time import time
import sys
sys.dont_write_bytecode = True # impede criação de cache

from data.nomes_desord import nomes

# pega apenas os 10k primeiros nomes
nomes = nomes[:25000]

hora_ini = time()
Bubble_sort(nomes)
hora_fim = time()

print("Nomes ordenados: ", nomes)
print(f"Tempo gasto: {(hora_fim - hora_ini) * 10000}ms")
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")