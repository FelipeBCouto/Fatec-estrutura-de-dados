"""
ALGORITMO DE ORDENAÇÃO QUICK SORT


Escolhe um dos elementos da lista para ser o pivo (na nossa Umplementação, o ultimo elemento) e, na primeira passada, divide a lista, a partir da posição final do pivo, em una sublista a esquerda, contendo apenas valores menores que o pivo, e outra sublista à direita, que contém apenas valores maiores que o pivô


Em seguida, recursivamente, repete o processo em cada uma das sublistas, até que toda a lista esteja ordenada.

Em relação ao CONSUMO DE MEMÓRIA, o quick sort é superior em relação ao merge sort.

"""

# Variáveis de estatística
passadas = comps = trocas = 0

def quick_sort(lista, ini = 0, fim = None): # none = null ou undefined

    # Quando não soubermos o valor da variável "fim", vamos atribuir a ela a última posição da lista
    if fim is None: fim = len(lista) - 1

    # Para que o algoritmo trabalhe, é necessário que a faixa delimitada pelas variáveis "ini" e "fim" tenha, pelo menos, dois elementos. Caso contrário, saímos da função sem fazer nada
    if fim <= ini: return

    global passadas, comps, trocas

    # Inicialização das variáveis
    pivot = fim
    div = ini - 1
    passadas += 1

    # Percorre a lista da posição "ini" até a posição "fim" -1 (penúltima casa)
    for pos in range(ini, fim):

        # Compara os elementos das posições "pos" e "pivot"
        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1

            # Se os valores das variáveis "div" e "pos" forem diferentes entre si e o elemento da posição "pos" for menos que o elemento da posição "div", promove a troca entre eles
            comps += 1
            if pos != div and lista[pos] < lista[div]:
                lista[pos], lista[div] = lista[div], lista[pos]
                trocas += 1

    # Depois que o loop acaba, o divisor é incrementado ainda uma vez
    div += 1

    # Caso os valores das posições "div" e "pivot" sejam diferentes entre si, é feita a comparação entre os elementos dessas posições. Se o valor de "pivot" for menor, promove-se a troca entre os elementos.
    comps += 1
    if pivot != div and lista[pivot] < lista[div]:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1

    # O ELEMENTO DA POSIÇÃO "div" ESTÁ EM SEU LUGAR CORRETO AGORA.

    # Chamamos recursivamente a função para ordenar a sublista à esquerda da posição "div"
    # Perceba que a mesma lista é passada (1º parâmetro). Porém, começará no primeiro elemento e irá até a posição que a variável "div" parou, - 1 (2º e 3º parâmetros)
    quick_sort(lista, ini, div -1) 

    # Fazemos o mesmo para ordenar a sublista à direita de "div"
    quick_sort(lista, div + 1, fim)

################################################################################################

from time import time 
import sys
import tracemalloc
sys.dont_write_bytecode = True # impede a criação de cache

from data.emp25mil import empresas

empresa_cont = empresas

passadas = comps = trocas = 0

tracemalloc.start()

hora_ini = time()
quick_sort(empresa_cont)
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print("################# 100 MIL #################")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Tempo gasto = {(hora_fim - hora_ini) * 1000} ms")