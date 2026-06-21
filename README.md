# Snake Adventure: Arena Neon

Projeto final de jogo em Python com Pygame, desenvolvido para a Semana 4 de finalizacao e apresentacao.

## Integrantes do grupo

- Gabriel Rodrigues Lima
- Patrick da Lomba
- Igor
- Bernardo Vinhal de Carvalho Teixeira

## Proposta do jogo

Snake Adventure: Arena Neon e um jogo inspirado na dinamica de crescimento de jogos como slither.io, mas implementado de forma autoral com Python e Pygame. O jogador controla uma cobra em uma arena neon, coleta orbes de energia, aumenta o corpo e tenta sobreviver pelo maior tempo possivel.

O objetivo principal e fazer a maior pontuacao sem bater nas bordas, nos obstaculos da arena ou no proprio corpo.

## Como o jogador interage

O jogador movimenta a cobra com teclado. A cobra anda continuamente e a direcao muda conforme as teclas pressionadas. A partida possui tela inicial, HUD com pontuacao, recorde, tamanho atual, pausa e tela de fim de jogo.

## Controles

- `W` ou seta para cima: mover para cima.
- `S` ou seta para baixo: mover para baixo.
- `A` ou seta para esquerda: mover para esquerda.
- `D` ou seta para direita: mover para direita.
- `P`: pausar ou continuar a partida.
- `ENTER`: iniciar ou reiniciar.
- `ESC`: sair da tela atual ou encerrar a partida.

## Regras principais

- A cobra se movimenta continuamente dentro da arena.
- Cada orbe coletado aumenta a pontuacao.
- Cada orbe tambem aumenta o comprimento alvo da cobra.
- A velocidade aumenta gradualmente conforme a pontuacao sobe.
- A partida termina se a cabeca da cobra sair da arena.
- A partida termina se a cabeca bater em um obstaculo.
- A partida termina se a cabeca bater no proprio corpo.
- O melhor resultado e salvo em `data/recorde.txt`.

## Conceitos da disciplina utilizados

- Variaveis, constantes e tipos de dados.
- Condicionais para regras de colisao, pausa e fim de jogo.
- Estruturas de repeticao no loop principal e na geracao de objetos.
- Listas para armazenar os segmentos da cobra e os itens da arena.
- Funcoes para separar responsabilidades e facilitar testes.
- Modulos Python para organizar configuracao, dados, regras e jogo.
- Leitura e escrita de arquivos para salvar recorde.
- Testes automatizados com `pytest`.
- Uso de biblioteca externa (`pygame`) para janela, eventos, desenho e tempo.

## Organizacao do codigo

- `main.py`: ponto de entrada do projeto; chama `executar_jogo()`.
- `src/jogo.py`: loop principal, telas, eventos, renderizacao, comida, obstaculos e regras da partida.
- `src/config.py`: constantes de tela, cores, FPS, titulo e caminhos.
- `src/funcoes.py`: funcoes puras de regra, pontuacao, limites, crescimento, velocidade e colisao.
- `src/dados.py`: leitura e gravacao do recorde.
- `src/sprites.py`: suporte do template para recorte de spritesheet.
- `tests/test_logica.py`: testes das funcoes de regra.
- `docs/proposta.md`: proposta inicial preenchida.
- `assets/`: pasta de recursos visuais, sons e fontes.
- `data/`: arquivos de persistencia simples.

## Como executar o projeto

Requisitos: Python 3.10 ou superior.

```bash
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Arquivos auxiliares necessarios

- `requirements.txt`: lista as dependencias (`pygame` e `pytest`).
- `data/recorde.txt`: guarda o melhor placar.
- `assets/imagens/spritesheet.bmp`: arquivo do template mantido no repositorio, embora o jogo final desenhe os elementos principais via Pygame.

## Recursos externos e autoria

O jogo final nao usa imagens, sons ou fontes externos durante a partida. A cobra, comidas, obstaculos, arena e HUD sao desenhados com formas geometricas do proprio Pygame.

O arquivo `assets/imagens/spritesheet.bmp` foi mantido como recurso fornecido pelo template da disciplina, mas nao e essencial para a versao final do jogo. Nenhum codigo foi copiado integralmente de tutoriais ou repositorios prontos; a implementacao foi adaptada para a proposta do grupo e organizada nos modulos do projeto.

## Uso do template da disciplina

O template foi usado como base de organizacao do repositorio:

- manteve a divisao em `src`, `tests`, `docs`, `assets` e `data`;
- manteve `main.py` como entrada da aplicacao;
- manteve funcoes puras em `src/funcoes.py` para facilitar testes;
- manteve persistencia simples de dados em `src/dados.py`;
- expandiu a proposta inicial em `docs/proposta.md`;
- substituiu a demo inicial por um jogo completo, com telas, regras, pontuacao, recorde e apresentacao visual.

## Principais desafios encontrados

- Organizar o codigo para separar regras testaveis do loop visual do Pygame.
- Criar uma movimentacao mais suave que a Snake classica em grade.
- Evitar colisao injusta com segmentos muito proximos da cabeca.
- Gerar comida em posicoes validas sem sobrepor cobra e obstaculos.
- Documentar autoria e recursos externos de forma clara.
- Garantir que o projeto executa por `python main.py` e que os testes passam.

## Roteiro breve para apresentacao

1. Explicar a proposta: uma Snake moderna em arena neon, inspirada em jogos .io.
2. Demonstrar controles: WASD/setas, pausa, reinicio e saida.
3. Mostrar regras: coletar orbes, crescer, evitar parede, obstaculos e corpo.
4. Apontar conceitos: listas, funcoes, modulos, eventos, colisao, arquivos e testes.
5. Mostrar organizacao: `main.py`, `src/jogo.py`, `src/funcoes.py`, `src/dados.py`, `tests`.
6. Rodar ou comentar os testes automatizados.
7. Explicar como o template foi aproveitado e evoluido.

## Status da entrega final

- Jogo completo e executavel: concluido.
- Codigo-fonte organizado: concluido.
- README preenchido: concluido.
- Proposta inicial em `docs/proposta.md`: concluido.
- Testes implementados: concluido.
- Arquivos auxiliares necessarios: concluido.
- Referencias para recursos externos: documentado.
- Apresentacao em sala: roteiro preparado neste README.
