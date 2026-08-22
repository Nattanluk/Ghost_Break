#chave.py
import pygame

class Chave:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.coletada = False
        
        self.imagem = pygame.image.load(
            "imagens/chave.png"
        ).convert_alpha()

    def desenhar(self, tela, camera_x):

        if not self.coletada: 
            tela.blit(
                self.imagem,
                (
                    self.rect.x - camera_x,
                    self.rect.y
                )
            )
