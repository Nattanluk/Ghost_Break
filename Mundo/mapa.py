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
            (128, 140),
            (143, 155),
            (158, 170),
            (173, 185),
            (188, 200),
            (203, 215)
        ]

        dados_plataformas = [
            (180, 340, 100, 50),
            (310, 300, 110, 50),
            (450, 260, 120, 50),
            (610, 300, 140, 50),
            (790, 240, 130, 50),
            (950, 190, 150, 50),
            (1150, 250, 130, 50),
            (1320, 310, 150, 50),
            (1510, 250, 140, 50),
            (1690, 190, 150, 50),
            (1870, 250, 130, 50),
            (2040, 320, 150, 50),
            (2230, 260, 160, 50),
            (2440, 200, 150, 50),
            (2630, 270, 140, 50),
            (2810, 330, 150, 50),
            (2990, 270, 140, 50),
            (3160, 200, 160, 50),
            (3370, 260, 150, 50),
            (3550, 320, 140, 50),
            (3730, 270, 150, 50),
            (3900, 210, 160, 50),
            (4080, 280, 150, 50)
        ]

        self.plataformas = Criar_Plataforma(2).criar(
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
            plataforma.desenhar(tela, camera_x)

        for inimigo in self.inimigos:
            inimigo.desenhar(tela, camera_x)

        self.porta.desenhar(tela, camera_x)
        self.chave.desenhar(tela, camera_x)

        for plasma in self.plasmas:
            plasma.desenhar(tela, camera_x)

    def desenhar_mensagem_porta(self, tela, largura_tela, altura_tela):

        fonte = pygame.font.SysFont("Arial", 22, bold=True)

        texto = fonte.render(
            "Você precisa da chave!",
            True,
            (255, 255, 255)
        )

        largura_caixa = texto.get_width() + 40
        altura_caixa = texto.get_height() + 20

        x = (largura_tela - largura_caixa) // 2
        y = altura_tela - altura_caixa - 20

        pygame.draw.rect(
            tela, (15, 20, 30),
            (x, y, largura_caixa, altura_caixa),
            border_radius=8
        )

        pygame.draw.rect(
            tela, (80, 180, 255),
            (x, y, largura_caixa, altura_caixa),
            2, border_radius=8
        )

        texto_x = x + (largura_caixa - texto.get_width()) // 2
        texto_y = y + (altura_caixa - texto.get_height()) // 2

        tela.blit(texto, (texto_x, texto_y))