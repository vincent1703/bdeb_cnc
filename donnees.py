from PIL import Image
import cnc_v1
import os
import math

espacement = 1
largeur_surface = 400
hauteur_surface = 400
image_path = os.path.dirname(os.path.abspath(__file__)) + "/images/mendel.png"

hauteur_originale = 1
largeur_originale = 1

hauteur_nouvelle = 100
largeur_nouvelle = 100

hauteur_machine_max = 500
largeur_machine_max = 500

mode = 0
estimation = 0.0
preview_path = os.path.dirname(os.path.abspath(__file__)) + "/images/preview.png"

compare = 6
threshold = 60
difference = 34

nb_step_x = 0                           # Compteur du nb de steps fait de droite a gauche
nb_step_y = 0                           # Compteur du nb de steps fait de haut en bas
DELAIS_STEP = 0.002                     # Delais en secondes entre chaque changement de step 
DELAIS_SOLENOIDE = 0.5                  # Delais en secondes pour lequel le solenoide est active


def generate_image_preview():
    image_loading_array()
    cnc_v1.generate_preview(image_booleen)
    #preview_image.save(preview_path)

def generate_estimation():
    estimation = cnc_v1.time_estimation()
    heures = math.floor(estimation / 3600)
    minutes = math.floor((estimation % 3600) / 60)
    secondes = math.floor(estimation % 60)
    temps = str(heures) + "h " + str(minutes) + "m " + str(secondes) + "s"
    return temps

def image_loading_array ():
    global image_booleen
    image_booleen = [[False for i in range(largeur_nouvelle)] for j in range(hauteur_nouvelle)]
    if mode == 0:
        image_booleen = cnc_v1.mapping_image()
    elif mode == 1:
        image_booleen = cnc_v1.contour_image()
    elif mode == 2:
        image_booleen = cnc_v1.color_change()
    else:
        print('option non accessible')

def update_premiere_page():
    info_image()
    #print('info_image')
    calcul_facteur_max()
    #print('facteur_max')
    image_final_size()
    #print('final_size')


def info_image ():
    global image
    image = Image.open(image_path)
    global hauteur_originale
    hauteur_originale = image.height
    global largeur_originale
    largeur_originale = image.width

def calcul_facteur_max():
    global limite_hauteur
    limite_hauteur = test_facteur(hauteur_originale, hauteur_surface, espacement)
    global limite_largeur
    limite_largeur = test_facteur(largeur_originale, largeur_surface, espacement)
    
    global facteur_max
    if limite_hauteur >= limite_largeur:
        facteur_max = limite_largeur
    else:
        facteur_max = limite_hauteur

def test_facteur(original,surface,espacement):
    capacite = surface / espacement
    mult = capacite / original
    return mult

def image_final_size():
    global image_final
    image_final = cnc_v1.resizing(image,facteur_max)
    largeur_nouvelle = image_final.width
    hauteur_nouvelle = image_final.height


################
### inutiles ###
################
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

def get_facteur_max():
    return facteur_max
def get_img_new_height():
    return hauteur_nouvelle
def get_img_new_width():
    return largeur_nouvelle
def get_espacement():
    return espacement
