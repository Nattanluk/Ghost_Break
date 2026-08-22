#porta.py
import pygame

class Porta:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 80)
        
    # Imagem da porta
        self.sprite = pygame.image.load(
            "imagens/porta_pixel_art.png"
        ).convert_alpha()

        # Tamanho da imagem
        self.sprite = pygame.transform.scale(
            self.sprite,
            (50, 80)
        )

    def desenhar(self, tela, camera_x):

        tela.blit(
            self.sprite,
            (
                self.rect.x - camera_x,
                self.rect.y
            )
        )

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
