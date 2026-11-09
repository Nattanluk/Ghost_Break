# GhostBreak – O Despertar do Esquecido

Projeto de desenvolvimento de um jogo da matéria de POO – Programação Orientada a Objetos.

\--------------------------------------------

# Como Executar o Projeto

Para executar o jogo corretamente, siga os passos abaixo:

## Pré-requisitos

Certifique-se de possuir instalado em seu computador:

- Python
- Biblioteca Pygame

## Instalação das Dependências

Abra o terminal e execute o comando abaixo para instalar o Pygame:

```
python -m pip install pygame
```

## Execução do Jogo

1. Faça o download ou clone o repositório do projeto;
2. Certifique-se de que as pastas e os arquivos estejam organizados corretamente;
3. Abra o terminal dentro da pasta principal do projeto;
4. Execute o arquivo principal utilizando o comando:

```
python main_jogo.py
```

Após a execução, o jogo será iniciado automaticamente.

\--------------------------------------------

# Tecnologias e Bibliotecas Utilizadas

O projeto foi desenvolvido utilizando a linguagem Python e a biblioteca Pygame para construção da interface gráfica, movimentação dos personagens, colisões e mecânicas do jogo.

## Tecnologias

- Python
- Pygame
- Programação Orientada a Objetos

## Bibliotecas Utilizadas

| Biblioteca | Função                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------- |
| pygame     | Criação da janela, renderização gráfica, movimentação, colisões, eventos e controle do jogo |
| os         | Manipulação de arquivos e diretórios, quando necessário                                     |
| math       | Cálculos matemáticos utilizados na movimentação e animação do personagem                    |

\--------------------------------------------

# Título do Jogo

GhostBreak

O Despertar do Esquecido

\--------------------------------------------

# Descrição Geral

GhostBreak é um jogo de plataforma dos gêneros aventura, fantasia e mistério.

O jogo se passa em uma masmorra extensa, na qual o jogador controla um fantasma chamado Saulo. Durante a jornada, o personagem precisa atravessar plataformas, enfrentar inimigos, coletar plasmas e encontrar uma chave para liberar a saída.

O jogo possui uma tela inicial, seleção de níveis, sistema de combate, controle de vidas, pontuação e telas de conclusão e Game Over.

Atualmente, existem dois mapas com construções próprias: Eterno e Congelante. A seleção apresenta cinco níveis, mas os níveis 3, 4 e 5 ainda reutilizam o mapa Eterno, pois seus cenários específicos não estão implementados.

\--------------------------------------------

# Objetivo do Jogo

O objetivo do jogador é atravessar os níveis da masmorra, superar os desafios encontrados e alcançar a saída de cada fase.

Para concluir uma fase, o jogador deve encontrar e coletar a chave presente no mapa. Depois disso, precisa alcançar o portão de saída.

Os inimigos podem ser derrotados utilizando os projéteis de plasma, mas derrotá-los não é obrigatório para concluir a fase.

A progressão acontece por meio da conclusão dos níveis. Ao finalizar uma fase, o próximo nível é desbloqueado.

\--------------------------------------------

# Personagem Principal

O personagem principal é um fantasma chamado Saulo, que precisa atravessar a masmorra enfrentando diferentes desafios.

Ele possui movimentação de plataforma, podendo andar para a esquerda e para a direita, pular sobre plataformas e atacar inimigos utilizando projéteis de plasma.

## Atributos do personagem

- Vidas: 3 por fase;
- Velocidade horizontal: 5 unidades por atualização;
- Pulo: realizado por meio de uma força vertical;
- Gravidade: aplicada durante a movimentação;
- Ataque: utilização de projéteis de plasma;
- Invulnerabilidade: temporária após receber dano;
- Flutuação: pequena animação vertical durante a movimentação.

Para atacar, o jogador deve coletar pelo menos 3 plasmas, que são consumidos a cada disparo.

\--------------------------------------------

# Inimigos e Obstáculos

O jogo possui inimigos com movimentação própria, animações e pontos de vida.

Os inimigos se movimentam em áreas determinadas por limites de patrulha e podem causar dano ao personagem por contato.

Na fase Congelante, os inimigos também possuem a capacidade de realizar disparos contra o jogador.

O personagem pode derrotar os inimigos utilizando seus projéteis de plasma. Cada inimigo derrotado acrescenta 100 pontos à pontuação.

## Obstáculos

