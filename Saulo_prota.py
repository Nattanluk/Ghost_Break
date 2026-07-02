# Saulo_prota.py
import pygame
from personagem import Personagem


LARGURA_TELA = 800
CHAO_Y = 350


class Saulo(Personagem):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.velocidade = 5
        self.vel_y = 1
        self.f_gravidade = 0.6
        self.forca_pulo = -12
        self.no_chao = False

    def mover(self, teclas):
        tempo_pulo = 0
        if teclas[pygame.K_LEFT]:
            self.pos_x -= self.velocidade

        if teclas[pygame.K_RIGHT]:
            self.pos_x += self.velocidade

        if teclas[pygame.K_UP] and self.no_chao:
            while tempo_pulo < 15:
                self.pos_y += self.forca_pulo
                self.no_chao = False
                tempo_pulo += 1
            self.pos_y -= self.f_gravidade


        if self.pos_x < 0:
            self.pos_x = 0

        if self.pos_x + self.largura > LARGURA_TELA:
            self.pos_x = LARGURA_TELA - self.largura

    def gravidade(self):

        self.vel_y += self.f_gravidade
        self.pos_y += self.vel_y

        if self.pos_y >= CHAO_Y:
            self.pos_y = CHAO_Y
            self.vel_y = 0
            self.no_chao = True

    def update(self, teclas):

        self.mover(teclas)
        self.gravidade()

    def desenhar(self, tela, camera_x):
        pygame.draw.rect(
        tela,
        (255, 255, 0),
        (
            self.pos_x - camera_x,
            self.pos_y,
            self.largura,
            self.altura
        )
    )