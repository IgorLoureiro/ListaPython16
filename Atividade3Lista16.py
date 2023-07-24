"""
3. Crie uma classe denominada Elevador para armazenar as informações de um elevador
dentro de um prédio. A classe deve armazenar o andar atual (térreo = 0), total de
andares no prédio, excluindo o térreo, capacidade do elevador, e quantas pessoas estão
presentes nele.

* classe deve também disponibilizar os seguintes métodos:

 -> Inicializa: que deve receber como parâmetros a capacidade do elevador e o
total de andares no prédio (os elevadores sempre começam no térreo e vazio);

 -> Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda
houver espaço);

 - > Sai: para remover uma pessoa do elevador (só deve remover se houver alguém
dentro dele);

 -> Sobe: para subir um andar (não deve subir se já estiver no último andar);
 -> Desce: para descer um andar (não deve descer se já estiver no térreo);

"""


class Elevador:

    def __init__(self, capacidade, numerodeandares):
        self.capacidade = capacidade
        self.NumeroDeAndares = numerodeandares
        self.total = 0
        self.andar = 0

    @classmethod
    def entrar(cls, pessoas, elevador):
        if elevador.total + pessoas <= elevador.capacidade:
            elevador.total += pessoas
        else:
            print(f"O numero de pessoas excede a capacidade")

    @classmethod
    def sai(cls, pessoas, elevador):
        if elevador.total - pessoas >= 0:
            elevador.total -= pessoas
        else:
            print(f"O numero de pessoas a sair é maior do que o numero de pessoas dentro")

    @classmethod
    def sobe(cls, andares, elevador):
        if elevador.andar + andares <= elevador.NumeroDeAndares:
            elevador.andar += andares
        else:
            print(f"O numero de andares que deseja subir é mais alto que o prédio")

    @classmethod
    def desce(cls, andares, elevador):
        if elevador.andar - andares >= 0:
            elevador.andar -= andares
        else:
            print(f"O numero de andares que deseja descer é mais baixo que o Térreo")



