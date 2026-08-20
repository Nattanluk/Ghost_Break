#plataformas.py
import pygame

class Plataforma:

    def __init__(self, x, y, largura, altura):
        self.rect = pygame.Rect(x, y, largura, altura)

    def desenhar(self, tela, camera_x):
        pygame.draw.rect(
            tela, 
            (0, 100, 255),
            (
                self.rect.x - camera_x,
                self.rect.y,
                self.rect.width,
                self.rect.height
            )
        )
