#LISTAS ou VETORES

# lista de números
valores = [2,3,5,7,9,11,"batata","tomate",True] # perceba que o são USADOS COLCHETES, NÃO CHAVES
print("Lista de valores inicial:",valores)

# OPERAÇÕES SOBRE LISTAS


print("\n","*" * 25,"1. PERCURSO","*" * 25)


# 1. PERCURSO: significa percorrer a lista do primeiro até o último elemento, fazendo algo com cada um deles. No caso a seguir, vamos exibir cada um dos elementos separadamente usando print().

for v in valores:
    print(v)
    # "v" é uma variável qualquer, criada no laço para que ela assuma o valor de cada elemento do vetor e, nesse caso, escreva em tela, UM DE CADA VEZ.
    # o "for" é o mesmo que "para"


print("\n","*" * 25,"2. INSERINDO VALOR NO FIM","*" * 25)


# 2. INSERÇÃO DE NOVO ELEMENTO NO # FIM # DA LISTA: append()
valores.append("cebola")
print(valores)

valores.append(50)
print(valores)


print("\n","*" * 25,"3. INSERINDO VALOR EM UMA POSIÇÃO ESPECÍFICA","*" * 25)


# 3. INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÃO ESPECÍFICA: insert()
# Parâmetros:
# 1º: posição para inserir (contagem inicia em 0)
# 2º: valor a ser inserido
valores.insert(4,"chuchu") # insere na 5ª posição 
print(valores)

valores.insert(0,"abobrinha") # insere na 1ª posição 
print(valores)


print("\n","*" * 25,"4. ACESSANDO VALOR EM UMA POSIÇÃO ESPECÍFICA","*" * 25)


# 4. ACESSANDO UM VALOR EM UMA POSIÇÃO ESPECÍFICA: 
print("Elemento na SÉTIMA posição: ",valores[6])
print("Elemento na TERCEIRA posição: ",valores[2])
print("Elemento na SEGUNDA posição: ",valores[1])
print("Elemento na ÚLTIMA posição: ",valores[-1])
print("Elemento na PENÚLTIMA posição: ",valores[-2])
print("Elemento na ANTEPENÚLTIMA posição: ",valores[-3])


print("\n","*" * 25,"5. SUBSTITUINDO VALORES","*" * 25)


# 5. SUBSTITUINDO VALORES EXISTENTES
print("ANTES:",valores)

# substituindo o valor da posição 10:
valores[9] = "cenoura"

#substituindo o valor da posição 0:
valores[0] = "beterraba"

#substituindo o valor da última posição: 
valores[-1] = "alho"

print("DEPOIS:",valores)


print("\n","*" * 25,"6. DETERMINANDO QUANTIDADE DE ELEMENTOS","*" * 25)


# 6. DETERMINANDO QUANTOS ELEMENTOS HÁ NA LISTA: len()
print("Número de elementos na lista:", len(valores))

# imprimindo o último elemento da lista com a ajuda do len()
print("O último elemento da lista é:",valores[len(valores) -1])
# o menos um é em razão de que o Python começa a contar no 0 e como o comando len() começa sua contagem no 1, é necessário efetuar essa subtração


print("\n","*" * 25,"7. REMOVENDO O ÚLTIMO VALOR","*" * 25)


# 7. REMOVENDO O ÚLTIMO ELEMENTO DA LISTA: pop()
print("ANTES:", valores)
ultimo = valores.pop() # ainda que o array "valores" esteja sendo usado como valor de outra variável, o comando pop() removeu o último valor deste (por não ter nenhum parâmetro entre seus parenteses) e atribuiu para a variável "ultimo".
print("Valor removido da lista:", ultimo)
print("DEPOIS:",valores)


print("\n","*" * 25,"8. REMOVENDO VALOR DE ACORDO COM A POSIÇÃO","*" * 25)


# 8. REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() com parâmetro
print("ANTES:", valores)
pos4 = valores.pop(3) # nesse caso, o pop() está removendo o valor da 4ª posição e atribuindo na variável "pos4"
pos1 = valores.pop(9)
print("Valor removido da 4ª posição:", pos4)
print("Valor removido da 1ª posição:", pos1)
print("DEPOIS:",valores)


print("\n","*" * 25,"9. REMOVENDO UM VALOR ESPECÍFICO","*" * 25)


# 9. REMOVENDO UM ELEMENTO PELO SEU VALOR: remove()
print("ANTES:", valores)
valores.remove("beterraba") # remove o valor beterraba
valores.remove(11) # remove o valor 11
print("DEPOIS:", valores)
# OBS: assim que o primeiro valor determinado em "remove" for localizado, ele parará a execução, ainda que possam existir outros


print("\n","*" * 25,"10. FATIANDO UMA LISTA","*" * 25)

# adicionando valores à lista
valores.append(33)
valores.append("33")
valores.append("Doidera")
valores.append(False)
valores.append("sim")
valores.append("não")


# 10. FATIANDO UMA LISTA
print(valores)

# Cria uma sublista que contém os elementos de 2 (dois) até 7 (sete), não da 2ª (segunda) até a 7ª (sétima) (posição 8 NÃO ENTRA)
sublista1_7 = valores[2:8] # note que isso se refere da posição 2 (dois) até a 7 (sete), não da 1ª (primeira) à 7ª (sétima). Além disso, é necessário colocar um valor a mais do que o último (por isso que foi inserido o 8) - trata-se de uma sintaxe própria do Python.
print("Sublista de 1 a 7:",sublista1_7)

# Cria uma sublista que contém os elementos do início até a posição 5 (posição 6 NÃO ENTRA)
sublista0_5 = valores[0:6]
print("Sublista de 0 a 5:",sublista0_5)

# Cria uma sublista que contém os elementos da posição 10 até o fim da lista
sublista10_fim = valores[10:] # note que basta deixar a posição final em branco para que a sublista receba até o último elemento da lista
print("Sublista de 10 até o final:",sublista10_fim)

# ou seja, A SINTAXE É A SEGUINTE:
# lista[Posição_Inicial : Posição_Final]
# lembrando que o valor dado como posição final NÃO É CONSIDERADO, mas tão somente seu antecessor.
