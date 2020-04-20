from PIL import Image
import cnc_v1
import os
import enums
import math

largeur_surface = 400
hauteur_surface = 400

HAUTEUR_MAX = 500
LARGEUR_MAX = 500

PREVIEW_PATH = os.path.dirname(os.path.abspath(__file__)) + "/images/preview.png"

nb_step_x = 0                           # Compteur du nb de steps fait de droite a gauche
nb_step_y = 0                           # Compteur du nb de steps fait de haut en bas
DELAIS_STEP = 0.002                     # Delais en secondes entre chaque changement de step 
DELAIS_SOLENOIDE = 0.5                  # Delais en secondes pour lequel le solenoide est active
#DELAIS_GRIS = ?


parametres = {}
parametres[enums.Param.PATH] = os.path.dirname(os.path.abspath(__file__)) + "/images/mendel.png"
parametres[enums.Param.LARGEUR] = 100
parametres[enums.Param.HAUTEUR] = 100
parametres[enums.Param.ESPACEMENT] = 1
parametres[enums.Param.MODE] = enums.Mode.CONTRASTE
parametres[enums.Param.THRESHOLD] = 60
parametres[enums.Param.DIFFERENCE] = 20
parametres[enums.Param.COMPARE] = 20
parametres[enums.Param.ESTIMATION] = "aucune estimation"


def generate_image_preview():
    image_loading_array()
    cnc_v1.generate_preview(image_booleen)
    #preview_image.save(PREVIEW_PATH)

def generate_estimation():
    estimation = cnc_v1.time_estimation()
    heures = math.floor(estimation / 3600)
    minutes = math.floor((estimation % 3600) / 60)
    secondes = math.floor(estimation % 60)
    temps = str(heures) + "h " + str(minutes) + "m " + str(secondes) + "s"
    parametres[enums.Param.ESTIMATION] = temps
    return temps

def image_loading_array ():
    global image_booleen
    image_booleen = [[0 for i in range(parametres[enums.Param.LARGEUR])] for j in range(parametres[enums.Param.HAUTEUR])]
    if parametres[enums.Param.MODE] == enums.Mode.CONTRASTE:
        image_booleen = cnc_v1.mapping_image()
    elif parametres[enums.Param.MODE] == enums.Mode.LUMINOSITE:
        image_booleen = cnc_v1.contour_image()
    elif parametres[enums.Param.MODE] == enums.Mode.COULEUR:
        image_booleen = cnc_v1.color_change()
    else:
        print('option non accessible')

def update_premiere_page():
    image = Image.open(parametres[enums.Param.PATH])
    limite_hauteur = test_facteur(image.height, hauteur_surface, parametres[enums.Param.ESPACEMENT])
    limite_largeur = test_facteur(image.width, largeur_surface, parametres[enums.Param.ESPACEMENT])
    if limite_hauteur >= limite_largeur:
        facteur_max = limite_largeur
    else:
        facteur_max = limite_hauteur
    global image_final
    image_final = cnc_v1.resizing(image, facteur_max)
    parametres[enums.Param.LARGEUR] = image_final.width
    parametres[enums.Param.HAUTEUR] = image_final.height

def test_facteur(original,surface,espacement):
    capacite = surface / espacement
    mult = capacite / original
    return mult

