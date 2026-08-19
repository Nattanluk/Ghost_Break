import pygame

class Inimigo:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.largura = 40
        self.altura = 60
        self.vida = 1
        self.vivo = True

    def desenhar(self, tela, camera_x):

        if self.vivo:

            pygame.draw.rect(
                tela,
                (255, 0, 0),
                (
                    self.x - camera_x,
                    self.y,
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

    def tomar_dano(self):

        self.vida -= 1

        if self.vida <= 0:
            self.vivo = False