"""
ALGORITMO DE ORDENAÇÃO: BUBBLE SORT
Percorre a lista a ser ordenada em sucessivas passadas, trocando dois elementos adjacentes sempre que o segundo for MENOR QUE o primeiro. Efetua tantas passadas quanto necessárias, até que, na última passada, nenhuma troca seja efetuada.
Há o MÍNIMO de 1 PASSADA.
"""

# Variáveis de estatística
comps = trocas = passadas = 0

def Bubble_sort(lista):
    global comps, trocas, passadas
    comps = trocas = passadas = 0
    # Loop eterno, não sabemos quantas passadas serão necessárias.
    while True:
        trocou = False
        passadas += 1

        # Percurso da lista, do primeiro ao PENÚLTIMO ELEMENTO, com acesso a cada posição. 
        # O loop não pode percorrer até o último elemento o código irá crashar, posto que não haverá nenhum sucessor para ser comparado. Ademais, o último será verificado pelo penúltimo elemento.
        for pos in range(len(lista) - 1): # -1 em razão da regra acima
            comps += 1 # contador de comparação
            
            # Se o número que está à frente na lista for MENOR do que o que está atrás, TROCA
            if lista[pos + 1] < lista[pos]: # se o sucessor for menor que o antecessor
                # em outras linguagens seria necessário uma variável auxiliar para efetuar a troca. Porém, em Python, é possível efetuar o seguinte:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1] # ou seja, 1º = 3º e 2º = 4º
                trocou = True # enquanto houver alguma troca, o trocou = True e, portanto, o loop continuará. 
                trocas += 1

        if not trocou: # Não houve troca na passada. not = negação. Negação de false = true e, portanto, haverá o break
            break      # Interrompoe o loop eterno

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
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")