from lib.graph import Graph

estradas = Graph()  # Não direcionado, por padrão
print(estradas)

estradas.add_vertex("Franca") # adiciona vértice
print(estradas)
print(f"Grau Franca (a): {estradas.degree('Franca')}\n")

# adicionando dois vértices, que estarão conectados pela aresta "Rod. Candido Portinari"
estradas.add_edge("Franca", "Batatais", "Rod. Candido Portinari")
print(estradas)
print(f"Grau Franca (b): {estradas.degree('Franca')}\n") # o grau de Franca será dois, já que uma aresta sai em direção à cidade de Batatais e essa mesma sai de Batatais e se coneta a Franca (ou seja, não direcionada) 

estradas.add_edge("Franca", "Restinga") # o nome da aresta é None
print(estradas)
print(f"Grau Franca (c): {estradas.degree('Franca')}\n") # o grau é 4, já que uma aresta não direcionada conecta Franca à Batatais e outra Franca à Restinga

# Remoção da aresta Batatais <-> Franca
estradas.remove_edge("Batatais", "Franca", "Rod. Candido Portinari")
print(estradas)

# Tentativa de apagar o vértice "Batatais"
estradas.remove_vertex("Batatais")
print(estradas)