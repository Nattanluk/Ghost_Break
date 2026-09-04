import pygame

from Sistemas.desenho_jogo import DesenhoJogo
from Jogador.Saulo_prota import Saulo, BarraVidas
from Telas.menu import Menu
from Mundo.mapa import Mapa
from Telas.gameover import GameOver
from Telas.fase_concluida import FaseConcluida
from Combate.projetil import BarraPlasma, GerenciadorProjeteis
from configuracoes import *
from Sistemas.camera import Camera
from Combate.Colisao import Colisao
from Sistemas.atualizacao_jogo import AtualizacaoJogo


class Jogo:

    def __init__(self):

        pygame.init()

        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Ghost_Break")

        self.clock = pygame.time.Clock()
        self.player = Saulo(*POSICAO_JOGADOR)

        self.mensagem_porta = False
        self.mapa = Mapa()
        self.camera = Camera(LARGURA_MAPA)
        self.projeteis = GerenciadorProjeteis()

        # Sistema de colisão
        self.colisao = Colisao(self)

        self.barra_plasma = BarraPlasma()
        self.barra_vidas = BarraVidas()

        # SCORE
        self.inimigos_derrotados = 0
        self.score = 0

        # TEMPO DA FASE
        self.tempo_inicio = pygame.time.get_ticks()

        self.desenho = DesenhoJogo(self)
        self.atualizacao = AtualizacaoJogo(self)


    def reiniciar_jogo(self):

        # Cria um novo jogador
        self.player = Saulo(*POSICAO_JOGADOR)

        # Remove os projéteis antigos
        self.projeteis = GerenciadorProjeteis()

        # Cria o mapa novamente
        self.mapa = Mapa()

        # Reinicia a câmera
        self.camera = Camera(LARGURA_MAPA)

        # Reinicia o SCORE
        self.inimigos_derrotados = 0
        self.score = 0

        # Reinicia o tempo
        self.tempo_inicio = pygame.time.get_ticks()


    def loop_jogo(self):

        rodando = True

        while rodando:

            self.clock.tick(FPS)

            # EVENTOS
            resultado = self.tratar_eventos()

            if resultado is not None:
                return resultado

            # GAME OVER
            resultado = self.verificar_game_over()

            if resultado == "continuar":
                continue

            if resultado is not None:
                return resultado

            # ATUALIZAÇÃO
            resultado = self.atualizacao.atualizar()

            if resultado == "continuar":
                continue

            if resultado is not None:
                return resultado

            # DESENHO
            self.desenhar_jogo()

            pygame.display.flip()

        return "menu"


    def desenhar_jogo(self):

        self.desenho.desenhar()


    def verificar_porta(self):

        if not self.player.get_rect().colliderect(self.mapa.porta.rect):
            self.mensagem_porta = False
            return None

        if not self.player.tem_chave:
            self.mensagem_porta = True
            return None

        self.mensagem_porta = False

        # Calcula o tempo final da fase
        tempo_final = (
            pygame.time.get_ticks() - self.tempo_inicio
        ) // 1000

        # Abre a tela de fase concluída
        tela_fase = FaseConcluida(
            self.tela,
            self.clock,
            self.inimigos_derrotados,
            tempo_final,
            self.score
        )

        resultado = tela_fase.executar()

        if resultado == "tentar":
            self.reiniciar_jogo()
            return "continuar"

        if resultado == "proxima":
            self.reiniciar_jogo()
            return "menu"

        return resultado


    def verificar_game_over(self):

        if self.player.vida > 0:
            return None

        gameover = GameOver(self)

        resultado = gameover.executar()

        if resultado == "jogar":
            self.reiniciar_jogo()
            return "continuar"

        return resultado


    def tratar_eventos(self):

        for evento in pygame.event.get():

            # Fechar janela
            if evento.type == pygame.QUIT:
                return "sair"

            if evento.type == pygame.KEYDOWN:

                # Pular
                if evento.key in TECLA_PULAR:
                    self.player.pular()

                # Atacar
                if evento.key == TECLA_ATACAR:

                    projetil = self.player.atirar()

                    if projetil is not None:
                        self.projeteis.adicionar(projetil)

                # Reiniciar fase
                if evento.key == TECLA_REINICIAR:
                    self.reiniciar_jogo()

                # Sair
                if evento.key == TECLA_SAIR:
                    return "sair"

        return None


    def iniciar(self):

        menu = Menu(self)

        menu.executar()