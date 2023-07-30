"""
DICIONÁRIOS

Dicionário = registro = objeto (json, por exemplo)

Dicionário é uma estrutura de dados fornecida pela linguagem Python, capaz de armazenar múltiplos valores em uma única variável, por meio de pares de chave-valor.

Logo, cada campo do dicionário representa uma variável, que pode ter diferentes tipos.

Se difere das LISTAS visto que elas salvam os dados em uma única variável (array), com POSIÇÕES NUMERADAS.
Já no DICIONÁRIO, as POSIÇÕES SÃO NOMEADAS (visto que cada posição é uma variável).

Além disso, a criação dos dicionários USAM CHAVES, enquanto as listas usam colchetes.


Sintaxe:

nome_do_dicionario = {
    "nome_da_variável_1": "valor_inicial",      <<<< DOIS PONTOS ENTRE O NOME DA VARIÁVEL E O VALOR, E VÍRGULA PARA SEPARAR OS CAMPOS
    "nome_da_variável_2": "valor_inicial"
}

Lembrando que o tipo de dado da variável é definido ao atribuir o valor a ela.


"""

# Um dicionário é um delimitado por chaves {}
# Diferente das listas, que têm posições numeradas, os dicionários possuem posições NOMEADAS. Cada uma das posições nomeadas de um dicionário é chamada PROPRIEDADE.

pessoa = {
    "nome": "Orizombo Oliveira Osório",
    "sexo": "M",
    "idade": 71,
    "peso": 76,
    "altura": 1.66,
    "aposentado": True
}

# Acessando os valores armazenados no dicionário
print("Nome:",pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Aposentado?", pessoa["aposentado"])

# Calculando o IMC (Índice de Massa Corporal) da pessoa
imc = pessoa["peso"] / pessoa["altura"] ** 2 # Dois asterísticos = exponenciação
print(f"O IMC de {pessoa['nome']} é {imc}.") # Note que, como o texto foi criado com aspas duplas, a variável do dicionário é chamada com aspas simples. Ou seja, é sempre ao contrário.

########################################################################################################################

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R" # Retângulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T" # Triângulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E" # Elipse
}



from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R": # Retângulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T": # Triângulo
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E": # Elipse
        return (forma["base"] / 2) * (forma["altura"] / 2) * pi
    else:
        return None