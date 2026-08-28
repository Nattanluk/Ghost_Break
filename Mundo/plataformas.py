#plataforma.py
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
            (47, 74, 173),
            (
                self.rect.x - camera_x,
                self.rect.y,
                self.rect.width,
                self.rect.height
            )
        )
        
class Criar_Plataforma:

    def criar(self):

        plataformas = []

        # Chão - primeiro trecho
        for x in range(0, 30):
            plataformas.append(
                Plataforma(x * 20, 410, 20, 40)
            )

        # Segundo trecho
        for x in range(38, 70):
            plataformas.append(
                Plataforma(x * 20, 410, 20, 40)
            )

        # Terceiro trecho
        for x in range(80, 130):
            plataformas.append(
                Plataforma(x * 20, 410, 20, 40)
            )

        # Quarto trecho
        for x in range(140, 180):
            plataformas.append(
                Plataforma(x * 20, 410, 20, 40)
            )

        # Plataformas suspensas
        plataformas.append(
            Plataforma(300, 315, 120, 20)
        )

        plataformas.append(
            Plataforma(520, 280, 120, 20)
        )

        plataformas.append(
            Plataforma(800, 230, 150, 20)
        )

        plataformas.append(
            Plataforma(1150, 250, 120, 20)
        )

        plataformas.append(
            Plataforma(1450, 320, 130, 20)
        )

        plataformas.append(
            Plataforma(1750, 290, 150, 20)
        )

        plataformas.append(
            Plataforma(2000, 200, 430, 20)
        )

        plataformas.append(
            Plataforma(2190, 105, 60, 12)
        )

        plataformas.append(
            Plataforma(2650, 280, 90, 20)
        )

        return plataformas