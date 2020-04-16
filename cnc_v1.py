from PIL import Image, ImageDraw
import random
import donnees
import math
from array import *


###############
### CHOIX 0 ###
###############
def mapping_image():
    threshold = donnees.threshold
    gris = math.floor(donnees.threshold * 1.6)
    img = donnees.image_final
    array = [[0 for j in range(img.width)] for i in range(img.height)]
    for i in range(len(array)):
        for j in range(len(array[i])):
            r,g,b = img.getpixel((j,i))
            if r < gris:
                if r < donnees.threshold:
                    array[i][j] = 2
                else:
                    array[i][j] = 1
            elif g < gris:
                if g < donnees.threshold:
                    array[i][j] = 2
                else:
                    array[i][j] = 1
            elif b < gris:
                if b < donnees.threshold:
                    array[i][j] = 2
                else:
                    array[i][j] = 1
    return array


###############
### CHOIX 1 ###
###############
def contour_image():
    img = donnees.image_final
    array = [[0 for j in range(img.width)] for i in range(img.height)]
    liste_pixels = [[0 for j in range(3)] for i in range(5)]
    for i in range(len(array)):
        for j in range(len(array[i])):
            try : 
                liste_pixels[0] = img.getpixel((j,i))
                liste_pixels[1] = img.getpixel((j+1,i))
                liste_pixels[2] = img.getpixel((j,i+1))
                liste_pixels[3] = img.getpixel((j-1,i))
                liste_pixels[4] = img.getpixel((j,i-1))
                
                array[i][j] = verification_contour(liste_pixels)
            except : 
                print ("", end = '')
    return array


def verification_contour (liste_pixels):
    r,g,b = liste_pixels[0]
    gris = math.floor(donnees.difference * 0.8)
    for x in liste_pixels :
        if r - x[0] > gris:
            if r-x[0] > donnees.difference:
                return 2
            return 1
        if g - x[1] > gris:
            if g-x[1] > donnees.difference:
                return 2
            return 1
        if b - x[2] > gris:
            if b-x[2] > donnees.difference:
                return 2
            return 1
    return 0


###############
### CHOIX 2 ###
###############
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

def hue_evaluate (array):
    gris = math.floor(donnees.compare * 0.8)
    for pixel in array:
        if abs(pixel - array[0]) > gris:
            if (array[0] - pixel) > donnees.compare:
                return 2
            return 1
    return 0

def color_change ():
    img = donnees.image_final
    array = [[0 for j in range(img.width)] for i in range(img.height)]
    liste_pixels = [0 for i in range(5)]    
    for i in range(len(array)):
        for j in range(len(array[i])):
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
                
                array[i][j] = hue_evaluate(liste_pixels)
            except : 
                print ("", end = '')
    return array


#############
### TEMPS ###
#############
def time_estimation ():
    time_in_seconds = 0.0
    nbr_gris = 0
    nbr_noir = 0
    for i in range (len(donnees.image_booleen)):
        for j in range (len(donnees.image_booleen[i])):
            if donnees.image_booleen[i][j] == 1:
                nbr_gris += 1
                time_in_seconds += math.floor(donnees.DELAIS_SOLENOIDE * 0.5)
            elif donnees.image_booleen[i][j] == 2:
                nbr_noir += 1
                time_in_seconds += donnees.DELAIS_SOLENOIDE
            else :
                time_in_seconds += donnees.DELAIS_STEP
    print ("nbr points gris: " + str(nbr_gris))
    print ("nbr points noirs: " + str(nbr_noir))
    print("nbr points total: " + str(len(donnees.image_booleen) * len(donnees.image_booleen[i])))
    return time_in_seconds


##############
### TAILLE ###
##############
def resizing (img_original, facteur):
    img_final = img_original.resize((int(img_original.width*facteur),int(img_original.height*facteur)))
    print(img_final.width,end=' pixels de large\t')
    donnees.largeur_nouvelle = img_final.width
    print(img_final.height,end=' pixels de haut\n')
    donnees.hauteur_nouvelle = img_final.height
    return img_final


#####################
### IMAGE PREVIEW ###
#####################
def generate_preview(array):
    preview = Image.new('RGB',(donnees.image_final.width, donnees.image_final.height), (255,255,255))
    preview.save(donnees.preview_path)
    pixels = preview.load()
    for i in range(len(donnees.image_booleen)):
        for j in range(len(donnees.image_booleen[i])):
            try:
                if donnees.image_booleen[i][j] == 2:
                    pixels[j,i] = (0,0,0)
                elif donnees.image_booleen[i][j] == 1:
                    pixels[j,i] = (125,125,125)
            except:
                print(i,end=" i\t")
                print(j,end=" j\n")
    preview.save(donnees.preview_path)


