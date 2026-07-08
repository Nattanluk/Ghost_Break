import pygame

class Chave:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.coletada = False

    def desenhar(self, tela, camera_x):

        if not self.coletada:
            pygame.draw.rect(
                tela,
                (255, 215, 0),   # Dourado
                (
                    self.rect.x - camera_x,
                    self.rect.y,
                    self.rect.width,
                    self.rect.height
                )
            )