import pygame

pygame.init()
font = pygame.font.Font(None, 40)


def debug(info, y=10, x=10):
    displaySurface = pygame.display.get_surface()
    debugSurface = font.render(str(info), True, "gold")
    debugRect = debugSurface.get_rect(topleft=(x, y))
    pygame.draw.rect(displaySurface, "gray27", debugRect)
    displaySurface.blit(debugSurface, debugRect)
