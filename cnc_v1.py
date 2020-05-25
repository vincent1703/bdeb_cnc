from PIL import Image, ImageDraw
import random
import donnees
import enums
import sys
import math
import os
from array import *

###############
### CHOIX 0 ###
###############
#prend une image et met un point noir ou gris dans une image de meme dimension
#choisi si un point est gris noir ou blanc selon le rgb de chque pixel
#une image preview est generee et sauvegardee
def mapping_image():
    noir = int(donnees.parametres[enums.Param.THRESHOLD])
    gris = math.floor(noir * 1.6)
    img = donnees.image_final
    preview = preparation_preview()
    pixels = preview.load()
    for i in range(donnees.parametres[enums.Param.HAUTEUR]):
        for j in range(donnees.parametres[enums.Param.LARGEUR]):
            r,g,b = img.getpixel((j,i))
            if r < gris or g < gris or b < gris:
                if r < noir or g < noir or b < noir:
                    pixels[j,i] = (0,0,0)
                else:
                    pixels[j,i] = (60,60,60)
    preview.save(donnees.parametres[enums.Param.PREVIEW])


#prepare le gabarit du preview utilise dans les autres methodes
#retourne une image blanche de la bonne taille
def preparation_preview():
    preview = Image.new('RGB', (donnees.parametres[enums.Param.LARGEUR], donnees.parametres[enums.Param.HAUTEUR]), (255,255,255))
    preview.save(donnees.parametres[enums.Param.PREVIEW])
    return preview

###############
### CHOIX 1 ###
###############
#prend les pixels adjacents pour les envoyer dans une autre methode
#prend le resultat et met gris noir ou blanc comme point du preview
#remplie l'image preview
def contour_image():
    img = donnees.image_final
    preview = preparation_preview()
    pixels = preview.load()
    liste_pixels = [[0 for j in range(3)] for i in range(5)]
    for i in range(donnees.parametres[enums.Param.HAUTEUR]):
        for j in range(donnees.parametres[enums.Param.LARGEUR]):
            try : 
                liste_pixels[0] = img.getpixel((j,i))
                liste_pixels[1] = img.getpixel((j+1,i))
                liste_pixels[2] = img.getpixel((j,i+1))
                liste_pixels[3] = img.getpixel((j-1,i))
                liste_pixels[4] = img.getpixel((j,i-1))
                
                pixels[j,i] = verification_contour(liste_pixels)
            except : 
                pass
    preview.save(donnees.parametres[enums.Param.PREVIEW])

#param liste_pixels : tableau de pixels duquel sont pris les valeurs rgb
#compare les variations entre les couleurs de pixels adjascents
#return: retourne la couleur attribuee au pixel principal choisi
def verification_contour (liste_pixels):
    r,g,b = liste_pixels[0]
    noir = donnees.parametres[enums.Param.DIFFERENCE]
    gris = math.floor(noir * 0.8)
    for x in liste_pixels :
        if r-x[0] > gris or g-x[1] > gris or b-x[2] > gris:
            if r-x[0] > noir or g-x[1] > noir or b-x[2] > noir:
                return (0,0,0)
            return (60,60,60)
    return (255,255,255)


###############
### CHOIX 2 ###
###############
#transforme une valeur rgb pour donner le hue (de 0 a 360)
#return: valeur de hue
def testHue (r,g,b):
    M = max(r,g,b)
    m = min(r,g,b)
    c = M-m
    if c == 0:
        return 0
    if M == r:
        temp = ((g-b)/c) % 6
    elif M == g:
        temp = (b-r)/c + 2
    else:
        temp = (r-g)/c + 4
    return 60*temp

#param array : tableau de valeurs de hue
#compare les variations de hue aux pixels adjascents
#return: valeur rgb a mettre pour le pixel choisi
def hue_evaluate (array):
    noir = donnees.parametres[enums.Param.COMPARE]
    gris = math.floor(noir * 0.8)
    for pixel in array:
        if abs(pixel - array[0]) > gris:
            if (array[0] - pixel) > noir:
                return (0,0,0)
            return (60,60,60)
    return (255,255,255)

