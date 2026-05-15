# Saulo_prota.py
import pygame


class Saulo:

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.largura = 40
        self.altura = 60
        self.velocidade = 5
        self.vel_y = 0
        self.f_gravidade = 0.6
        self.forca_pulo = -12
        self.no_chao = False

    def mover(self, teclas):
        if teclas[pygame.K_a]:
            self.pos_x -= self.velocidade

        if teclas[pygame.K_d]:
            self.pos_x += self.velocidade

        if teclas[pygame.K_SPACE] and self.no_chao:
            self.vel_y = self.forca_pulo
            self.no_chao = False

    def gravidade(self):
        self.vel_y += self.f_gravidade
        self.pos_y += self.vel_y

        if self.pos_y >= 300:
            self.pos_y = 300
            self.vel_y = 0
            self.no_chao = True

    def update(self, teclas):
        self.mover(teclas)
        self.gravidade()

    def desenhar(self, tela):

        pygame.draw.rect(
            tela,
            (255, 255, 0),
            (
                self.pos_x,
                self.pos_y,
                self.largura,
                self.altura
            )
        )