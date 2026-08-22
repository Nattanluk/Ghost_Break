import pygame

class Plataforma:

    def __init__(self, x, y, largura, altura):
        # Área visual
        self.rect = pygame.Rect(x, y, largura, altura)

        # Área de colisão
        self.rect_colisao = pygame.Rect(
            x - 15,      # 15 pixels para a esquerda
            y,
            largura + 15,
            altura
        )

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