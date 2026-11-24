import pygame

from Mundo.mapa_base import MapaBase


class Mapa2(MapaBase):
    """Fase 1 - mapa "Eterno".

    Percurso em cinco trechos (≈ 4560 px, antes eram ~3000):
      1. Entrada      - chão seguro, primeiro inimigo e primeiros plasmas.
      2. Escadaria    - degraus de plataformas com plasmas no alto.
      3. Subida       - degraus até a plataforma da CHAVE.
      4. Salão        - plataforma larga com inimigo e chão com dois
                        inimigos (dá para atravessar por cima ou por baixo).
      5. Saída        - último trecho de chão com o portão.
    Todos os saltos foram dimensionados para a física do Saulo
    (pulo ≈ 100 px de altura e ≈ 200 px de alcance).
    """

    LARGURA = 4560
    TEMA = 1

    def __init__(self):

        self.nome = "Eterno"

        dados_chao = [
            (0, 780),
            (890, 1700),
            (1860, 3340),
            (3490, 4070),
            (4230, 4560)
        ]

        dados_plataformas = [
            # Trecho 1
            (470, 340, 130),

            # Trecho 2 - escadaria (o chão continua embaixo, então
            # descer do último degrau não leva ao abismo)
            (1010, 340, 110),
            (1190, 270, 110),
            (1370, 200, 110),

            # Trecho 3 - subida até a chave
            (1970, 340, 130),
            (2170, 270, 130),
            (2350, 200, 130),
            (2510, 140, 150),

            # Trecho 4 - salão
            (2750, 340, 240),
            (3060, 280, 120),

            # Trecho 5
            (3620, 330, 120),
            (3790, 260, 120)
        ]

        # (x_centro, y_topo da plataforma, intervalo de tiro)
        # Na fase 1 os inimigos apenas patrulham.
        inimigos = [
            (560, 410, None),
            (1250, 410, None),
            (2180, 410, None),
            (2870, 340, None),
            (3720, 410, None)
        ]

        # (x_centro, y_base)
        plasmas = [
            (230, 410), (300, 410), (370, 410),
            (535, 340),
            (1065, 340), (1245, 270), (1425, 200),
            (1100, 410),
            (2035, 340), (2235, 270),
            (2430, 200),
            (2870, 410), (3120, 280),
            (3680, 330), (3850, 260)
        ]

        self.montar(
            dados_chao,
            dados_plataformas,
            inimigos,
            plasmas,
            chave=(2575, 85),
            porta=(4400, 410)
        )
