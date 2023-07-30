"""
RECURSIVIDADE

Trata-se de uma técnica de programa pela qual uma função chama a si mesma, em uma condição diferente da inicial. O principal objetivo do uso da recursividade é diminuir a complexidiade de algoritmos.

Em programação, é estabelecido que, da mesma forma que existe um algoritmo recursivo, há outro não recursivo com a mesma funcionalidade, chamado de iterativo.

Ou seja, temos dois tipos de algoritmos: recursivos e não recursivos (iterativos)

Vejamos que:
5! = 5 x 4 x 3 x 2 x 1
4! = 4 x 3 x 2 x 1
3! = 3 x 2 x 1
2! = 2 x 1!
1! = 1
0! = 1

Portanto:
5! = 5 x 4!
4! = 4 x 3!
3! = 3 x 2!
2! = 2 x 1!
1! = 1 x 0!
"""

##################################################################################################################

# Cálculo do fatorial, versão iterativa (não recursiva)
def fatorial_iter(num):
    # Não é possível calcular o fatorial de números negativos
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível") # Exception = interrompe a execução do PROGRAMA pelo erro determinado

    res = 1

    # Loop descendente de num até 1
    for x in range(num, 0, -1): res *= x # res = res * x
    # caso num = 0, o loop não executa, visto que o laço não o considera no momento da execução, e res é devolvido no return como 1 

    return res

##################################################################################################################

# Cálculo do fatorial, de forma recursiva

def fatorial_rec(num):

    # não é possível calcular o fatorial de números negativos
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")
    
    if num <= 1: 
        return 1 # fatorial de 0 e 1 = 1
    else: 
        return num * fatorial_rec(num - 1) # chamada recursiva da função
        # ou seja, a função chama a si mesma com o número inicial menos 1 (num - 1), até que num - 1 = 2
        # assim, ao chegar em fatorial de 1, a função percorre o caminho inverso, multiplicando cada antecessor de num até o próprio num
        # Esse método de chamadas da função recebe o nome de PILHA (pilha de chamadas), justamente por estar EMPILHANDO os valores obtidos em suas chamadas.
        # Já o ESTOURO DE PILHA (stackoverflow) ocorre quando a função executa ao infinito, isto é, não para de empilhar.
        # Condição de saída = é necessário pelo menos UMA situação em que a função, ao ser chamada, não chame a si mesmo novamente - evitando-se o estouro de pilha.
        # Perceba que a pilha começa aumentando-se e, na volta, passa a diminuir.

##################################################################################################################

print("7! = ",fatorial_rec(7))
print("0! = ",fatorial_rec(0))
print("10! = ",fatorial_rec(10))