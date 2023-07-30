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

from time import time
import sys
sys.dont_write_bytecode = True # impede criação de cache

import tracemalloc

from data.emp25mil import empresas

empresa_cont = empresas

tracemalloc.start()

hora_ini = time()
Bubble_sort(empresa_cont)
hora_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()

print("################ BUBBLE SORT #################")
print("################### 25 MIL ###################")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")