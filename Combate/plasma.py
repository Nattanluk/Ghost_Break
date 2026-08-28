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
    
class Criar_Plasmas:

    def criar(self):

        plasmas = [
            Plasma(400, 370),
            Plasma(800, 370),
            Plasma(1000, 190),
            Plasma(1200, 370),
            Plasma(1350, 370),
            Plasma(2200, 370)
        ]

        return plasmas