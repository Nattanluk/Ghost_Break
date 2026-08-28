#mapa.py
import pygame

from Mundo.plataformas import Criar_Plataforma
from Mundo.porta import Criar_Porta
from Mundo.chave import Criar_Chave
from Combate.inimigo import Criar_Inimigos
from Combate.plasma import Criar_Plasmas



class Mapa:

    def __init__(self):

        # Plataformas
        self.plataformas = Criar_Plataforma().criar()

        # Porta
        self.porta = Criar_Porta().criar()

        # Chave
        self.chave = Criar_Chave().criar()

        # Inimigos
        self.inimigos = Criar_Inimigos().criar()

        # Plasmas
        self.plasmas = Criar_Plasmas().criar()


    def desenhar(self, tela, camera_x):

        # Plataformas
        for plataforma in self.plataformas:

            plataforma.desenhar(
                tela,
                camera_x
            )


        # Inimigos
        for inimigo in self.inimigos:

            inimigo.desenhar(
                tela,
                camera_x
            )


        # Porta
        self.porta.desenhar(
            tela,
            camera_x
        )


        # Chave
        self.chave.desenhar(
            tela,
            camera_x
        )


        # Plasmas
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

        x = (largura_tela - largura_caixa) // 2

        y = altura_tela - altura_caixa - 20

        # Fundo da caixa
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

        # Borda
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

        # Texto
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