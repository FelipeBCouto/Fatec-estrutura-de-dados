"""
1. Todas as questões deste arquivo referem-se ao grafo representado
   na imagem "grafo.png".

2. Importe a classe Graph neste arquivo e implemente em código o grafo
   mostrado na imagem. Use print() para exibir o grafo.

3. Exclua o vértice cujo valor é "Etelvina". Use print() para exibir o grafo
   após a exclusão.
"""

from lib.graph import Graph

"""
2° EXERCÍCIO:
"""

relacoes = Graph(True)

# Adição de nós:
relacoes.add_vertex('Guiomar')
relacoes.add_vertex('Veneranda')
relacoes.add_vertex('Etelvina')
relacoes.add_vertex('Nereu')
relacoes.add_vertex('Quiteria')

# Adição das arestas:
relacoes.add_edge('Guiomar', 'Veneranda', 'amiga de')
relacoes.add_edge('Veneranda', 'Guimar', 'amiga de')
relacoes.add_edge('Guiomar', 'Nereu', 'madrinha de')
relacoes.add_edge('Nereu', 'Guiomar', 'afilhado de')
relacoes.add_edge('Nereu', 'Veneranda', 'apaixonado por')
relacoes.add_edge('Nereu', 'Etelvina', 'filho de') # Já exclui
relacoes.add_edge('Etelvina', 'Nereu', 'mãe de') #já exclui
relacoes.add_edge('Veneranda', 'Quiteria', 'deve dinheiro para')
relacoes.add_edge('Veneranda', 'Etelvina', 'trabalha para') #já exclui
relacoes.add_edge('Quiteria', 'Nereu', 'apaixonada por')

print('################# EXERCÍCIO 2 #################')
print(relacoes)
print('\n')

"""
3° EXERCÍCIO:
"""
relacoes.remove_edge('Etelvina', 'Nereu', 'mãe de')
relacoes.remove_edge('Veneranda', 'Etelvina', 'trabalha para')
relacoes.remove_edge('Nereu', 'Etelvina', 'filho de')
relacoes.remove_vertex('Etelvina')

print('################# EXERCÍCIO 3 #################')
print(relacoes)