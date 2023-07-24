"""
Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume
e trocar os canais da televisão.

 -> O controle de volume permite aumentar ou diminuor a potência do volume de
som em uma unidade de cada vez;

 -> O controle de canal também permite aumentar e diminuir o número do canal
em uma unidade, porém, também possibilita trocar para um canal indicado;

 -> Também devem existir métodos para consultar o valor do volume de som e o
canal selecionado.
"""


class Televisao:

    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    @staticmethod
    def checa_volume(x):
        print(f"O valor do volume é {x.volume}")

    @staticmethod
    def checa_canal(x):
        print(f"O canal é {x.canal}")


class ControleRemoto:

    @staticmethod
    def muda_volume(x, y):
        x.volume += y

    @staticmethod
    def muda_canal(x, y):
        x.canal += y


televisao = Televisao(0, 50)

ControleRemoto = ControleRemoto

ControleRemoto.muda_canal(televisao, 5)

televisao.checa_canal(televisao)

ControleRemoto.muda_volume(televisao, 25)

televisao.checa_volume(televisao)