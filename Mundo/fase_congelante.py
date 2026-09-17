#fase_congelante.py
import pygame

from Mundo.plataformas import Criar_Plataforma
from Mundo.porta import Criar_Porta
from Mundo.chave import Criar_Chave
from Combate.inimigo import Criar_Inimigos
from Combate.plasma import Criar_Plasmas


class Mapa:

    def __init__(self):
        # Trechos de chão
        #
        # Cada tupla representa:
        # (inicio, fim)
        #
        # Os espaços entre os números são buracos.
        dados_chao = [
            (0, 5),       # Começo
            (8, 25),
            (29, 42),     # Área depois da subida
            (46, 61),     # Corredor
            (65, 82),     # Área central
            (87, 105),    # Caminho inferior
            (110, 130),   # Caminho até o final
            (135, 150)    # Área da porta
        ]

        # Plataformas suspensas
        #
        # Formato:
        # (x, y, largura, altura)
        dados_plataformas = [

            # ==================================
            # COMEÇO DA FASE
            # ==================================

            # Subida em degraus
            (180, 340, 90, 50),
            (265, 315, 90, 50),
            (335, 290, 90, 50),
            (405, 265, 130, 50),

            # ==================================
            # ÁREA ALTA
            # ==================================

            # Grande plataforma superior
            (560, 220, 180, 50),

            # Pequena plataforma de passagem
            (780, 270, 100, 50),

            # ==================================
            # TORRE / ÁREA CENTRAL
            # ==================================

            # Plataforma grande vertical
            (900, 170, 140, 50),

            # Plataforma na lateral
            (1050, 240, 120, 50),

            # Plataforma inferior
            (1180, 310, 150, 50),

            # ==================================
            # CORREDOR
            # ==================================

            (1370, 250, 180, 50),

            (1600, 300, 130, 50),

            # ==================================
            # ÁREA DE DESCIDA
            # ==================================

            (1780, 350, 160, 50),

            (1980, 280, 130, 50),

            # ==================================
            # ÁREA DA CHAVE
            # ==================================

            # Plataforma onde fica a chave
            (2160, 200, 160, 50),

            # Plataforma para alcançar a área da chave
            (2050, 280, 100, 50),

            # ==================================
            # CAMINHO FINAL
            # ==================================

            (2340, 300, 150, 50),

            (2530, 250, 150, 50),

            (2720, 320, 150, 50),

            # Plataforma final próxima da porta
            (2880, 330, 120, 50)
        ]

        # ==========================================
        # CRIA AS PLATAFORMAS
        # ==========================================

        self.plataformas = Criar_Plataforma().criar(
            dados_plataformas,
            dados_chao
        )

        # ==========================================
        # PORTA
        # ==========================================

        self.porta = Criar_Porta().criar()

        # ==========================================
        # CHAVE
        # ==========================================

        self.chave = Criar_Chave().criar()

        # ==========================================
        # INIMIGOS
        # ==========================================

        self.inimigos = Criar_Inimigos().criar()

        # ==========================================
        # PLASMAS
        # ==========================================

        self.plasmas = Criar_Plasmas().criar()

    def desenhar(self, tela, camera_x):

        # ==========================================
        # PLATAFORMAS
        # ==========================================

        for plataforma in self.plataformas:

            plataforma.desenhar(
                tela,
                camera_x
            )

        # ==========================================
        # INIMIGOS
        # ==========================================

        for inimigo in self.inimigos:

            inimigo.desenhar(
                tela,
                camera_x
            )

        # ==========================================
        # PORTA
        # ==========================================

        self.porta.desenhar(
            tela,
            camera_x
        )

        # ==========================================
        # CHAVE
        # ==========================================

        self.chave.desenhar(
            tela,
            camera_x
        )

        # ==========================================
        # PLASMAS
        # ==========================================

        for plasma in self.plasmas:

            plasma.desenhar(
                tela,
                camera_x
            )

    def desenhar_mensagem_porta(
        self,
        tela,
        largura_tela,
        altura_tela
    ):

        fonte = pygame.font.SysFont(
            "Arial",
            22,
            bold=True
        )

        texto = fonte.render(
            "Você precisa da chave!",
            True,
            (255, 255, 255)
        )

        largura_caixa = texto.get_width() + 40
        altura_caixa = texto.get_height() + 20

        x = (largura_tela - largura_caixa) // 2
        y = altura_tela - altura_caixa - 20

        # ==========================================
        # FUNDO DA MENSAGEM
        # ==========================================

        pygame.draw.rect(
            tela,
            (15, 20, 30),
            (
                x,
                y,
                largura_caixa,
                altura_caixa
            ),
            border_radius=8
        )

        # ==========================================
        # BORDA
        # ==========================================

        pygame.draw.rect(
            tela,
            (80, 180, 255),
            (
                x,
                y,
                largura_caixa,
                altura_caixa
            ),
            2,
            border_radius=8
        )

        # ==========================================
        # TEXTO
        # ==========================================

        texto_x = x + (
            largura_caixa - texto.get_width()
        ) // 2

        texto_y = y + (
            altura_caixa - texto.get_height()
        ) // 2

        tela.blit(
            texto,
            (
                texto_x,
                texto_y
            )
        )