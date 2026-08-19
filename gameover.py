import pygame

class GameOver:

    def __init__(self, jogo):

        # Guarda o jogo para usar a mesma tela
        self.jogo = jogo

        self.fonte_titulo = pygame.font.SysFont(
            "Arial",
            60,
            bold=True
        )

        self.fonte = pygame.font.SysFont(
            "Arial",
            24
        )

    def executar(self):

        while True:

            # Fundo da tela
            self.jogo.tela.fill((20, 20, 20))

            # Título
            titulo = self.fonte_titulo.render(
                "GAME OVER",
                True,
                (255, 255, 255)
            )

            # Opção para jogar novamente
            jogar = self.fonte.render(
                "ENTER - Jogar novamente",
                True,
                (255, 255, 255)
            )

            # Opção para voltar ao menu
            menu = self.fonte.render(
                "ESC - Menu principal",
                True,
                (255, 255, 255)
            )

            # Desenha o título no centro
            titulo_rect = titulo.get_rect(
                center=(400, 120)
            )

            self.jogo.tela.blit(
                titulo,
                titulo_rect
            )

            # Desenha a opção de jogar
            jogar_rect = jogar.get_rect(
                center=(400, 220)
            )

            self.jogo.tela.blit(
                jogar,
                jogar_rect
            )

            # Desenha a opção de voltar ao menu
            menu_rect = menu.get_rect(
                center=(400, 270)
            )

            self.jogo.tela.blit(
                menu,
                menu_rect
            )

            pygame.display.flip()

            # Verifica os eventos
            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    return "sair"

                if evento.type == pygame.KEYDOWN:

                    # ENTER = jogar novamente
                    if evento.key == pygame.K_RETURN:
                        return "jogar"

                    # ESC = voltar para o menu
                    if evento.key == pygame.K_ESCAPE:
                        return "menu"

            self.jogo.clock.tick(60)