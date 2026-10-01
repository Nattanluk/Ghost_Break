import pygame

from Mundo.plataformas import Criar_Plataforma
from Mundo.porta import Criar_Porta
from Mundo.chave import Criar_Chave
from Combate.inimigo import Inimigo, Atirar
from Combate.plasma import Criar_Plasmas


class Mapa:

    def __init__(self):

        dados_chao = [
            (0, 5),
            (8, 25),
            (29, 42),
            (46, 61),
            (65, 82),
            (87, 105),
            (110, 130),
            (135, 150)
        ]

        dados_plataformas = [
            (180, 340, 90, 50),
            (265, 315, 90, 50),
            (335, 290, 90, 50),
            (405, 265, 130, 50),

            (560, 220, 180, 50),
            (780, 270, 100, 50),

            (900, 170, 140, 50),
            (1050, 240, 120, 50),
            (1180, 310, 150, 50),

            (1370, 250, 180, 50),
            (1600, 300, 130, 50),

            (1780, 350, 160, 50),
            (1980, 280, 130, 50),

            (2160, 200, 160, 50),
            (2050, 280, 100, 50),

            (2340, 300, 150, 50),
            (2530, 250, 150, 50),
            (2720, 320, 150, 50),

            (2880, 330, 120, 50)
        ]

        self.plataformas = Criar_Plataforma().criar(
            dados_plataformas,
            dados_chao
        )

        self.porta = Criar_Porta().criar()

        self.chave = Criar_Chave().criar()

        self.inimigos = [
            Inimigo(400, 350, 2),
            Inimigo(1200, 350, 2),
            Inimigo(2200, 140, 2)
        ]

        for inimigo in self.inimigos:
            inimigo.atirador = Atirar()

        self.plasmas = Criar_Plasmas().criar()


    def desenhar(self, tela, camera_x):

        for plataforma in self.plataformas:
            plataforma.desenhar(
                tela,
                camera_x
            )

        for inimigo in self.inimigos:
            inimigo.desenhar(
                tela,
                camera_x
            )

        self.porta.desenhar(
            tela,
            camera_x
        )

        self.chave.desenhar(
            tela,
            camera_x
        )

        for plasma in self.plasmas:
            plasma.desenhar(
                tela,
                camera_x
            )


    def desenhar_mensagem_porta(
        self,
        tela,
        largura_tela,
        altura_tela
    ):

        fonte = pygame.font.SysFont(
            "Arial",
            22,
            bold=True
        )

        texto = fonte.render(
            "Você precisa da chave!",
            True,
            (255, 255, 255)
        )

        largura_caixa = texto.get_width() + 40
        altura_caixa = texto.get_height() + 20

        x = (
            largura_tela - largura_caixa
        ) // 2

        y = (
            altura_tela - altura_caixa - 20
        )

        pygame.draw.rect(
            tela,
            (15, 20, 30),
            (
                x,
                y,
                largura_caixa,
                altura_caixa
            ),
            border_radius=8
        )

        pygame.draw.rect(
            tela,
            (80, 180, 255),
            (
                x,
                y,
                largura_caixa,
                altura_caixa
            ),
            2,
            border_radius=8
        )

        texto_x = x + (
            largura_caixa - texto.get_width()
        ) // 2

        texto_y = y + (
            altura_caixa - texto.get_height()
        ) // 2

        tela.blit(
            texto,
            (
                texto_x,
                texto_y
            )
        )
