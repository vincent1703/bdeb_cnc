from PIL import Image

espacement = 1
largeur_surface = 20
hauteur_surface = 30
image_path = "/home/vincent/bdeb_cnc/images/angela.png"

hauteur_originale = 1
largeur_originale = 1

hauteur_nouvelle = 1
largeur_nouvelle = 1

facteur = 1
facteur_max = 1

def image_loading ():
    global image_booleen
    image_booleen = [[False for i in range(largeur_nouvelle)] for j in range(hauteur_nouvelle)]

def info_image ():
    image = Image.open(image_path)
    hauteur_originale = image.height
    largeur_originale = image.width

def calcul_facteur_max():
    limite_hauteur = test_facteur(hauteur_originale, hauteur_surface, espacement)
    limite_largeur = test_facteur(largeur_originale, largeur_surface, espacement)
    if limite_hauteur >= limite_largeur:
        facteur_max = limite_largeur
        return facteur_max
    else:
        facteur_max = limite_hauteur
        return facteur_max

def test_facteur(original,surface,espacement):
    capacite = surface / espacement
    mult = capacite / original
    return mult


def set_path(image_path_import):
    image_path = image_path_import
def set_espacement(spacing):
    espacement = spacing
def set_max_heigth(max_height):
    hauteur_surface = max_height
def set_max_width(max_width):
    largeur_surface = max_width
def set_img_new_height(new_height):
    heuteur_nouvelle = new_height
def set_img_new_width(new_width):
    largeur_nouvelle = new_width

def get_facteur():
    return facteur
def get_facteur_max():
    return facteur_max
def get_img_new_height():
    return hauteur_nouvelle
def get_img_new_width():
    return largeur_nouvelle
def get_espacement():
    return espacement
