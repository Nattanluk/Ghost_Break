#mapa.py
from plataformas import Plataforma
from porta import Porta
from chave import Chave
from inimigo import Inimigo
from plasma import Plasma


class Mapa:

    def __init__(self):

        self.plataformas = []

        # Chão - primeiro trecho
        for x in range(0, 30):
            self.plataformas.append(
                Plataforma(x * 20, 410, 20, 40)
            )

        # Segundo trecho
        for x in range(38, 70):
            self.plataformas.append(
                Plataforma(x * 20, 410, 20, 40)
            )

        # Terceiro trecho
        for x in range(80, 130):
            self.plataformas.append(
                Plataforma(x * 20, 410, 20, 40)
            )

        # Quarto trecho
        for x in range(140, 180):
            self.plataformas.append(
                Plataforma(x * 20, 410, 20, 40)
            )

        # Plataformas suspensas

        self.plataformas.append(
            Plataforma(300, 315, 120, 20)
        )

        self.plataformas.append(
            Plataforma(520, 280, 120, 20)
        )

        self.plataformas.append(
            Plataforma(800, 230, 150, 20)
        )

        self.plataformas.append(
            Plataforma(1150, 250, 120, 20)
        )

        self.plataformas.append(
            Plataforma(1450, 320, 130, 20)
        )

        self.plataformas.append(
            Plataforma(1750, 290, 150, 20)
        )

        self.plataformas.append(
            Plataforma(2000, 200, 430, 20)
        )
        
        self.plataformas.append(
            Plataforma(2190, 105, 60, 12)
        )

        self.plataformas.append(
            Plataforma(2650, 280, 90, 20)
        )

        # Porta
        self.porta = Porta(2910, 330)

        # Chave
        self.chave = Chave(2205, 85)

        # Inimigos
        self.inimigos = [
            Inimigo(400, 350),
            Inimigo(1200, 350)
        ]

        # Plasmas
        self.plasmas = [
            Plasma(400, 370),
            Plasma(800, 370),
            Plasma(1000, 190),
            Plasma(1200, 370),
            Plasma(1350, 370)
        ]

