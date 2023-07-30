"""
    1) Identifique o algoritmo abaixo.

    merge sort

    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).

    b = parâmetro que recebe a lista a ser ordenada
    c = define o meio da lista. Para tanto, chama a última posição do índice da lista passada no parâmetro (b) e divide seu valor por 2.
    d = é a sublista da esquerda, isto é, recebe os valores entre 0 até o meio da lista recebida no parametro da função (b). Depois, chama a própria função (a) recursivamente para processar os valores que recebeu. 
    e = é a sublista da direita, isto é, recebe os valores entre o meio até o final da lista recebida no parametro da função (b). Depois, chama a própria função (a) recursivamente para processar os valores que recebeu. 
    f = é o ponteiro utilizado para "andar" entre os índices da sublista esquerda (d), indicando qual valor será inserido na sublista ordenada (i), se esse for menor que o da direita.   
    g = é o ponteiro utilizado para "andar" entre os índices da sublista direita (e), indicando qual valor será inserido na sublista ordenada (i), se esse for menor que o da esquerda.
    h = sublista vazia que recebe os valores conforme vão sendo ordenados nas condicionais "if" e "else" inseridos no loop "while"
    i = sublista vazia que recebe os valores que sobraram após a execução do laço "while" e não foram inseridos na sublista "i"

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    
    A sublista "h", que deveria receber os valores ordenados nas condicionais do laço "while", foi trocada pela sublista "i", em "i.append(d[f])" e "i.append(e[g])" 
    
"""

def a(b):
    if len(b) <= 1: return b
    c = len(b) // 2
    d = b[:c]
    e = b[c:]
    d = a(d)
    e = a(e)
    f = g = 0
    h = []
    i = []
    while f < len(d) and g < len(e):
        if d[f] < e[g]:
            h.append(d[f])
            f += 1
        else:
            h.append(e[g])
            g += 1
    if(f < g): i = d[f:]
    else: i = e[g:]
    return h + i