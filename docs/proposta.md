# Proposta Inicial do Jogo

## 1. Nome provisiorio do jogo

Snake Adventure: Arena Neon.

## 2. Integrantes do grupo

- Gabriel Rodrigues Lima
- Patrick da Lomba
- Igor
- Bernardo Vinhal de Carvalho Teixeira

## 3. Tipo de jogo

Snake com coleta de itens, crescimento do personagem, desvio de obstaculos e sobrevivencia em arena.

## 4. Descricao geral do jogo

O jogador controla uma cobra em uma arena fechada. Na tela aparecem orbes de energia, obstaculos e o corpo da propria cobra. O jogador precisa coletar os orbes para ganhar pontos e crescer, evitando bater nas bordas, nos obstaculos e no proprio corpo.

## 5. Objetivo do jogador

Alcancar a maior pontuacao possivel coletando orbes e sobrevivendo por mais tempo.

## 6. Regras principais

- A cobra anda continuamente.
- O jogador muda a direcao com WASD ou setas.
- Cada orbe coletado aumenta pontos e tamanho da cobra.
- A velocidade aumenta aos poucos conforme a pontuacao cresce.
- A partida termina ao bater na parede, em obstaculos ou no proprio corpo.

## 7. Condicao de vitoria

O jogo nao possui uma vitoria fixa. O objetivo e superar o proprio recorde, criando uma meta de pontuacao cada vez maior.

## 8. Condicao de derrota ou encerramento

A partida termina quando a cobra colide com a borda da arena, com um obstaculo ou com o proprio corpo. O jogador tambem pode encerrar usando `ESC`.

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

Uma cobra desenhada por segmentos circulares, com cabeca, corpo e olhos. O corpo cresce conforme a pontuacao aumenta.

### Obstaculos, inimigos ou desafios

Pedras ficam espalhadas pela arena. Elas servem como obstaculos fixos e encerram a partida se a cabeca da cobra encostar.

### Itens, alvos ou objetos de interacao

Orbes coloridos aparecem em posicoes aleatorias. Eles aumentam a pontuacao e o tamanho da cobra quando coletados.

### Pontuacao, vidas, tempo ou progresso

O jogo usa pontuacao e recorde salvo em arquivo. Nao ha vidas: uma colisao importante encerra a rodada.

## 10. Controles previstos

- `W` ou seta para cima: mover para cima.
- `S` ou seta para baixo: mover para baixo.
- `A` ou seta para esquerda: mover para esquerda.
- `D` ou seta para direita: mover para direita.
- `P`: pausar.
- `ENTER`: iniciar ou reiniciar.
- `ESC`: sair.

## 11. Organizacao inicial do codigo

- `main.py`: inicia o jogo.
- `src/jogo.py`: contem telas, loop principal, eventos, atualizacao e desenho.
- `src/config.py`: guarda tamanho da tela, FPS, cores e caminhos.
- `src/funcoes.py`: contem funcoes de logica e regras testaveis.
- `src/dados.py`: contem leitura e escrita do recorde.
- `tests/test_logica.py`: valida regras importantes com pytest.

## 12. Recursos externos previstos

Nao pretendemos utilizar recursos externos na partida final. Os elementos visuais principais sao desenhados com formas do Pygame. O arquivo `assets/imagens/spritesheet.bmp` foi mantido por ser parte do template da disciplina.

## 13. Principais dificuldades esperadas

- Criar movimento fluido sem grade fixa.
- Implementar colisao circular justa.
- Separar codigo visual de funcoes testaveis.
- Salvar recorde em arquivo.
- Gerar itens em posicoes validas.

## 14. Escopo minimo para a entrega final

A versao minima deve ter uma cobra controlavel, comida coletavel, pontuacao, crescimento, colisao com bordas, tela inicial, tela de fim de jogo e testes das funcoes principais.

## 15. Possiveis melhorias, caso haja tempo

- Obstaculos na arena.
- Recorde salvo em arquivo.
- Visual neon com grade e brilho.
- Pausa durante a partida.
- Aumento gradual de velocidade.
