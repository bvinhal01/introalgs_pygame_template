import os


def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuacao recorde em arquivo texto."""
    pasta = os.path.dirname(caminho_arquivo)
    if pasta:
        os.makedirs(pasta, exist_ok=True)

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se nao existir valor valido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except (FileNotFoundError, ValueError):
        return 0
