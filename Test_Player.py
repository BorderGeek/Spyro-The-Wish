import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de l'image du joueur
width, height = 64, 64

# Création de l'image du joueur (Spyro)
player = pygame.Surface((width, height), pygame.SRCALPHA)
pygame.draw.circle(player, (148, 0, 211), (width // 2, height // 2), 30)  # Corps violet
pygame.draw.circle(player, (255, 255, 0), (width // 2 - 10, height // 2 - 10), 6)  # Œil jaune
pygame.draw.polygon(player, (255, 165, 0), [(width // 2 - 10, height // 2 + 10),
                                             (width // 2 + 10, height // 2 + 10),
                                             (width // 2, height // 2 + 25)])  # Flamme orange sur le dos

# Ajout d'ailes
pygame.draw.polygon(player, (0, 0, 255), [(width // 2 - 10, height // 2 - 5),
                                           (width // 2 - 15, height // 2 - 20),
                                           (width // 2 - 5, height // 2 - 15)])

pygame.draw.polygon(player, (0, 0, 255), [(width // 2 + 10, height // 2 - 5),
                                           (width // 2 + 15, height // 2 - 20),
                                           (width // 2 + 5, height // 2 - 15)])

# Sauvegarde de l'image du joueur
pygame.image.save(player, "player.png")