#prend une image et rempli le preview selon les valeurs de hue des pixels
#rempli un tableau avec les valeurs de hue pour comparaison
#rempli une image preview de gris noir ou blanc
def color_change ():
    img = donnees.image_final
    preview = preparation_preview()
    pixels = preview.load()
    liste_pixels = [0 for i in range(5)]    
    for i in range(donnees.parametres[enums.Param.HAUTEUR]):
        for j in range(donnees.parametres[enums.Param.LARGEUR]):
            try :
                r,g,b =  img.getpixel((j,i))
                liste_pixels[0] = testHue(r,g,b)
                r,g,b =  img.getpixel((j+1,i))
                liste_pixels[1] = testHue(r,g,b) 
                r,g,b =  img.getpixel((j,i+1))
                liste_pixels[2] = testHue(r,g,b)
                r,g,b =  img.getpixel((j-1,i))
                liste_pixels[3] = testHue(r,g,b)
                r,g,b =  img.getpixel((j,i-1))
                liste_pixels[4] = testHue(r,g,b)
                
                pixels[j,i] = hue_evaluate(liste_pixels)
            except : 
                print ("", end = '')
    preview.save(donnees.parametres[enums.Param.PREVIEW])


###############
### CHOIX 3 ###
###############
#prend une image et la converti au mode luminosite
#se sert de la valeur de luminosite selon un seuil
#cree un preview avec les valeurs de gris de noir et de blanc
def gestion_auto():
    img = donnees.image_final.convert('L')
    noir = donnees.parametres[enums.Param.THRESHOLD]
    gris = noir * 1.6
    preview = preparation_preview()
    pixels = preview.load()
    for i in range (donnees.parametres[enums.Param.HAUTEUR]):
        for j in range (donnees.parametres[enums.Param.LARGEUR]):
            l = img.getpixel((j,i))
            if l < gris:
                if l < noir:
                    pixels[j,i] = (0,0,0)
                else:
                    pixels[j,i] = (60,60,60)
    preview.save(donnees.parametres[enums.Param.PREVIEW])


#########################
### OUVERTURE FICHIER ###
#########################
#param path : chemin du fichier
#charge les elements dans le dictionnaire parametres situe dans donnees
#converti les informations dans le bon type
def load_fichier(path):
    fichier = open(path, "r")
    contenu = fichier.read()
    separation = contenu.splitlines()
    print("nom du fichier: " + os.path.basename(path))
    i=0
    for element in separation:
        try:
            donnees.parametres[enums.Param(i)] = float(element)
        except:
            donnees.parametres[enums.Param(i)] = element
        try:
            donnees.parametres[enums.Param(i)] = int(element)
        except:
            pass
        i+=1
    fichier.close()

###########################
### ENREGISTRER FICHIER ###
###########################
#param name : nom de la sauvegarde
#sauve dans un fichier du nom du choisi les valeurs de parametres situe dans donnees
def save_fichier(name):
    path = os.path.dirname(os.path.abspath(__file__)) + "/sauvegardes/" + name + ".save"
    fichier = open(path, "w")
    for info in enums.Param:
        fichier.write(str(donnees.parametres[info]) + "\n")
    fichier.close()

#############
### TEMPS ###
#############
#passe par chaque point de l'image et estime le temps selon la couleur du point
#return: temps d'impression prevu en secondes
def time_estimation ():
    time_in_seconds = 0.0
    nbr_gris = 0
    nbr_noir = 0
    delais = choix_delais()
    image = Image.open(donnees.parametres[enums.Param.PREVIEW])
    for i in range (donnees.parametres[enums.Param.HAUTEUR]):
        for j in range (donnees.parametres[enums.Param.LARGEUR]):
            if image.getpixel((j,i)) == (60,60,60):
                nbr_gris += 1
                time_in_seconds += delais
            elif image.getpixel((j,i)) == (0,0,0):
                nbr_noir += 1
                time_in_seconds += delais
            else :
                pass
            time_in_seconds += float(8*donnees.DELAIS_STEP*donnees.parametres[enums.Param.ESPACEMENT]/0.2)
    print ("nbr points gris: " + str(nbr_gris))
    print ("nbr points noirs: " + str(nbr_noir))
    print("nbr points total: "+ str(donnees.parametres[enums.Param.LARGEUR] * donnees.parametres[enums.Param.HAUTEUR]))
    return time_in_seconds

def choix_delais():
    DELAIS_SOLENOIDE = 0.05
    if donnees.parametres[enums.Param.VITESSE] == enums.Vitesse.LENT:
        DELAIS_SOLENOIDE = donnees.DELAIS_LENT
    elif donnees.parametres[enums.Param.VITESSE] == enums.Vitesse.MOYEN:
        DELAIS_SOLENOIDE = donnees.DELAIS_MOYEN
    else:
        DELAIS_SOLENOIDE = donnees.DELAIS_VITE
    return DELAIS_SOLENOIDE


##############
### TAILLE ###
##############
#param img_original : image initiale
#param facteur : facteur de grossissement de l'image en float
#return: image de dimension modifiee par le facteur de grossissement
def resizing (img_original, facteur):
    return  img_original.resize((int(img_original.width*facteur),int(img_original.height*facteur)))

