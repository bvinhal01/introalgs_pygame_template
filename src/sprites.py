import pygame


def pegar_sprite(local_arquivo, x, y, width, height, scale=1):
    """Corta um elemento de uma spritesheet BMP e remove a cor de fundo."""
    sheet = pygame.image.load(local_arquivo).convert()
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), (x, y, width, height))

    # Em BMP sem transparencia, usamos a cor do primeiro pixel como colorkey.
    cor_do_fundo = image.get_at((0, 0))
    image.set_colorkey(cor_do_fundo)

    if scale != 1:
        novo_largura = int(width * scale)
        novo_altura = int(height * scale)
        image = pygame.transform.scale(image, (novo_largura, novo_altura))

    return image
