# 🐍 Jogo da Cobrinha - Pygame

Um jogo da cobrinha clássico desenvolvido com Pygame em Python. O objetivo é guiar a cobra para comer comidas enquanto evita obstáculos, outras partes do corpo e as bordas da tela.

## 📋 Requisitos

- Python 3.8+
- Pygame
- pytest (para rodar os testes)

## 🚀 Instalação

1. **Clone ou baixe o projeto**:
```bash
cd introalgs_pygame_template
```

2. **Crie um ambiente virtual** (recomendado):
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

## 🎮 Como Jogar

Execute o jogo com:
```bash
python main.py
```

### Controles

- **Setas do Teclado** (↑ ↓ ← →): Mover a cobra nas 4 direções
- **R**: Recomeçar o jogo na tela de game over
- **Q**: Sair do jogo na tela de game over

### Objetivo

1. **Comida (Amarelo)**: Mova a cobra para comer. Cada comida comida = +10 pontos
2. **Evite Obstáculos (Vermelho)**: Colidir com obstáculos causa perda de 1 vida
3. **Evite Colisão com Você Mesmo**: A cobra cresce ao comer, colidir consigo mesmo causa perda de 1 vida
4. **Evite as Bordas**: Sair da tela causa perda de 1 vida
5. **Vença antes do Tempo Acabar**: Você tem 120 segundos para sobreviver e acumular pontos

### Status do Jogo

O HUD (interface) mostra:
- **Pontos**: Seus pontos atuais
- **Vidas**: Vidas restantes (começa com 3)
- **Tempo**: Tempo restante em MM:SS
- **Recorde**: Sua melhor pontuação de todos os tempos

## 📊 Mecanismo de Jogo

### Pontuação
- +10 pontos por cada comida comida
- O recorde é salvo automaticamente em `data/recorde.txt`
- Ranking dos melhores 10 jogos é salvo em `data/ranking.txt`

### Vidas
- Começa com 3 vidas
- Perde 1 vida ao colidir com:
  - Obstáculos (aparecem a cada 5 segundos, máximo 5 obstáculos)
  - Você mesmo (cobra)
  - As bordas da tela
- Game Over quando vidas chegam a 0

### Tempo
- Total de 120 segundos (2 minutos)
- Descontagem em tempo real
- Você vence se sobreviver os 120 segundos

### Obstáculos
- Aparecem aleatoriamente a cada 5 segundos
- Máximo de 5 obstáculos na tela simultaneamente
- Causam perda de 1 vida ao colidir

## 📁 Estrutura do Projeto

```
introalgs_pygame_template/
├── main.py                 # Ponto de entrada
├── requirements.txt        # Dependências
├── README.md              # Este arquivo
├── src/
│   ├── __init__.py
│   ├── config.py          # Configurações centrais
│   ├── jogo.py            # Loop principal do jogo
│   ├── funcoes.py         # Funções auxiliares
│   ├── dados.py           # Leitura/escrita de dados
│   ├── sprites.py         # Manipulação de sprites
│   └── README.md
├── tests/
│   ├── test_logica.py     # Testes unitários
│   └── README.md
├── assets/                # Recursos (imagens, sons)
│   ├── imagens/
│   ├── sons/
│   └── fontes/
├── data/                  # Dados persistentes
│   ├── recorde.txt        # Melhor pontuação
│   ├── ranking.txt        # Ranking de partidas
│   └── README.md
└── docs/                  # Documentação
    ├── proposta.MD
    └── README.md
```

## 🧪 Testes

Rode os testes unitários com:

```bash
pytest tests/test_logica.py -v
```

Os testes cobrem:
- Cálculo de pontos
- Sistema de vidas
- Validação de limites
- Formatação de tempo
- Criação da cobra e comida
- Movimento da cobra
- Detecção de colisões (cobra, paredes, comida, obstáculos)

### Executar um teste específico:
```bash
pytest tests/test_logica.py::test_calcular_pontos -v
```

### Ver cobertura de testes:
```bash
pytest tests/test_logica.py --cov=src --cov-report=html
```

## 🔧 Configurações

Todas as configurações centrais estão em `src/config.py`:

```python
LARGURA_TELA = 800          # Largura em pixels
ALTURA_TELA = 600           # Altura em pixels
FPS = 60                    # Frames por segundo
TAMANHO_QUADRADO = 20       # Tamanho de cada célula
TITULO_JOGO = "..."         # Título da janela

TEMPO_JOGO = 120            # Tempo em segundos
VIDAS_INICIAIS = 3          # Vidas iniciais
CAMINHO_RECORDE = "..."     # Caminho do arquivo de recorde
```

Você pode editar essas configurações para customizar o jogo (tamanho da tela, velocidade, etc).

## 📊 Persistência de Dados

### Recorde (`data/recorde.txt`)
Arquivo de texto simples armazenando a melhor pontuação de todos os tempos.

### Ranking (`data/ranking.txt`)
Arquivo JSON armazenando os 10 melhores jogos com:
- Pontuação
- Tempo jogado

Exemplo:
```json
[
  {
    "pontos": 150,
    "tempo": 95
  },
  {
    "pontos": 120,
    "tempo": 110
  }
]
```

