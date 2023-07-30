"""
ESTRUTURAS DE DADOS PILHA (STACK)
É uma estrutura de dados linear de acesso restrito na qual tanto a operação de inserção (tradicionalmente chamada "push"), quanto a operação de remoção ("pop") acontecem no final (ou topo). Em consequência, o funcionamento da pilha obedece ao princípio LIFO (Last In, First Out): o último elemento a entrar deve ser o primeiro a sair.

push = método utilizado para inserir elementos na pilha. Em Python, isso é feito com o APPEND()
pop = método utilizado para retirar elementos na pilha. Em Python, isso é feito com o POP()

A pilha INSERE e REMOVE valores da última posição de seu índice.
"""

class Stack:
    def __init__(self):
        # Cria uma lista privada e vazia para armazenar os dados da pilha.
        self.__data = []

    """
    Método para inserção
    Em pilhas, tem nome padronizado: push
    """
    def push(self, val):
        self.__data.append(val)

    """
    Método que verifica se a pilha está ou não vazia
    """
    def is_empty(self):
        return len(self.__data) == 0 # pega a última posição da lista. Se ele for 0, significa que não HÁ nenhum elemento, já que o len inicia em 1
        # trata-se de um método booleano, que retorna true ou false

    """
    Método para remoção
    Em pilhas, tem nome padronizado: pop
    """
    def pop(self):
        if self.is_empty():
            raise Exception("ERRO: impossível remover de uma pilha vazia.")
        
        # Se chegou até aqui, a pilha NÃO está vazia e a remoção pode ser feita
        return self.__data.pop() # remove o último valor da pilha, já que nenhum outro índice foi indicado
    
    """
    Método que permite consultar o valor que está no topo da pilha, sem removê-lo.
    Em pilhas, tem nome padronizado: peek
    ("peek" significa "dar uma espiadinha" em inglês)
    """
    def peek(self):
        if self.is_empty():
            raise Exception("ERRO: impossível consultar uma lista vazia.")
        
        return self.__data[-1] # -1 significa o primeiro valor do íncide, de trás para frente. Ou seja, o ultimo elemento da lista
    
    """
    Método que permite imprimir a lista como string
    """
    def ___str___(self):
        return str(self.__data)
    
##########################################################################################

pilha = Stack() # Cria uma pilha

pilha.push("Primeiro")
pilha.push("Segundo")
pilha.push("Terceiro")

print(pilha)

removido = pilha.pop()
print(f"Removido: {removido}")

print(pilha)