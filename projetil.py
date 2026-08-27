#projetil.py
import pygame

class Projetil:

    def __init__(self, x, y, direcao):

        self.x = x
        self.y = y
        # Tamanho do ataque
        self.largura = 45
        self.altura = 25
        self.velocidade = 10
        self.direcao = direcao     
        # ANIMAÇÃO
        self.frames = []

        nomes_imagens = [
            "imagens/ChatGPT Image 27 de ago. de 2026, 09_33_44.png",
            "imagens/ChatGPT Image 27 de ago. de 2026, 09_35_37.png",
            "imagens/ChatGPT Image 27 de ago. de 2026, 09_32_19.png"
        ]

        for nome in nomes_imagens:

            imagem = pygame.image.load(nome).convert_alpha()
            imagem = pygame.transform.scale(imagem,(self.largura, self.altura))
            self.frames.append(imagem)

        self.frame_atual = 0
        self.tempo_animacao = 0
        self.velocidade_animacao = 5

    def mover(self):

        self.x += self.velocidade * self.direcao

        self.tempo_animacao += 1

        if self.tempo_animacao >= self.velocidade_animacao:

            self.tempo_animacao = 0
            self.frame_atual += 1

            if self.frame_atual >= len(self.frames):
                self.frame_atual = 0

    def desenhar(self, tela, camera_x):

        imagem = self.frames[self.frame_atual]

        # As imagens originais devem apontar para a DIREITA.
        # Se o ataque estiver indo para a esquerda,
        # espelha a imagem.
        if self.direcao < 0:

            imagem = pygame.transform.flip(imagem,True,False)

        # Posição na tela
        pos_x = int(self.x - camera_x)
        pos_y = int(self.y - (self.altura - 8) / 2)

        tela.blit(imagem,(pos_x, pos_y))

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
        )