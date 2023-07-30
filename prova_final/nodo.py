"""
    1. Observe a classe Nodo listada logo abaixo.

    2. Responda: para qual ou quais estruturas esse nodo pode ser utilizado?
    lista duplamente encadeada, denominada Doubly Linked List, e árvore binária de busca, também chamada de Binary Search Tree.
    
    3. Qual seria o propósito dos atributos a, b e c?
    Atributo "a": representa a informação de usuário armazenada no nodo.
    Atributo "b": seria o prev/next para Doubly Linked List ou o left/right para Binary Search Tree.
    Atributo "c": seria o prev/next para Doubly Linked List ou o left/right para Binary Search Tree.
    OBS: note que, para "b" e "c", se um for prev/left, o outro será next/right, assim como o contrário é verdadeiro.
"""

class Node:
    def __init__(self, x):
        self.a = x
        self.b = None
        self.c = None
