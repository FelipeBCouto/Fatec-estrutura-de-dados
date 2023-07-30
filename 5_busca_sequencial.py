# lista de números
nums = [9,21,33,12,0,18,24,30,15,6,3,27]

###########################################################

# FUNÇÃO QUE REALIZA UMA >BUSCA SEQUENCIAL< EM UMA LISTA, PROCURANDO POR UM VAL (VALOR).
# Se val for encontrado, retorna a posição de val.
# Caso contrário, retorna o valor -1

def busca_sequencial(lista, val):
    for pos in range(len(lista)):
        if val == lista[pos]: return pos # Encontrou val; retorna a posição onde foi encontrado
    return -1 # Percorreu toda a lista e não encontrou val: retorna -1

###########################################################

# IMPORTANDO COISAS

import sys
sys.dont_write_bytecode = True # impede a criação do cache

from time import time

from data.lista_nomes import nomes # sintaxe: from nome_da_pasta.nome_do_arquivo import nome_da_lista_no_arquivo


# BUSCA POR UM NOME

hora_ini = time()
resultado = busca_sequencial(nomes, "GUILHERME")
hora_fim = time()
print(f"Posição do nome GUILHERME na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

# BUSCA POR UM NOME

hora_ini = time()
resultado = busca_sequencial(nomes, "ZYON")
hora_fim = time()
print(f"Posição do nome ZYON na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

# BUSCA POR UM NOME

hora_ini = time()
resultado = busca_sequencial(nomes, "FELIPE")
hora_fim = time()
print(f"Posição do nome FELIPE na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
resultado = busca_sequencial(nomes, "GRUDERSON")
hora_fim = time()
print(f"Posição do nome GRUDERSON na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

# Note que, quanto maior o tamanho da lista, maior será a necessidade de processamento para verificar a existência do dado e sua posição
# Esse é um dos maiores problemas da busca sequencial

"""
# Input para checar se há o nome na lista
inputnome = input("Informe o nome: ")
res = busca_sequencial(nomes,inputnome) # função está recebendo a lista importada e o input do nome.
if res >= 0:
    print(f"A posição de {inputnome} é: {res + 1}")
else:
    print(f"O nome {inputnome} não foi encontrado na lista.")
"""