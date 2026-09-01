# plataforma.py
import pygame


class Plataforma:

    def __init__(self, x, y, largura, altura, imagem):
        # Área visual
        self.rect = pygame.Rect(x, y, largura, altura)

        # Área de colisão
        self.rect_colisao = pygame.Rect(
            x - 15,
            y,
            largura + 15,
            altura
        )

        # Sprite da plataforma
        self.imagem = pygame.transform.scale(
            imagem,
            (largura, altura)
        )

    def desenhar(self, tela, camera_x):
        tela.blit(
            self.imagem,
            (
                self.rect.x - camera_x,
                self.rect.y
            )
        )


class Criar_Plataforma:

    def __init__(self):
        # Carrega a sprite uma única vez
        self.sprite_plataforma = pygame.image.load("imagens/1000328238.png").convert_alpha()

    def criar(self):

        plataformas = []

        # Chão - primeiro trecho
        for x in range(0, 30):
            plataformas.append(Plataforma(x * 20 , 410, 20, 40,self.sprite_plataforma))

        # Segundo trecho
        for x in range(38, 70):
            plataformas.append(
                Plataforma(
                    x * 20,
                    410,
                    20,
                    40,
                    self.sprite_plataforma
                )
            )

        # Terceiro trecho
        for x in range(80, 130):
            plataformas.append(
                Plataforma(
                    x * 20,
                    410,
                    20,
                    40,
                    self.sprite_plataforma
                )
            )

        # Quarto trecho
        for x in range(140, 180):
            plataformas.append(
                Plataforma(
                    x * 20,
                    410,
                    20,
                    40,
                    self.sprite_plataforma
                ))

        # Plataformas suspensas
        plataformas.append(Plataforma(300, 305, 130, 50, self.sprite_plataforma))

        plataformas.append(Plataforma(520, 280, 130, 50, self.sprite_plataforma))

        plataformas.append(Plataforma(800, 230, 180, 50, self.sprite_plataforma))

        plataformas.append(Plataforma(1150, 250, 150, 50, self.sprite_plataforma))

        plataformas.append(Plataforma(1450, 320, 140, 50, self.sprite_plataforma))

        plataformas.append(Plataforma(1750, 290, 160, 50, self.sprite_plataforma))

        plataformas.append(Plataforma(2000, 200, 440, 50, self.sprite_plataforma))

        plataformas.append(Plataforma(2190, 105, 40, 32, self.sprite_plataforma))

        plataformas.append(Plataforma(2650, 280, 100, 50, self.sprite_plataforma))

        return plataformas