- Plataformas suspensas que exigem saltos para atravessar o cenário;
- Trechos de chão separados por áreas vazias;
- Inimigos que causam dano por contato;
- Projéteis disparados pelos inimigos na fase Congelante;
- Quedas para fora da área visível do cenário, que levam à condição de Game Over.

\--------------------------------------------

# Cenário (Mapa)

As fases possuem estrutura de plataforma e extensão maior que a tela do jogo. O jogador avança pelo cenário utilizando movimentação horizontal e saltos.

Para acompanhar o personagem durante a exploração, foi implementado um sistema de câmera horizontal.

## Elementos do mapa

- Chave: item coletável necessário para liberar a saída;
- Portão de saída: localizado ao final do cenário;
- Plasmas: itens coletáveis utilizados como recurso para os ataques;
- Plataformas: estruturas utilizadas para movimentação e saltos;
- Trechos de chão: superfícies que permitem ao personagem se movimentar;
- Inimigos: personagens que oferecem desafios durante a exploração.

## Níveis da masmorra

### Eterno

Primeiro mapa do jogo. Possui plataformas, trechos de chão, inimigos, plasmas, chave e portão de saída.

### Congelante

Segundo mapa do jogo. Possui uma organização própria de plataformas e inimigos que também podem realizar disparos contra o personagem.

Obs.: Os nomes ainda serão trocados
\--------------------------------------------

# Sistema de Pontuação

O jogador acumula pontos ao derrotar inimigos durante as fases.

| Ação              | Pontuação  |
| ----------------- | ---------- |
| Derrotar inimigos | 100 pontos |

O jogo também registra a quantidade de inimigos derrotados e o tempo utilizado para concluir a fase.

Essas informações são apresentadas na tela de fase concluída.

\--------------------------------------------

# Sistema de Vida

O jogador inicia cada fase com 3 vidas.

Ao encostar em um inimigo ou ser atingido por um projétil inimigo, Saulo perde uma vida.

Após receber dano, o personagem recebe um período temporário de invulnerabilidade, evitando que sofra danos consecutivos durante esse intervalo.

Caso o personagem caia para fora da área do cenário, sua vida é zerada e a tela de Game Over é apresentada.

Na tela de Game Over, o jogador pode tentar novamente ou retornar ao menu principal.

\--------------------------------------------

# Controles

## Movimentação

| Tecla | Função                       |
| ----- | ---------------------------- |
| A / ← | Movimentação para a esquerda |
| D / → | Movimentação para a direita  |

## Pulo

| Tecla  | Função |
| ------ | ------ |
| Espaço | Pular  |
| W      | Pular  |
| ↑      | Pular  |

## Ações

| Tecla | Função            |
| ----- | ----------------- |
| S     | Ataque com plasma |
| R     | Reiniciar a fase  |
| Esc   | Sair do jogo      |

\-----------------------------------------------

# Fluxo do Jogo

1. O jogo inicia apresentando o menu principal;
2. O jogador pode iniciar a partida, acessar os créditos ou sair;
3. Ao selecionar a opção de jogar, é apresentada a tela de seleção de níveis;
4. O primeiro nível fica desbloqueado inicialmente;
5. Durante a partida, o jogador explora o mapa, coleta plasmas e enfrenta inimigos;
6. O jogador precisa encontrar a chave para liberar o portão de saída;
7. Ao alcançar o portão com a chave, a fase é concluída;
8. É apresentada uma tela com a quantidade de inimigos derrotados, o tempo e a pontuação;
9. O jogador pode refazer a fase, avançar para o próximo nível ou retornar ao menu;
10. Ao concluir uma fase, o próximo nível é desbloqueado;
11. Caso todas as vidas acabem, a tela de Game Over permite tentar novamente ou retornar ao menu.

\--------------------------------------------

# Regras do Jogo

- O jogador inicia cada fase com 3 vidas;
- A chave é obrigatória para liberar o portão de saída;
- O jogador precisa possuir pelo menos 3 plasmas para realizar um ataque;
- Cada disparo consome exatamente 3 plasmas;
- Os inimigos podem ser derrotados utilizando os projéteis do jogador;
- Não é obrigatório derrotar todos os inimigos para concluir uma fase;
- Ao receber dano, o personagem fica temporariamente invulnerável;
- Cada inimigo derrotado acrescenta 100 pontos à pontuação;
- O jogador precisa alcançar o portão após coletar a chave para concluir a fase;
- Cair para fora da área do cenário zera as vidas do personagem;
- A progressão desbloqueia o próximo nível após a conclusão da fase.

