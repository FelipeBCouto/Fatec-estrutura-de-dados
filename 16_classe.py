"""
CLASSE
Classe é uma estrutura que representa conjuntamente dados e algoritmos.
Uma classe pode ser comparada a uma "assadeira", com a qual se pode produzir diferentes "assados" (objetos), variando os "ingredientes" (dados) e o "modo de fazer" (algoritmos). Apesar dessas variações, todos os objetos criados a partir de uma classe terão sempre o formato (características essenciais) determinado por esta.


O ato de criar um novo objeto recebe o nome de instanciar, ou seja, criar uma instância. Isso ocorre sempre que a função CONSTRUTOR é chamado. Em Python, essa função é a __init__


SELF torna os elementos contidos na classe, sejam atributos ou métodos, globais em relação a essa.
SEM O SELF, o código interpretará que o elemento é de fora da classe e, portanto, o procurará em outras partes que não nessa. Caso não encontre, apresentará um erro.
Da mesma forma, usando o self, é possível ALTERAR O VALOR DE UM MESMO ATRIBUTO EM DIFERENTES PARTES DO CÓDIGO, o que valerá para TODA A CLASSE, já que ele é global em relação a ela.
EM PYTHON, TODO MÉTODO SEMPRE COMEÇA COM SELF, caso contrário será entendido que ele 


Por convenção, OS NOMES DE CLASSES SEGUEM A FORMA PascalCase, onde as palavras começam com maiúsculas e não possuem underline (regra adotada para grande parte das linguagens).
Ex.: NomeClasse

Outros tipos de nomes são:

Já os nomes de variáveis e funções, em Java e Javascript, seguem a forma camelCase, em que a primeira palavra começa em minúsculo e a segunda em maiúscula.
Ex.: nomeVariavel

Nas lignuagens Python e C, ao contrário, os nomes de variáveis e funções seguem a forma snake_case, ou seja, palavras escritas em minúsculo e separadas por underline.
Ex.: nome_variavel

Por fim, a forma slug-case, comumente usadas em propriedades CSS (já que não possuem cálculos nos seletores e nomes de propriedades), onde as palavras são escritas em minúsculo e separadas por hífen.
Ex.: font-family 


Uma forma de IMPEDIR A ALTERAÇÃO DE ATRIBUTOS após a verificação é 

A criação de MÉTODOS DESTINADOS A ACESSAR OS ATRIBUTOS são comumente chamados de:
1) set (setter) = serve para receber e alterar o valor do atributo 
2) get (getter) = destinado a retornar o valor do atributo
"""


from math import pi


# CLASSE FORMAGEOMETRICA
class FormaGeometrica:

    """
    Uma classe pode ter, dentro de si, tantos dados quanto funções (estas últimas, representando os algoritmos). 
    

    Uma função especial, chamada de __init__, é chamada sempre que um novo objeto é criado a partir de uma classe. Essa função especial também é chamada de CONSTRUTOR (já que serve justamente parar dar origem a um novo objeto, ou seja, realiza sua construção).
    
    Perceba que a __init__ é escrita entre dois underlines de cada lado

        __init__ é um NOME RESERVADO pelo Python, destinado para a criação de objetos 


    Quando aparecem dentro de uma classe:
    ~> funções passam a ser chamadas de MÉTODOS, e seu primeiro parâmetro é sempre SELF, que representa o próprio objeto.
    ~> varipaveis passam a ser chamadas de ATRIBUTOS.
    """

    def __init__(self, base, altura, tipo):

        # Armazenando os dados recebidos DENTRO do objeto, com self, de forma PÚBLICA
        # Dessa forma, os atributos podem ser acessados fora da classe
        # self.base = base
        # self.altura = altura
        # self.tipo = tipo

        # Armazenando os dados recebidos DENTRO do objeto, com self, de forma PRIVADA
        # para PRIVAR UM ATRIBUTO, basta 2 UNDERLINES antes do seu nome 
        # Com os atributos privados, esses só podem ser acessados por meio da classe, chamando-a, mas NUNCA FORA DELAS
        # self.__base = base
        # self.__altura = altura
        # self.__tipo = tipo


        # Armazenando os dados recebidos com o self, de FORMA PRIVADA, chamando os métodos set, para que seja feita a validação dos dados
        self.set_base(base)
        self.set_altura(altura)
        self.set_tipo(tipo)
        

    # Métodos SETTER:
    def set_base(self, val):
        if type(val) not in [int, float] or val <= 0:
            raise Exception(f"ERRO: a base ({val}) deve ser numérica e maior que zero.") 
        self.__base = val # cria um atributo PRIVADO

    def set_altura(self, val):
        if type(val) not in [int, float] or val <= 0:
            raise Exception(f"ERRO: a altura ({val}) deve ser numérica e maior que zero.")
        self.__altura = val # cria um atributo PRIVADO

    def set_tipo(self, val):
        if val not in ["R", "T", "E"]:
            raise Exception(f"ERRO: o tipo ('{val}') deve ser 'R', 'T' ou 'E'.")
        self.__tipo = val # cria um atributo PRIVADO


    # Métodos GETTER:
    def get_base(self):
        return self.__base # retorna o atributo PRIVADO
    
    def get_altura(self):
        return self.__altura # retorna o atributo PRIVADO
    
    def get_tipo(self):
        return self.__tipo # retorna o atributo PRIVADO
    

    # Converte o objeto para uma representação personalizada em string
    def __str__(self):
        return f"< Base: {self.__base}; Altura: {self.__altura}; Tipo: {self.__tipo} >"
    """
    O método __str__, com dois underlines de cada lado, assim como __init__, É UM NOME RESERVADO do Python. 
    
    O __str__ serve para representar o objeto criado a partir da classe como uma string.
    """


    def calc_area(self):
        if self.__tipo == "R": # retângulo
            return self.__base * self.__altura
        elif self.__tipo == "T": # triângulo
            return self.__base * self.__altura / 2
        else:                    # elipse/círculo
            return (self.__base / 2) * (self.__altura / 2) * pi

#########################################################################################################################################


# Criando um objeto chamado forma1 a partir da classe FormaGeometrica
# Perceba que o método __init_ possui 4 parâmetros, porém, o primeiro, SELF, não é considerado para o chamar, mas tão somente "base", "altura" e "tipo"
# perceba que NÃO FOI NECESSÁRIO CHAMAR O MÉTODO __INIT__, 
forma1 = FormaGeometrica(10, 7.2, 'T')


# Agora que os ATRIBUTOS ESTÃO PRIVADOS, para alterar os valores, é necessário chamar os métodos set
forma1.set_altura(200)


# Agora, o print está chamando atributos criados junto ao objeto "forma1" a partir da classe "FormaGeometrica", por meio dos métodos get
print(f"Base: {forma1.get_base()}")  
print(f"Altura: {forma1.get_altura()}")
print(f"Tipo: {forma1.get_tipo()}")
print(f"forma1: {forma1.__str__()}")
print(f"Area = {forma1.calc_area()}")

#########################################################################################################################################

forma2 = FormaGeometrica(7, 4.5, "R")
forma3 = FormaGeometrica(12, 12, "E")


# output dos valores
# perceba que ao colocar os nomes dos objetos "forma2" e "forma3", não foi necessário chamar o método __str__, já que ele é RESERVADO e, portanto, uma vez que o método foi criado ele é chamado pela linguagem quando os objetos são inseridos no print sem acompanhar outro método
print(forma2, f" Área: {forma2.calc_area()}")
print(forma3, f" Área: {forma3.calc_area()}")