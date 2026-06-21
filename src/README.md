# Codigo-fonte (`src`)

Esta pasta contem os modulos principais do jogo.

## Arquivos

- `jogo.py`: loop principal, eventos, atualizacao, renderizacao, telas e regras da partida.
- `config.py`: constantes globais, como tamanho da tela, cores, caminhos e FPS.
- `funcoes.py`: funcoes auxiliares de regra e logica, mantidas pequenas para testes.
- `sprites.py`: suporte do template para carregamento e recorte de spritesheet.
- `dados.py`: leitura e gravacao de dados, como o recorde.

## Organizacao

O jogo visual fica em `src/jogo.py`, enquanto regras puras ficam em `src/funcoes.py`. Essa separacao facilita explicar o codigo e executar testes sem abrir a janela do Pygame.
