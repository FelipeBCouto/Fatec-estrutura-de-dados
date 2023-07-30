"""
  ALGORITMO DE BUSCA BINÁRIA
  Dados uma lista, que deve estar PREVIAMENTE ORDENADA,
  e um valor de busca, divide a lista em duas metades
  procurando pelo valor de busca apenas na metade onde
  o valor poderia estar. Novas subdivisões são feitas
  até que se encontre o valor de busca ou que reste
  apenas uma sublista vazia, quando então se conclui
  que o valor de busca não existe na lista.
"""
comps = 0       # Conta o número de comparações

def busca_binaria(lista, val):
    global comps # comps precisa ser setado dentro da função
    comps = 0

    ini = 0               # Início da lista
    fim = len(lista) - 1  # Fim da lista
     # LEMBRANDO QUE O -1 deve ser colocado pq o primeiro elemento da lista está na posição 0. Porém, o len inicia sua contagem no 1
    while ini <= fim: # a condição de parada é até o ini ser <= fim posto que, se o inicio for maior que o fim, todos os valores foram verificados, portanto inexiste o que é desejado.
        meio = (ini + fim) // 2 # // = divisão inteira, isto é, os decimais e resto não são considerados
        # a soma de ini + fim é da posição em si. Ex.: se o ini está na posição 20 e o fim na 50, será feito 20 + 50 = 70. Depois, é dividido por 2. 70 / 2 = 35. Logo, 35 é o meio

        if val == lista[meio]: # o valor de busca foi encontrado. Retorna a posição 
            comps += 1
            return meio

        elif val < lista[meio]: # o valor de busca é menor do que o meio da lista/sublista
            comps += 2 # +2 por ser a segunda comparação
            fim = meio - 1

        else: # val > lista[meio] = o valor de busca é maior do que o meio da lista/sublista
            comps += 2 # +2 visto que o else não é uma nova comparação, já que é a única possível e, portanto, será executada
            ini = meio + 1

    return -1   # valor não existe na lista

# TESTES COM NOMES

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from data.lista_nomes import nomes

# Busca pelo nome FAUSTO

resultado = busca_binaria(nomes, "FAUSTO")


print(f"Posição do nome FAUSTO na lista: {resultado}")

# # Busca pelo nome CARLOS
# hora_ini = time()
# resultado = busca_binaria(nomes, "CARLOS")
# hora_fim = time()
# print(f"Posição do nome CARLOS na lista: {resultado}")
# print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {comps}")

# # Busca pelo nome YARA
# hora_ini = time()
# resultado = busca_binaria(nomes, "YARA")
# hora_fim = time()
# print(f"Posição do nome YARA na lista: {resultado}")
# print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {comps}")

# # Busca pelo nome ORKUTILSON
# hora_ini = time()
# resultado = busca_binaria(nomes, "ORKUTILSON")
# hora_fim = time()
# print(f"Posição do nome ORKUTILSON na lista: {resultado}")
# print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {comps}")

# # Busca pelo nome AARAO
# hora_ini = time()
# resultado = busca_binaria(nomes, "AARAO")
# hora_fim = time()
# print(f"Posição do nome AARAO na lista: {resultado}")
# print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {comps}")