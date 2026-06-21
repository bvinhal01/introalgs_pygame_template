# Testes

Esta pasta contem testes automatizados do projeto.

## Arquivos

- `test_logica.py`: valida funcoes puras de regra em `src/funcoes.py`.

## O que e testado

- Soma de pontuacao.
- Condicao de derrota por vidas, herdada do template.
- Limitacao de valores.
- Distancia ao quadrado.
- Colisao circular.
- Limites da arena.
- Crescimento da cobra.
- Aumento gradual de velocidade.

## Como executar

```bash
python -m pytest
```

## Observacao

As regras principais ficam em funcoes pequenas para que possam ser testadas sem abrir uma janela do Pygame.
