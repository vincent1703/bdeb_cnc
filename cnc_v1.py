from PIL import Image, ImageDraw
import random
import donnees
from array import *


###############
### CHOIX 0 ###
###############
def mapping_image():
    threshold = donnees.threshold
    img = donnees.image_final
    array = [[False for i in range(img.width)] for j in range(img.height)]
    i=0
    j=0
    for y in array:
        for x in y:
            r,g,b = img.getpixel((i,j))
            if r < threshold:
                array[j][i] = True
            elif g < threshold:
                array[j][i] = True
            elif b < threshold:
                array[j][i] = True
            else:
                print ("", end = '')
            i+=1
        i=0
        j+=1
    return array


###############
### CHOIX 1 ###
###############
def contour_image():
    img = donnees.image_final
    array = [[False for i in range(img.width)] for j in range(img.height)]
    liste_pixels = [[0 for i in range(3)] for j in range(5)]
    i = 0
    j = 0
    for x in array :
        for y in x :
            try : 
                liste_pixels[0] = img.getpixel((j,i))
                liste_pixels[1] = img.getpixel((j+1,i))
                liste_pixels[2] = img.getpixel((j,i+1))
                liste_pixels[3] = img.getpixel((j-1,i))
                liste_pixels[4] = img.getpixel((j,i-1))
                
                array[i][j] = verification_contour(liste_pixels, donnees.difference)
            except : 
                print ("", end = '')

            finally :
                j +=1
        j=0
        i+=1
    return array


def verification_contour (liste_pixels, difference):
    r,g,b = liste_pixels[0]
    for x in liste_pixels :
        if r - x[0] > difference :
            return True
        if g - x[1] > difference :
            return True
        if b - x[2] > difference :
            return True
    return False    


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
    for pixel in array:
        if (pixel - array[0]) > donnees.compare:
            return True
        elif (array[0] - pixel) > donnees.compare:
            return True
    return False

def color_change ():
    img = donnees.image_final
    array = [[False for i in range(img.width)] for j in range(img.height)]
    liste_pixels = [0 for i in range(5)]    
    i=0
    j=0
    for x  in array:
        for y in x:
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
            finally :
                j+=1
        j=0
        i+=1
    return array


#############
### TEMPS ###
#############
def time_estimation ():
    time_in_seconds = 0.0
    nbr_true=0
    for i in range (len(donnees.image_booleen)):
        for j in range (len(donnees.image_booleen[i])):
            if donnees.image_booleen[i][j] == True:
                nbr_true = nbr_true + 1
                time_in_seconds = time_in_seconds + donnees.DELAIS_SOLENOIDE
            else :
                time_in_seconds = time_in_seconds + donnees.DELAIS_STEP
    print ("nbr a imprimer: " + str(nbr_true))
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
    i=0
    j=0
    for i in range(len(donnees.image_booleen)):
        for j in range(len(donnees.image_booleen[i])):
            try:
                if donnees.image_booleen[i][j] == True:
                    pixels[j,i] = (0,0,0)
                else:
                    pixels[j,i] = (255,255,255)
            except:
                print(i,end=" i\t")
                print(j,end=" j\n")
            j+=1
        j=0
        i+=1
    preview.save(donnees.preview_path)


