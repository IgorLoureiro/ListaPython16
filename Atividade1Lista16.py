"""
1. Crie uma classe para representar uma pessoa, com os atributos privados de nome,
idade e altura. Crie os métodos públicos necessários para sets e gets e também um
método para imprimir os dados de uma pessoa.
"""


class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura



    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

def pegardados(Nome):
    print(f"Nome: {Nome.nome}")
    print(f"Idade: {Nome.idade}")
    print(f"Altura: {Nome.altura}")

Igor = Pessoa('Igor', 21, 1.77)

pegardados(Igor)