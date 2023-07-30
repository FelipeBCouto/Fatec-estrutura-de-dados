# LISTA 
frutas = ["laranja","maça","uva","pera","mamão","abacate","amora"]

# Para percorrer uma lista e exibir apenas seus elementos, usamos for..in, como já vimos no arquivo 2

for f in frutas:
    print(f)

print("-" * 80)

# Agora, se precisarmos exibir, além do elemento, também sua POSIÇÃO, devemos usar o range()
for pos in range(len(frutas)):
    print(f"A fruta {frutas[pos]} está na posição {pos}.")

print("-" * 80)

# Percurso em ordem inversa usando range() com 3 parâmetros
for i in range (len(frutas) -1, -1, -1):
    print(f"A fruta {frutas[i]} está na posição {i}.")
    # Nos parâmetros, temos:
    # O primeiro -1: representa que a lista começará pelo fim
    # O segundo -1: representa o último item da lista. Como Python sempre exclui o valor final, o -1 foi inserido para que a a execução vá até 0
    # O terceiro -1: representa a quantidade de casas que cada execução irá pular. Como a lista está em ordem decrescente, haverá sempre uma subtração - nesse caso, de 1 em 1.

