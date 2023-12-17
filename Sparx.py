import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de l'image de Sparx
width, height = 32, 32

# Création de l'image de Sparx
sparx = pygame.Surface((width, height), pygame.SRCALPHA)
pygame.draw.circle(sparx, (255, 255, 0), (width // 2, height // 2), 12)  # Corps jaune
pygame.draw.circle(sparx, (0, 0, 0), (width // 2 - 5, height // 2 - 5), 3)  # Œil noir

# Sauvegarde de l'image de Sparx
pygame.image.save(sparx, "sparx.png")