from plataformas import Plataforma
from porta import Porta
from chave import Chave
from inimigo import Inimigo

class Mapa:

    def __init__(self):

        self.plataformas = []

        # Chão da fase
        for x in range(0, 600):
            self.plataformas.append(Plataforma(x * 20, 410, 20, 40))

        # Primeiro buraco
        # (não adicionamos blocos entre 600 e 760)

        for x in range(38, 70):
            self.plataformas.append(Plataforma(x * 20, 410, 20, 40))

        # Plataformas suspensas
        self.plataformas.append(Plataforma(300, 330, 120, 20))
        self.plataformas.append(Plataforma(520, 280, 120, 20))
        self.plataformas.append(Plataforma(900, 230, 150, 20))

        self.porta = Porta(1450, 330)

        self.chave = Chave(700, 370)

        self.inimigos = [
            Inimigo(600, 350),
            Inimigo(1200, 350)
        ]

