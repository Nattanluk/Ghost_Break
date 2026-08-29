#plasma.py
import pygame


class Plasma:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 25, 25)
        self.coletado = False

        # ANIMAÇÃO
        self.frames = [
            pygame.image.load("imagens/plasma_frame_1.png").convert_alpha(),
            pygame.image.load("imagens/plasma_frame_2.png").convert_alpha(),
            pygame.image.load("imagens/plasma_frame_3.png").convert_alpha(),
            pygame.image.load("imagens/plasma_frame_4.png").convert_alpha(),
            pygame.image.load("imagens/plasma_frame_5.png").convert_alpha()
        ]

        # Tamanho dos frames
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(
                self.frames[i],
                (30, 40)
            )

        self.frame_atual = 0
        self.tempo_animacao = 0
        self.velocidade_animacao = 250

    def atualizar(self):

        self.tempo_animacao += 1

        if self.tempo_animacao >= self.velocidade_animacao // 60:

            self.tempo_animacao = 0

            self.frame_atual += 1

            if self.frame_atual >= len(self.frames):
                self.frame_atual = 0

    def desenhar(self, tela, camera_x):

        if not self.coletado:

            tela.blit(
                self.frames[self.frame_atual],
                (
                    self.rect.x - camera_x,
                    self.rect.y
                )
            )

    def get_rect(self):
        return self.rect
    
class Criar_Plasmas:

    def criar(self):

        plasmas = [
            Plasma(400, 365),
            Plasma(800, 365),
            Plasma(1000, 190),
            Plasma(1200, 365),
            Plasma(1350, 365),
            Plasma(2200, 365)
        ]

        return plasmas