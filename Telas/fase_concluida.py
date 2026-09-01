#fase_concluida.py
import pygame

class FaseConcluida:

    def __init__(self, tela, clock):

        self.tela = tela
        self.clock = clock
        self.fonte = pygame.font.SysFont("Arial",24)

        largura, altura = self.tela.get_size()

        # Imagem de fundo
        self.fundo = pygame.image.load("imagens/1000323927.png").convert()

        self.fundo = pygame.transform.scale(
            self.fundo,
            (largura, altura)
        )

        # Mesmo tamanho dos botões do menu
        largura_botao = 150
        altura_botao = 50

        # Botão TENTAR NOVAMENTE
        self.botao_tentar = pygame.Rect(340,370,largura_botao,altura_botao)
        # Botão PRÓXIMO
        self.botao_proximo = pygame.Rect(520,370,largura_botao,altura_botao)
        # Botão MENU
        self.botao_menu = pygame.Rect(160,370,largura_botao,altura_botao)

    def desenhar_botao(self, rect, texto):

        mouse = pygame.mouse.get_pos()

        # EXATAMENTE A MESMA COR DO MENU
        if rect.collidepoint(mouse):
            cor = (120, 70, 255, 220)

        else:
            cor = (0, 0, 0, 170)

        # EXATAMENTE A MESMA SUPERFÍCIE
        superficie = pygame.Surface(
            (rect.width, rect.height),
            pygame.SRCALPHA
        )

        # EXATAMENTE O MESMO RETÂNGULO
        pygame.draw.rect(
            superficie,
            cor,
            superficie.get_rect(),
            border_radius=15
        )

        # EXATAMENTE A MESMA BORDA
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

        # EXATAMENTE A MESMA FONTE DOS BOTÕES DO MENU
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
            self.desenhar_botao(self.botao_tentar,"REFAZER")

            self.desenhar_botao(self.botao_proximo,"PRÓXIMO")

            self.desenhar_botao(self.botao_menu,"MENU")


            # EVENTOS
            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    return "sair"

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.botao_tentar.collidepoint(evento.pos):
                        return "tentar"

                    elif self.botao_proximo.collidepoint(evento.pos):
                        return "proxima"

                    elif self.botao_menu.collidepoint(evento.pos):
                        return "menu"

            pygame.display.flip()
            self.clock.tick(60)