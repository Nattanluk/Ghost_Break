#plasma.py
import pygame


class Plasma:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.coletado = False

    def desenhar(self, tela, camera_x):

        if not self.coletado:

            pygame.draw.circle(
                tela,
                (0, 255, 255),
                (
                    self.rect.centerx - camera_x,
                    self.rect.centery
                ),
                12
            )

    def get_rect(self):
        return self.rect