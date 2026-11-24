#chave.py
import math

import pygame

from Sistemas.recursos import carregar_escalada
from Sistemas.efeitos import halo


class Chave:

    def __init__(self, x, y):

        # Hitbox generosa (a sprite original é bem pequena)
        self.rect = pygame.Rect(x, y, 40, 40)
        self.coletada = False

        self.imagem = carregar_escalada(
            "imagens/chave.png",
            (54, 27)
        )

        self.brilho = halo(34, (255, 215, 90), 120)

        self.tempo = 0.0

    def atualizar(self, efeitos=None):

        self.tempo += 0.06

        if efeitos is not None and not self.coletada:

            if int(self.tempo * 100) % 9 == 0:

                efeitos.brilho_suave(
                    self.rect.centerx,
                    self.rect.centery,
                    (255, 225, 120)
                )

    def desenhar(self, tela, camera_x):

        if self.coletada:
            return

        flutuacao = math.sin(self.tempo) * 4

        centro_x = self.rect.centerx - camera_x
        centro_y = self.rect.centery + flutuacao

        if not (-60 < centro_x < tela.get_width() + 60):
            return

        pulso = 0.85 + 0.15 * math.sin(self.tempo * 1.7)

        brilho = self.brilho

        tela.blit(
            brilho,
            (
                centro_x - brilho.get_width() // 2,
                centro_y - brilho.get_height() // 2
            )
        )

        # Leve balanço lateral
        angulo = math.sin(self.tempo * 0.8) * 8

        imagem = pygame.transform.rotozoom(
            self.imagem,
            angulo,
            pulso * 0.15 + 0.92
        )

        tela.blit(
            imagem,
            imagem.get_rect(center=(centro_x, centro_y))
        )


class Criar_Chave:

    def criar(self, x=2205, y=85):

        return Chave(x, y)
