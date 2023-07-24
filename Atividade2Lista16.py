"""
2. Crie uma classe Agenda que pode armazenar 10 pessoas e seja capas de realizar as
seguintes operações:

 - void armazenaPessoa(String nome, int idade, float altura);
 - void removePessoa(String nome);
 - int buscaPessoa(String nome); // informa em que posição da agenda está a pessoa
 - void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda
 - void imprimePessoa(int index); // imprime os dados da pessoa que está na posição “1” da agenda.

"""

class Pessoa:

    def __init__(self, Nome, Idade, Altura):
        self.nome = Nome
        self.idade = Idade
        self.altura = Altura


class Agenda:

    Agenda = []

    @classmethod
    def armazenapessoa(cls, pessoa):
        if isinstance(pessoa, Pessoa):
            Agenda.Agenda.append(pessoa)
        else:
            print("A pessoa informada não foi devidamente cadastrada como uma Pessoa")

    @classmethod
    def removepessoa(cls, pessoa):
        if isinstance(pessoa, Pessoa):
            Agenda.Agenda.remove(pessoa)
        else:
            print("A pessoa informada não foi devidamente cadastrada como uma Pessoa")

    @classmethod
    def encontrapessoa(cls, pessoa):
        if isinstance(pessoa, Pessoa):
            print(f"A pessoa se encontra na posição: {Agenda.Agenda.index(pessoa)}")
        else:
            print("A pessoa informada não foi devidamente cadastrada como uma Pessoa")

    @classmethod
    def imprimeagenda(cls):
        for x in Agenda.Agenda:
            print(f"Nome: {x.nome}")
            print(f"Idade: {x.idade}")
            print(f"Altura: {x.altura}")
            print()

    @classmethod
    def imprimepessoa(cls, numero):

        try:
            print(f"Nome: {Agenda.Agenda[numero].nome}")
            print(f"Idade: {Agenda.Agenda[numero].idade}")
            print(f"Altura: {Agenda.Agenda[numero].altura}")
        except:
            print("O numero informado não se encontra na Agenda")


p1 = Pessoa("Igor", 21, 1.77)

Agenda.armazenapessoa(p1)

Agenda.imprimepessoa(0)

Agenda.encontrapessoa(p1)


