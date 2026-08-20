#projetil.py
import pygame

class Projetil:

    def __init__(self, x, y, direcao):

        self.x = x
        self.y = y

        self.largura = 15
        self.altura = 8

        self.velocidade = 10
        self.direcao = direcao

    def mover(self):

        self.x += self.velocidade * self.direcao

    def desenhar(self, tela, camera_x):

        pygame.draw.rect(
            tela,
            (0, 255, 255),
            (
                int(self.x - camera_x),
                int(self.y),
                self.largura,
                self.altura
            )
        )

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
        )

