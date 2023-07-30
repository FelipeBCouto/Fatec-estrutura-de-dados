"""
    1) Identifique o algoritmo abaixo.

    bubble sort

    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).

    b = parâmetro da função "a" que recebe a lista a ser ordenada.
    c = variável booleana que se inicia em "false" e se torna "true" caso os valores da lista troquem de posição dentro do laço.  
    d = é o ponteiro que define a posição na lista. Inicia na primeira casa, 0, e percorre até a última.

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.

    A troca de posições que ocorre dentro da condicional, b[d + 1], b[c] = b[c], b[d + 1], está recebendo a variável booleana "c" para indicar o índice da lista, ao invés da variável "d".

"""

def a(b):
    while True:
        c = False
        for d in range(len(b) - 1):
            if b[d + 1] < b[d]:
                b[d + 1], b[d] = b[d], b[d + 1]
                c = True
        if not c:
            break