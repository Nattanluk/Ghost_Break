# GhostBreak – O Despertar do Esquecido

Projeto de desenvolvimento de um jogo da matéria de POO-Programação Orientada a Objeto 

--------------------------------------------

# Como Executar o Projeto

Para executar o jogo corretamente, siga os passos abaixo:

## Pré-requisitos

Certifique-se de possuir instalado em seu computador:

- Python 3.8 até Python 3.12
- Biblioteca Pygame

## Instalação das Dependências

Abra o terminal e execute o comando abaixo para instalar o Pygame:

```bash
pip install pygame
```

## Execução do Jogo

1. Faça o download ou clone o repositório do projeto;
2. Certifique-se de que todos os arquivos estejam na mesma pasta;
3. Abra o terminal dentro da pasta do projeto;
4. Execute o arquivo principal utilizando o comando:

```bash
python main_jogo.py
```

Após a execução, o jogo será iniciado automaticamente.

--------------------------------------------

# Tecnologias e Bibliotecas Utilizadas

O projeto foi desenvolvido utilizando a linguagem Python e a biblioteca Pygame para construção da interface gráfica e mecânicas do jogo.

## Tecnologias

- Python
- Pygame

## Bibliotecas Utilizadas

| Biblioteca | Função |
|----------------------|
| pygame | Renderização gráfica, movimentação, colisões e controle do jogo |
| os | Manipulação de arquivos e diretórios do sistema |
| random | Geração de comportamentos aleatórios e eventos do jogo |

--------------------------------------------

# Título do Jogo

GhostBreak  
O Despertar do Esquecido

--------------------------------------------

# Descrição Geral

GhostBreak é um jogo de plataforma dos gêneros aventura, fantasia e mistério.

O jogo se passa em uma masmorra extensa, composta por seis níveis distintos: Eterno, Congelante, Escaldante, Desértico, Bestial e Carmesim, cada um com características próprias, inimigos e desafios que aumentam a dificuldade ao longo da progressão.

A ideia principal é que o jogador controle um fantasma chamado Saulo, que precisa escapar da masmorra enfrentando obstáculos e guardas ao longo do caminho. Para derrotar os inimigos, será necessário coletar plasmas espalhados pelo cenário, permitindo a realização de ataques. Ao final da jornada, o personagem recupera suas memórias perdidas e conquista sua liberdade.

--------------------------------------------

# Objetivo do Jogo

O objetivo do jogador é escapar da masmorra, atravessando todos os seis níveis e recuperando suas memórias ao final da jornada.

Para concluir cada fase, o jogador deve encontrar uma chave escondida no mapa e levá-la até o portão de saída.

Para avançar de fase, o jogador precisa possuir pelo menos uma vida ativa e ter coletado a chave da fase.

Os inimigos servem apenas como obstáculos e não são obrigatórios para progressão, sendo possível completar as fases sem derrotar nenhum deles.

A recuperação da memória ocorre apenas ao final do jogo.

--------------------------------------------

# Personagem Principal

O personagem principal é um fantasma chamado Saulo, preso em uma masmorra sem memória de seu passado.

Ele possui movimentação de plataforma, podendo andar para esquerda e direita e pular.


## Atributos do personagem

- Vidas: 3 por fase
- Velocidade: normal
- Ataque: uso de plasmas

Para atacar, o jogador deve coletar 5 plasmas, que são consumidos a cada uso do ataque.

O personagem não possui habilidades especiais além dessas mecânicas básicas.

--------------------------------------------

# Inimigos e Obstáculos

O jogo possui guardas fantasmas, com designs diferentes em cada nível da masmorra.

Os inimigos possuem movimentação limitada em áreas específicas. Em níveis mais avançados, alguns podem perseguir o jogador, como no nível Bestial.

Ao encostar em inimigos, o jogador perde uma vida. Caso esteja com apenas uma vida restante, ao sofrer dano, a fase é reiniciada.


## Obstáculos

- Buracos e fossos, que eliminam o jogador instantaneamente, reiniciando a fase
- No nível Escaldante existem bolas de fogo saindo de áreas de lava
- Obstáculos perigosos compostos por lâminas no nível Carmesim

--------------------------------------------

# Cenário (Mapa)

As fases possuem estrutura linear, onde o jogador progride da esquerda para a direita até alcançar o final do nível.



