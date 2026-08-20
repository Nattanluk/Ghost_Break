#porta.py
import pygame

class Porta:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 80)

    def desenhar(self, tela, camera_x):
        pygame.draw.rect(
            tela,
            (139, 69, 19),   # Marrom
            (
                self.rect.x - camera_x,
                self.rect.y,
                self.rect.width,
                self.rect.height
            )
        )
