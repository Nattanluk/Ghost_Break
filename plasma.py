#plasma.py
import pygame

class Plasma:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 25, 25)
        self.coletado = False

        self.imagem = pygame.image.load("imagens/Plasmas.png").convert_alpha()

        self.imagem = pygame.transform.scale(self.imagem,(25, 25))

    def desenhar(self, tela, camera_x):

        if not self.coletado:

            tela.blit(
                self.imagem,
                (
                    self.rect.x - camera_x,
                    self.rect.y
                )
            )

    def get_rect(self):
        return self.rect