\--------------------------------------------

# Estrutura do Projeto

```
Ghost_Break-main/
│
├── main_jogo.py
├── game.py
├── configuracoes.py
│
├── Combate/
│   ├── Colisao.py
│   ├── inimigo.py
│   ├── plasma.py
│   └── projetil.py
│
├── Jogador/
│   ├── Saulo_prota.py
│   └── personagem.py
│
├── Mundo/
│   ├── chave.py
│   ├── mapa.py
│   ├── mapa2.py
│   ├── plataformas.py
│   └── porta.py
│
├── Sistemas/
│   ├── atualizacao_jogo.py
│   ├── camera.py
│   └── desenho_jogo.py
│
├── Telas/
│   ├── fase_concluida.py
│   ├── gameover.py
│   ├── menu.py
│   └── selecao_niveis.py
│
├── imagens/
│   └── Sprites, cenários e elementos gráficos
│
└── README.md
```

## Responsabilidade dos arquivos

- `main_jogo.py` → inicialização e execução do jogo;
- `game.py` → controle principal, gerenciamento das fases e fluxo da partida;
- `configuracoes.py` → configurações da janela, dimensões do mapa, FPS e controles;
- `Jogador/personagem.py` → classe base do personagem;
- `Jogador/Saulo_prota.py` → movimentação, pulo, vidas, ataques e características de Saulo;
- `Combate/inimigo.py` → comportamento, movimentação, animações e ataques dos inimigos;
- `Combate/plasma.py` → criação e gerenciamento dos plasmas coletáveis;
- `Combate/projetil.py` → projéteis do jogador, projéteis dos inimigos e interface da barra de plasma;
- `Combate/Colisao.py` → tratamento das colisões entre jogador, inimigos, projéteis e itens;
- `Mundo/chave.py` → criação e gerenciamento da chave;
- `Mundo/porta.py` → criação e gerenciamento do portão de saída;
- `Mundo/plataformas.py` → criação das plataformas e dos trechos de chão;
- `Mundo/mapa.py` → construção do mapa Congelante;
- `Mundo/mapa2.py` → construção do mapa Eterno;
- `Sistemas/atualizacao_jogo.py` → atualização dos elementos durante a partida;
- `Sistemas/camera.py` → acompanhamento horizontal do personagem pelo cenário;
- `Sistemas/desenho_jogo.py` → renderização dos elementos na tela;
- `Telas/menu.py` → menu principal e tela de créditos;
- `Telas/selecao_niveis.py` → seleção e desbloqueio dos níveis;
- `Telas/fase_concluida.py` → apresentação dos resultados e opções após concluir uma fase;
- `Telas/gameover.py` → apresentação da tela de Game Over.

\--------------------------------------------

# Funcionalidades Mínimas

- Sistema de movimentação do jogador;
- Sistema de pulo e gravidade;
- Sistema de colisão com plataformas;
- Sistema de câmera;
- Sistema de coleta de plasmas;
- Sistema de ataque com projéteis;
- Sistema de inimigos com movimentação e animação;
- Sistema de disparos dos inimigos na fase Congelante;
- Sistema de colisão com inimigos e perda de vida;
- Sistema de invulnerabilidade temporária;
- Sistema de chave e portão;
- Sistema de pontuação;
- Sistema de seleção e desbloqueio de níveis;
- Tela de conclusão de fase;
- Tela de Game Over;
- Sistema de reinício da fase.

\--------------------------------------------

# Melhorias Futuras

- Implementação dos mapas próprios das fases Escaldante, Desértica e Bestial;
- Desenvolvimento do nível Carmesim e inclusão na seleção de níveis;
- Criação de novos tipos de inimigos com comportamentos diferentes;
- Implementação de obstáculos específicos para cada cenário;
- Desenvolvimento de novas habilidades para o personagem;
- Aprimoramento das animações dos personagens e inimigos;
- Melhorias visuais nos níveis, com mais detalhes e ambientação;
- Implementação de novas mecânicas para diferenciar os níveis;
- Aprimoramento do sistema de progressão entre as fases.

\--------------------------------------------

# Créditos

Projeto desenvolvido para a disciplina de POO – Programação Orientada a Objetos.

Instituição: IFRN

Curso/Turma: Informática – 2º Ano 2M

Professor: Max Miller

Desenvolvedores:

- Sofia Sabina Azevedo Nóbrega
- Nataniel M. Lucena dos Santos

\--------------------------------------------