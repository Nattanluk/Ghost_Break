import pygame
import sys


class SelecaoNiveis:

    def __init__(self, jogo):

        self.jogo = jogo
        self.tela = jogo.tela

        # FONTES
        self.fonte_titulo = pygame.font.SysFont("Arial", 40, bold=True)
        self.fonte_nivel = pygame.font.SysFont("Arial", 15, bold=True)
        self.fonte_bloqueado = pygame.font.SysFont("Arial", 15, bold=True)
        self.fonte_voltar = pygame.font.SysFont("Arial", 20, bold=True)

        # FUNDO
        self.fundo = pygame.image.load("imagens/fases.jpg").convert()
        self.fundo = pygame.transform.scale(self.fundo, self.tela.get_size())

        # BOTÕES DOS NÍVEIS
        self.botoes = [
            pygame.Rect(100, 130, 160, 60), 
            pygame.Rect(310, 130, 160, 60), 
            pygame.Rect(520, 130, 160, 60), 
            pygame.Rect(100, 230, 160, 60), 
            pygame.Rect(310, 230, 160, 60), 
            pygame.Rect(520, 230, 160, 60)]

        # BOTÃO VOLTAR
        self.botao_voltar = pygame.Rect(300, 350, 200, 55)

        # NÍVEIS DESBLOQUEADOS
        self.niveis_desbloqueados = self.jogo.niveis_desbloqueados

    def desenhar_botao(self, rect, texto, desbloqueado=True):

        mouse = pygame.mouse.get_pos()

        # BOTÃO DESBLOQUEADO
        if desbloqueado:
            if rect.collidepoint(mouse):
                cor = (120, 70, 255, 220)
            else:
                cor = (0, 0, 0, 180)

        # BOTÃO BLOQUEADO
        else:
            cor = (35, 35, 45, 220)

        superficie = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)

        pygame.draw.rect(superficie, cor, superficie.get_rect(), border_radius=15)
        pygame.draw.rect(superficie, (255, 255, 255), superficie.get_rect(), 2, border_radius=15)

        self.tela.blit(superficie, rect.topleft)

        # TEXTO
        if desbloqueado:
            texto_render = self.fonte_nivel.render(texto, True, (255, 255, 255))
        else:
            texto_render = self.fonte_bloqueado.render("BLOQUEADO", True, (160, 160, 160))

        texto_rect = texto_render.get_rect(center=rect.center)

        self.tela.blit(texto_render, texto_rect)

    def executar(self):

        while True:

            # FUNDO
            self.tela.blit(self.fundo, (0, 0))

            # SOMBRA
            sombra = pygame.Surface(self.tela.get_size(), pygame.SRCALPHA)
            sombra.fill((0, 0, 0, 50))
            self.tela.blit(sombra, (0, 0))

            # TÍTULO
            titulo = self.fonte_titulo.render("SELEÇÃO DE NÍVEIS", True, (255, 255, 255))
            titulo_rect = titulo.get_rect(center=(400, 65))
            self.tela.blit(titulo, titulo_rect)

            # BOTÕES DOS NÍVEIS
            for i, botao in enumerate(self.botoes):
                numero_nivel = i + 1
                self.desenhar_botao(botao, f"NÍVEL {numero_nivel}", self.niveis_desbloqueados[i])

            # BOTÃO VOLTAR
            self.desenhar_botao(self.botao_voltar, "VOLTAR", True)

            # EVENTOS
            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    # NÍVEIS
                    for i, botao in enumerate(self.botoes):

                        if botao.collidepoint(evento.pos):

                            if self.niveis_desbloqueados[i]:

                                self.jogo.fase_atual = i + 1
                                self.jogo.reiniciar_jogo()
                                return self.jogo.loop_jogo()

                    # VOLTAR
                    if self.botao_voltar.collidepoint(evento.pos):
                        return

            pygame.display.flip()

            self.jogo.clock.tick(60)