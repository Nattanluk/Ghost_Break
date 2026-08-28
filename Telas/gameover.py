#gameover.py
import pygame

class GameOver:

    def __init__(self, jogo):

        self.jogo = jogo
        self.tela = jogo.tela
        self.fonte = pygame.font.SysFont("Arial",15)
        largura, altura = self.tela.get_size()

        # Imagem de fundo
        self.fundo = pygame.image.load("imagens/1000323722.png").convert()

        self.fundo = pygame.transform.scale(
            self.fundo,
            (largura, altura)
        )

        # Tamanho dos botões
        largura_botao = 150
        altura_botao = 50

        # Botão JOGAR NOVAMENTE
        self.botao_jogar = pygame.Rect(140, 270, largura_botao, altura_botao)

        # Botão MENU PRINCIPAL
        self.botao_menu = pygame.Rect(500, 270, largura_botao, altura_botao)


    def desenhar_botao(self, rect, texto):
        mouse = pygame.mouse.get_pos()

        # Mesmo efeito do menu
        if rect.collidepoint(mouse):
            cor = (120, 70, 255, 220)

        else:
            cor = (0, 0, 0, 170)

        superficie = pygame.Surface(
            (rect.width, rect.height),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            superficie,
            cor,
            superficie.get_rect(),
            border_radius=15
        )

        # Borda branca
        pygame.draw.rect(
            superficie,
            (255, 255, 255),
            superficie.get_rect(),
            2,
            border_radius=15
        )

        self.tela.blit(
            superficie,
            rect.topleft
        )

        # Texto
        texto_render = self.fonte.render(
            texto,
            True,
            (255, 255, 255)
        )

        texto_rect = texto_render.get_rect(
            center=rect.center
        )

        self.tela.blit(
            texto_render,
            texto_rect
        )

    def executar(self):

        while True:

            # FUNDO
            self.tela.blit(
                self.fundo,
                (0, 0)
            )

            # BOTÕES
            self.desenhar_botao(
                self.botao_jogar,
                "JOGAR NOVAMENTE"
            )

            self.desenhar_botao(
                self.botao_menu,
                "MENU PRINCIPAL"
            )

            # EVENTOS
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "sair"
                
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    # JOGAR NOVAMENTE
                    if self.botao_jogar.collidepoint(evento.pos):
                        return "jogar"

                    # MENU PRINCIPAL
                    elif self.botao_menu.collidepoint(evento.pos):
                        return "menu"

            pygame.display.flip()
            self.jogo.clock.tick(60)