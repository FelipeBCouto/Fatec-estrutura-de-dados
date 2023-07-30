# range() = FUNÇÃO que GERA UMA FAIXA DE NÚMEROS.
# É muito usada em associação com listas

# range() COM 1 PARÂMETRO: gera uma faixa que vai de 0 (zero) até o valor do parâmetro -1
# Exemplo: range(5) = a faixa vai até 4
# O Python funciona dessa forma pq a contagem dos arrays, por exemplo, começam no 0. Portanto, não há risco de se definir um loop maior do que o tamanho do vetor, causando erro.


print("\n","*" * 25,"range com 1 parâmetro","*" * 25)


# range com 1 parâmetro
for x in range(10):
    print(x,"º loop") # range (loop for) vai até 9


print("\n","*" * 25,"range com 2 parâmetros","*" * 25)


# range com 2 parâmetros
for i in range(5,10):
    print(i,"ª posição")
    # esse loop começa com i = 5 e termina com i = 9


print("\n","*" * 25,"range com 3 parâmetros","*" * 25)


# range com 3 parâmetros:
# 1º: limite inferior (inclusive = início)
# 2º: limite superior (EXCLUSIVE = fim, não considerado)
# 3º: passo = tamanho do pulo, isto é, de quanto em quanto a lista irá saltar
for z in range(0, 22, 3): # lista de - a 21 saltando de 3 em 3
    print(z,"ª doidera")


print("\n","*" * 25,"TÓPICO","*" * 25)


# range com passo (pulo) negativo
for k in range (10,0, -1): # nesse caso, a contagem será regressiva, isto é, de 10 até 1 (pois 0 não é considerado)
    print(k,"º número")


teste = 0
while teste < 5:
    print(f"loop {teste + 1}")
    teste+= 1