## Elementos do mapa

- Chave: visível, porém localizada em áreas com maior concentração de inimigos
- Portão de saída: localizado ao final da fase
- Plasmas: espalhados pelo mapa



## Níveis da masmorra

### Eterno
Nível inicial, mais simples e introdutório.

### Congelante
Possui áreas que reduzem a velocidade do jogador.

### Escaldante
Contém lava e bolas de fogo como obstáculos principais.

### Desértico
Exige coleta de água para manter a velocidade do personagem.

### Bestial
Os inimigos passam a perseguir o jogador.

### Carmesim
Focado em precisão e controle, com áreas compostas por lâminas e superfícies perigosas.

--------------------------------------------

# Sistema de Pontuação

O jogador acumula pontos ao longo do jogo.

| Ação | Pontuação |
|----------------------|
| Derrotar inimigos | 20 pontos |
| Coletar plasma | 5 pontos |
| Completar fase | 50 pontos |

O sistema incentiva tanto exploração quanto combate.

--------------------------------------------

# Sistema de Vida

O jogador inicia cada fase com 3 vidas, sendo esse valor reiniciado a cada novo nível.

Ao encostar em inimigos, o jogador perde uma vida. O dano é fixo.

Buracos eliminam o jogador instantaneamente, reiniciando a fase.

Durante o jogo, é possível coletar até duas vidas adicionais por fase, porém o limite máximo de vidas permanece em três.

Ao perder todas as vidas, a fase é reiniciada.

--------------------------------------------

# Controles

## Movimentação

| Tecla | Função |
|----------------------|
| A / D | Movimentação lateral |
| ← / → | Movimentação lateral |

## Pulo

| Tecla | Função |
|----------------------|
| Espaço | Pular |
| W | Pular |
| ↑ | Pular |

## Ações

| Tecla | Função |
|----------------------|
| S | Ataque com plasma |
| R | Reiniciar fase |
| ESC | Sair do jogo |

-----------------------------------------------

# Fluxo do Jogo

1. O jogo inicia em um menu principal;
2. O jogador pode iniciar a partida, acessar opções ou sair;
3. Ao iniciar o jogo, o personagem é direcionado ao nível Eterno;
4. Durante a partida, o jogador explora o mapa, coleta itens e enfrenta obstáculos;
5. Ao concluir uma fase, é exibida uma tela de fase concluída;
6. O jogador pode avançar para a próxima fase ou retornar ao menu;
7. Caso todas as vidas acabem, a fase atual é reiniciada;
8. Ao concluir todos os níveis, uma sequência narrativa mostra as memórias recuperadas de Saulo.

--------------------------------------------

# Regras do Jogo

- A chave é obrigatória para liberar o portão de saída;
- O jogador pode derrotar inimigos, mas isso não é obrigatório para progressão;
- O ataque consome exatamente 5 plasmas por uso;
- Buracos reiniciam a fase imediatamente ao contato;
- Não é permitido atravessar paredes, obstáculos ou limites do mapa.

--------------------------------------------

# Estrutura do Projeto

```bash
/ghostbreak
│
├── main_jogo.py
├── player.py
├── inimigos.py
├── obstaculos.py
├── mapa.py
├── sistema_coleta.py
└── README.md
```

## Responsabilidade dos arquivos

- `main_jogo.py` → controle principal do jogo
- `player.py` → lógica do personagem principal
- `inimigos.py` → comportamento dos inimigos
- `obstaculos.py` → elementos perigosos do mapa
- `mapa.py` → construção dos níveis
- `sistema_coleta.py` → sistema de coleta de itens

--------------------------------------------

# Funcionalidades Mínimas

- Sistema de movimentação do jogador
- Sistema de coleta de plasmas
- Sistema de colisão com inimigos e perda de vida
- Sistema de progressão entre fases
- Sistema de chave e portão
- Sistema de pontuação

--------------------------------------------

# Melhorias Futuras

- Adição de novos tipos de inimigos com comportamentos diferentes
- Criação de animações mais detalhadas para personagens e inimigos
- Sistema de checkpoints dentro das fases
- Inclusão de novos poderes ou habilidades especiais para o personagem
- Sistema de ranking de pontuação entre jogadores
- Melhorias visuais nos níveis, com mais detalhes e ambientação

--------------------------------------------
