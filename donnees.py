from PIL import Image
import cnc_v1
import os
import enums
import math


largeur_surface = 400                   #largeur choisie par l'utilisateur en mm
hauteur_surface = 400                   #hauteur choisie par l'utilisateur en mm

espacement=0.4                          #espacement entre chaque points en mm

HAUTEUR_MAX = 500                       #hauteur maximale d'impression en mm
LARGEUR_MAX = 500                       #largeur maximale d'impression en mm 

PREVIEW_PATH = os.path.dirname(os.path.abspath(__file__)) + "/images/dauphin.jpeg"  #chemin initial

nb_step_x = 0                           # Compteur du nb de steps fait de droite a gauche
nb_step_y = 0                           # Compteur du nb de steps fait de haut en bas
DELAIS_STEP = 0.002                     # Delais en secondes entre chaque changement de step 
DELAIS_SOLENOIDE = 0.5                  # Delais en secondes pour lequel le solenoide est active
#DELAIS_GRIS = ?


#dictionnaire contenant les informations de l'impression
parametres = {}
parametres[enums.Param.PATH] = os.path.dirname(os.path.abspath(__file__)) + "/images/burger.jpeg"
parametres[enums.Param.LARGEUR] = 100
parametres[enums.Param.HAUTEUR] = 100
parametres[enums.Param.ESPACEMENT] = 1
parametres[enums.Param.MODE] = enums.Mode.CONTRASTE
parametres[enums.Param.THRESHOLD] = 60
parametres[enums.Param.DIFFERENCE] = 20
parametres[enums.Param.COMPARE] = 20
parametres[enums.Param.ESTIMATION] = "aucune estimation"
parametres[enums.Param.PREVIEW] = os.path.dirname(os.path.abspath(__file__)) + "/images/preview.jpg"

#prend l'estiamtion en secondes dans cnc_v1 et le converti en heure et minutes
def generate_estimation():
    estimation = cnc_v1.time_estimation()
    heures = math.floor(estimation / 3600)
    minutes = math.floor((estimation % 3600) / 60)
    secondes = math.floor(estimation % 60)
    temps = str(heures) + "h " + str(minutes) + "m " + str(secondes) + "s"
    parametres[enums.Param.ESTIMATION] = temps

#appele la methode de traitement d'image selon le mode choisi
#si le nom de choix est invalide il le corrige (pour les sauvegardes)
def image_loading_array ():
    print(parametres[enums.Param.MODE])
    if parametres[enums.Param.MODE] == enums.Mode.CONTRASTE:
        cnc_v1.mapping_image()
    elif parametres[enums.Param.MODE] == enums.Mode.LUMINOSITE:
        cnc_v1.contour_image()
    elif parametres[enums.Param.MODE] == enums.Mode.COULEUR:
        cnc_v1.color_change()
    elif parametres[enums.Param.MODE] == enums.Mode.AUTO:
        cnc_v1.gestion_auto()
    else:
        option = str(parametres[enums.Param.MODE]).replace("Mode.", "")
        parametres[enums.Param.MODE] = enums.Mode[option]
        image_loading_array()

#actualise les informations sur l'image choisie et ses dimensions
def update_premiere_page():
    image = Image.open(parametres[enums.Param.PATH])
    limite_hauteur = test_facteur(image.height, hauteur_surface, float(parametres[enums.Param.ESPACEMENT]))
    limite_largeur = test_facteur(image.width, largeur_surface, float(parametres[enums.Param.ESPACEMENT]))
    if limite_hauteur >= limite_largeur:
        facteur_max = limite_largeur
    else:
        facteur_max = limite_hauteur
    global image_final
    image_final = cnc_v1.resizing(image, facteur_max)
    parametres[enums.Param.LARGEUR] = image_final.width
    parametres[enums.Param.HAUTEUR] = image_final.height

#trouve le facteur limitant dans le changement de grandeur de l'image originale
#return : retourne le facteur de grossissement calcule
def test_facteur(original,surface,espacement):
    capacite = surface / espacement
    mult = capacite / original
    return mult

