import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de l'image étirée
largeur, hauteur = 1000, 800

# Création de l'image
background = pygame.Surface((largeur, hauteur))

# Ciel
background.fill((135, 206, 250))  # Couleur bleu ciel

# Montagnes avec pentes
pygame.draw.polygon(background, (169, 169, 169), [(0, hauteur), (largeur / 4, hauteur / 1.5), (largeur / 2, hauteur)])
pygame.draw.polygon(background, (169, 169, 169), [(largeur / 2, hauteur), (3 * largeur / 4, hauteur / 1.5), (largeur, hauteur)])

# Herbe ou sol
pygame.draw.rect(background, (50, 205, 50), (0, hauteur / 2, largeur, hauteur / 2))

# Ajout d'un château à l'entrée (à gauche)
pygame.draw.rect(background, (128, 0, 0), (50, hauteur / 2 - 100, 100, 100))  # Château rectangulaire

# Ajout d'un petit chemin au milieu
pygame.draw.rect(background, (210, 180, 140), (largeur / 3, hauteur / 2, largeur / 3, hauteur / 4))

# Sauvegarde de l'image
pygame.image.save(background, "Monde_Des_Artisans.png")