## 🎯 Funcionalidades Implementadas - Semana 3

✅ **Interações Principais**
- Controle via setas do teclado
- Sistema de entrada responsivo
- Tela de game over com opções (Recomeçar/Sair)

✅ **Sistema de Pontuação, Vidas, Tempo**
- Pontuação por comida comida (+10 pontos)
- Sistema de 3 vidas com penalidades por colisão
- Contagem regressiva de tempo (120 segundos)
- HUD mostrando status em tempo real

✅ **Condição de Vitória/Derrota/Encerramento**
- **Derrota**: Game Over ao perder todas as 3 vidas
- **Vitória**: Sobreviver os 120 segundos
- **Encerramento**: Tela de fim de jogo com opções

✅ **Estruturas de Dados**
- Lista para segmentos da cobra
- Listas para obstáculos
- Dicionários para ranking

✅ **Leitura/Escrita em Arquivo**
- Salvar recorde em `data/recorde.txt`
- Salvar ranking de partidas em `data/ranking.txt` (JSON)
- Carregar dados ao iniciar

✅ **Testes Unitários**
- 40+ testes cobrindo todas as funcionalidades principais
- Testes de pontuação, vidas, movimento, colisões

✅ **README Atualizado**
- Documentação completa
- Instruções de instalação e execução
- Descrição de mecanismos
- Guia de testes

## 🐛 Resolução de Problemas

### O jogo não inicia
- Verifique se o Pygame está instalado: `pip install pygame`
- Verifique se está usando Python 3.8+: `python --version`

### ModuleNotFoundError: No module named 'pygame'
```bash
pip install -r requirements.txt
```

### Teste falha com "ModuleNotFoundError"
```bash
# Verifique que está no diretório correto
cd /caminho/do/projeto

# Execute os testes do diretório raiz
pytest tests/test_logica.py -v
```

### Cobra muito rápida ou lenta
Edite `src/config.py` e ajuste `FPS`:
```python
FPS = 60  # Aumente para mais rápido, diminua para mais lento
```

Ou ajuste a velocidade no `jogo.py` (contador_frames >= 10).

## 📝 Estrutura do Código

### `main.py`
- Ponto de entrada da aplicação
- Chama `executar_jogo()`

### `src/config.py`
- Constantes e configurações centralizadas

### `src/jogo.py`
- **`executar_jogo()`**: Loop principal do jogo
- **`criar_cobra_inicial()`**: Inicializa cobra com 3 segmentos
- **`criar_comida()`**: Gera comida aleatória
- **`criar_obstaculo()`**: Gera obstáculos aleatórios
- **`atualizar_cobra()`**: Movimenta a cobra
- **`desenhar_jogo()`**: Renderiza frame
- **`desenhar_hud()`**: Mostra informações
- **Funções de colisão**: Detectam colisões

### `src/funcoes.py`
- Funções auxiliares reutilizáveis

### `src/dados.py`
- Gerenciamento de recorde
- Gerenciamento de ranking

### `tests/test_logica.py`
- Testes unitários com pytest

## 🎨 Cores

- **Verde**: Cobra
- **Amarelo**: Comida
- **Vermelho**: Obstáculos
- **Branco**: Fundo do HUD
- **Preto**: Fundo do jogo

## 📈 Possíveis Melhorias Futuras

- [ ] Sons e música
- [ ] Levels/fases
- [ ] Power-ups
- [ ] Efeitos visuais (animações)
- [ ] Menu principal
- [ ] Pausa
- [ ] Dificuldade ajustável
- [ ] Multiplayer
- [ ] Highscore com nome do jogador

## 📄 Licença

Este projeto é fornecido como está para fins educacionais.

## 👥 Autores

Projeto de Introdução a Algoritmos - Semana 3
Data de Entrega: 14/06/2026

---

**Divirta-se jogando! 🎮🐍** - Pygame

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Bernardo Vinhal De Carvalho Teixeira

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

> O jogo consiste em controlar uma cobra que deve coletar os itens no mapa e evitar obstáculos. O jogador ganha pontos ao coletar itens e perde vidas ao colidir com obstáculos. A partida termina quando o tempo acaba ou quando o jogador perde todas as vidas.

## Objetivo do jogador

> O objetivo é coletar a maior quantidade possível de itens antes que o tempo acabe, evitando colisões com os obstáculos.

## Requisitos

- Python 3.11+
- Pygame
- Pytest

## Regras do jogo

- O jogador se movimenta usando as setas do teclado.
- Cada item coletado aumenta a pontuação.
- Colidir com um obstáculo reduz a quantidade de vidas. ( max-3)

A partida termina quando:
- o jogador perde todas as vidas;
- o tempo acaba;
- a pontuação máxima é alcançada.

## Funcionalidades

- Sistema de pontuação
- Sistema de vidas
- Temporizador
- Obstáculos
- Crescimento da cobra
- Salvamento de recorde em arquivo

## Controles

- ↑ Mover para cima
- ↓ Mover para baixo
- ← Mover para esquerda
- → Mover para direita

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

