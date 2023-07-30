"""
    1) Identifique o algoritmo abaixo.

    busca binária

    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).

    b = parâmetro da função "a" que recebe a lista a ser ordenada.
    c = parâmetro da função "a" que recebe o dado que está sendo buscado, seja um nome ou outro.
    d = variável que define o inicio da lista, começando em 0".
    e = variável que recebe a ultima posição da lista. O "-1" se dá em razão de que as casas da lista começam em 0, enquanto a função "len" inicia em 1.
    f = variável que define o meio da lista. Recebe os valores de inicio (d) e fim (e) da lista, soma-os e depois divide o resultado por 2.

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o. 

    Na condicional que verifica se o dado foi localizado, "if c == b[f]: e = f", ao invés de retornar sua posição (f), ele atribui a variável com a última posição da lista (e) o valor do meio da lista (f) e não há retorno.

"""    

def a(b, c):
    d = 0
    e = len(b) - 1
    while d <= e: 
        f = (d + e) // 2
        if c == b[f]: return f
        elif c < b[f]: e = f - 1
        else: d = f + 1
    return -1