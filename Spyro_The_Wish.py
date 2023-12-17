import pygame
import sys
import pygame_menu
import math

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 800, 600
écran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Spyro The Wish")

# Chargement de l'image du Monde des Artisans
background = pygame.image.load("Monde_Des_Artisans.png")

# Chargement des images de Spyro et Sparx
spyro = pygame.image.load("Spyro.png")
sparx = pygame.image.load("Sparx.png")

# Position initiale de Spyro et Sparx
rect_spyro = spyro.get_rect()
rect_spyro.topleft = (66, hauteur / 2 + 37)  # Légèrement vers le bas

rect_sparx = sparx.get_rect()

# Paramètres de l'orbite de Sparx autour de Spyro
rayon_orbite = 50
vitesse_orbite = 0.20  # Ajustez la vitesse selon vos préférences
angle_orbite = 0  # Initialise l'angle d'orbite

# Paramètres du rebond
en_rebond = False
hauteur_rebond_initial = 0
hauteur_rebond_max = 50  # Hauteur maximale du rebond (ajustez selon vos préférences)
gravite = 2  # Force de gravité pour le rebond

# Paramètres de la vitesse de déplacement
vitesse_deplacement = 5

# État du jeu
SELECT_LANGUE = 0
JEU_EN_COURS = 1
etat_jeu = SELECT_LANGUE

# Fonction pour démarrer le jeu
def start_game():
    global en_rebond, etat_jeu
    en_rebond = False
    menu_principal.disable()
    etat_jeu = JEU_EN_COURS

# Fonction pour revenir au menu principal depuis le menu de sélection de langue
def retour_au_menu_principal():
    menu_langue.disable()
    menu_principal.enable()

# Paramètres du menu principal
menu_principal = pygame_menu.Menu('Spyro The Wish', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

# Fonction pour démarrer le jeu
def start_game():
    global en_rebond, etat_jeu
    en_rebond = False
    menu_principal.disable()
    etat_jeu = JEU_EN_COURS

# Paramètres du menu de sélection de langue
menu_langue = pygame_menu.Menu('Langue', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

# Fonction de changement de langue
def set_language(selected_language, selected_index):
    global language, game_running
    if isinstance(selected_language, str):  # Vérifie si la langue est une chaîne de caractères
        language = selected_language
        if language == 'fr':
            menu_principal.set_title("Français")
        elif language == 'en':
            menu_principal.set_title("English")
        retour_au_menu_principal()  # Revenir au menu principal après la sélection de la langue

# Ajout du bouton "Langue" dans le menu principal
menu_principal.add.button('Démarrer', start_game)

# Ajout des options "Anglais" et "Français" dans le menu de sélection de langue
menu_langue.add.selector('', [('Anglais', 'en'), ('Français', 'fr')], onchange=set_language)

# Ajout d'un bouton pour revenir au menu principal dans le menu de sélection de langue
menu_langue.add.button('Retour', retour_au_menu_principal)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if etat_jeu == SELECT_LANGUE:
                    menu_principal.disable()
                    etat_jeu = JEU_EN_COURS

    # Mise à jour de l'angle de l'orbite
    angle_orbite += vitesse_orbite

    # Calcul des nouvelles coordonnées de Sparx par rapport à Spyro en utilisant la fonction trigonométrique
    rect_sparx.centerx = rect_spyro.centerx + int(rayon_orbite * math.cos(angle_orbite))
    rect_sparx.centery = rect_spyro.centery + int(rayon_orbite * math.sin(angle_orbite))

    if etat_jeu == SELECT_LANGUE:
        # Affichage du fond d'écran du menu principal
        écran.blit(background, (0, 0))
        # Affichage du menu principal
        menu_principal.mainloop(écran, disable_loop=True)
    elif etat_jeu == JEU_EN_COURS:
        # Logique du jeu ici...

        # Gestion du rebond en appuyant sur la touche Espace
        touches = pygame.key.get_pressed()
        if touches[pygame.K_SPACE] and not en_rebond:
            en_rebond = True
            hauteur_rebond_initial = rect_spyro.y  # Enregistrez la position initiale du rebond

        if en_rebond:
            rect_spyro.y = hauteur_rebond_initial - hauteur_rebond_max
            rect_sparx.y = hauteur_rebond_initial - hauteur_rebond_max

            hauteur_rebond_max -= gravite  # Ajustez la vitesse de descente du rebond

            if hauteur_rebond_max < 0:
                hauteur_rebond_max = 50
                en_rebond = False

        # Gestion du déplacement gauche/droite
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect_spyro.x -= vitesse_deplacement
        if keys[pygame.K_RIGHT]:
            rect_spyro.x += vitesse_deplacement

        # Assurez-vous que Spyro reste dans les limites de l'écran
        rect_spyro.x = max(0, min(rect_spyro.x, largeur - rect_spyro.width))

        # Affichage du fond d'écran du jeu
        écran.blit(background, (0, 0))
        écran.blit(spyro, rect_spyro.topleft)
        écran.blit(sparx, rect_sparx.topleft)

        # Actualisation de l'affichage du jeu
        pygame.display.flip()
        pygame.time.Clock().tick(60)