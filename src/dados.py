def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(str(pontuacao))
    except IOError as e:
        print(f"Erro ao salvar recorde: {e}")


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


def salvar_ranking(caminho_arquivo, ranking):
    """Salva o ranking em arquivo texto (formato JSON)."""
    import json
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(ranking, arquivo, indent=2)
    except IOError as e:
        print(f"Erro ao salvar ranking: {e}")


def carregar_ranking(caminho_arquivo):
    """Carrega o ranking salvo; retorna lista vazia se não existir."""
    import json
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            
            if conteudo == "":
                return []
            
            return json.loads(conteudo)
    
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except IOError as e:
        print(f"Erro ao carregar ranking: {e}")
        return []