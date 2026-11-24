#porta.py
import math

import pygame

from Sistemas.recursos import carregar_escalada
from Sistemas.efeitos import halo


class Porta:

    LARGURA_SPRITE = 100
    ALTURA_SPRITE = 130

    def __init__(self, x, y):

        # (x, y) = canto superior esquerdo da área de colisão.
        # A colisão agora fica centralizada no desenho da porta.
        self.rect = pygame.Rect(x, y, 56, 90)

        # Sprite
        self.sprite = carregar_escalada(
            "imagens/porta_pixel_art.png",
            (self.LARGURA_SPRITE, self.ALTURA_SPRITE)
        )

        self.brilho = halo(80, (110, 190, 255), 110)

        self.tempo = 0.0
        self.aberta = False

    def atualizar(self, tem_chave=False, efeitos=None):

        self.tempo += 0.05
        self.aberta = tem_chave

        if self.aberta and efeitos is not None:

            if int(self.tempo * 100) % 7 == 0:

                efeitos.brilho_suave(
                    self.rect.centerx,
                    self.rect.centery,
                    (140, 215, 255)
                )

    def desenhar(self, tela, camera_x):

        x = self.rect.centerx - camera_x

        if not (-120 < x < tela.get_width() + 120):
            return

        y_base = self.rect.bottom

        # Brilho: fraco com a porta trancada, forte quando há chave
        intensidade = 255 if self.aberta else 90
        intensidade = int(
            intensidade * (0.8 + 0.2 * math.sin(self.tempo * 2))
        )

        brilho = self.brilho.copy()
        brilho.set_alpha(intensidade)

        tela.blit(
            brilho,
            (
                x - brilho.get_width() // 2,
                y_base - self.ALTURA_SPRITE // 2 - brilho.get_height() // 2
            )
        )

        tela.blit(
            self.sprite,
            (
                x - self.LARGURA_SPRITE // 2,
                y_base - self.ALTURA_SPRITE
            )
        )


class Criar_Porta:

    def criar(self, x=2910, y=330):

        return Porta(x, y)
