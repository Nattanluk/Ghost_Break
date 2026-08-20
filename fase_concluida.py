#fase_concluida.py
import pygame


class FaseConcluida:

    def __init__(self, tela, clock):
        self.tela = tela
        self.clock = clock

        self.fonte_titulo = pygame.font.SysFont(
            "Arial", 50, bold=True
        )

        self.fonte_texto = pygame.font.SysFont(
            "Arial", 25
        )

    def executar(self):

        while True:

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    return "sair"

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_RETURN:
                        return "proxima"

                    if evento.key == pygame.K_ESCAPE:
                        return "menu"

            # Fundo
            self.tela.fill((10, 10, 25))

            # Título
            titulo = self.fonte_titulo.render(
                "FASE CONCLUÍDA!",
                True,
                (255, 255, 255)
            )

            self.tela.blit(
                titulo,
                titulo.get_rect(
                    center=(400, 150)
                )
            )

            # Texto
            texto = self.fonte_texto.render(
                "Você encontrou a saída da fase!",
                True,
                (200, 200, 200)
            )

            self.tela.blit(
                texto,
                texto.get_rect(
                    center=(400, 230)
                )
            )

            # Instruções
            continuar = self.fonte_texto.render(
                "ENTER - Próxima fase",
                True,
                (255, 255, 255)
            )

            menu = self.fonte_texto.render(
                "ESC - Voltar ao menu",
                True,
                (255, 255, 255)
            )

            self.tela.blit(
                continuar,
                continuar.get_rect(
                    center=(400, 310)
                )
            )

            self.tela.blit(
                menu,
                menu.get_rect(
                    center=(400, 350)
                )
            )

            pygame.display.flip()

            self.clock.tick(60)
