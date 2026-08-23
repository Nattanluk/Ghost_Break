#porta.py
import pygame

class Porta:

    def __init__(self, x, y):

        # Área de colisão
        self.rect = pygame.Rect(x, y, 50, 80)

        # Sprite
        self.sprite = pygame.image.load(
            "imagens/porta_pixel_art.png"
        ).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.sprite,
            (100, 130)
        )

    def desenhar(self, tela, camera_x):

        tela.blit(
            self.sprite,
            (
                self.rect.x - camera_x - 10,
                self.rect.bottom - self.sprite.get_height()
            )
        )

