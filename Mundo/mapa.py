import pygame

from Mundo.mapa_base import MapaBase


class Mapa(MapaBase):
    """Fase 2 - mapa "Congelante".

    Mais longo (≈ 4800 px, antes só ~3000 px eram utilizáveis) e mais
    vertical: o jogador atravessa abismos pulando de plataforma em
    plataforma, com ilhas de chão como pontos de descanso. Todos os
    inimigos desta fase atiram e há plasma suficiente para derrotá-los.
    """

    LARGURA = 4800
    TEMA = 2

    def __init__(self):

        self.nome = "Congelante"

        dados_chao = [
            (0, 420),        # início
            (1560, 1940),    # ilha 1
            (3100, 3480),    # ilha 2
            (4300, 4800)     # saída
        ]

        dados_plataformas = [
            # Primeira travessia
            (520, 340, 120),
            (710, 290, 120),
            (900, 250, 280),     # plataforma larga (inimigo)
            (1300, 330, 130),

            # Subida até a chave
            (2060, 350, 120),
            (2240, 290, 120),
            (2420, 230, 120),
            (2600, 170, 330),    # plataforma da chave (inimigo)

            # Descida
            (3010, 280, 100),

            # Última travessia
            (3590, 340, 120),
            (3790, 280, 120),
            (3960, 330, 270)     # plataforma larga (inimigo)
        ]

        # (x_centro, y_topo, intervalo de tiro em frames)
        inimigos = [
            (1040, 250, 150),
            (1750, 410, 140),
            (2830, 170, 130),
            (3290, 410, 130),
            (4090, 330, 120)
        ]

        plasmas = [
            (200, 410), (265, 410), (330, 410),
            (580, 340), (770, 290),
            (1340, 330),
            (1620, 410), (1880, 410),
            (2120, 350), (2300, 290), (2480, 230),
            (3060, 280),
            (3160, 410), (3420, 410),
            (3650, 340), (3850, 280),
            (4350, 410)
        ]

        self.montar(
            dados_chao,
            dados_plataformas,
            inimigos,
            plasmas,
            chave=(2900, 115),
            porta=(4640, 410)
        )
