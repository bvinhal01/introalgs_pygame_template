# Nome do Jogo

Snake Adventure

## Integrantes do grupo

- Gabriel Rodrigues Lima
- Patrick da Lomba
- Igor 
- Bernardo Vinhal de Carvalho Teixeira


## Estrutura do Projeto

- `main.py`: arquivo principal que inicia o jogo.
- `src/`: código-fonte do jogo (movimentação da cobra, regras, pontuação e colisões).
- `assets/`: imagens, ícones e sons utilizados no jogo.
- `data/`: armazenamento do recorde do jogador.
- `tests/`: testes das principais funcionalidades do jogo.
- `docs/`: documentação do projeto, incluindo a proposta inicial e relatórios.

## Descrição do jogo



O jogador controla uma cobra que se movimenta por um cenário coletando alimentos. Cada alimento coletado aumenta o tamanho da cobra e a pontuação do jogador. O desafio é evitar colisões enquanto busca alcançar a maior pontuação possível.

## Objetivo do jogador

Coletar o maior número possível de alimentos sem colidir com as bordas do mapa ou com o próprio corpo da cobra.



## Regras do jogo

Liste as principais regras do jogo.

Exemplo:

- A cobra se movimenta continuamente.
- O jogador pode alterar a direção da cobra utilizando o teclado.
- Cada alimento coletado aumenta o tamanho da cobra.
- O jogador ganha pontos ao coletar alimentos.
- O jogo termina caso ocorra uma colisão.acaba.

## Controles

- Tecla W ou seta para cima: mover para cima.
- Tecla S ou seta para baixo: mover para baixo.
- Tecla A ou seta para esquerda: mover para esquerda.
- Tecla D ou seta para direita: mover para direita.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
