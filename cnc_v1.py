from PIL import Image, ImageDraw
import random
import donnees
from array import *

def generate_preview(array):
    preview = Image.new('RGB',(donnees.image_final.width, donnees.image_final.height), (255,255,255))
    
    preview.save(donnees.preview_path)
    
    pixels = preview.load()
    i=0
    j=0
    for i in range(len(donnees.image_booleen)):
        for j in range(len(donnees.image_booleen[i])):
            try:
                if(i == 20):
                    pixels[j,i] = (255,0,0)
                elif donnees.image_booleen[i][j] == True:
                    pixels[j,i] = (0,0,0)
                else:
                    pixels[j,i] = (255,255,255)
            except:
                print(i,end=" i\t")
                print(j,end=" j\n")
            j+=1
        j=0
        i+=1
    print("test")
    preview.save(donnees.preview_path)

#utile pour debug seulement
def affichage_booleen (array):
   

    print(len(array), end = 'len array')

    print(len(array[0]), end = 'len array[0]')

    for i in range(len(array[0])):
        for j in range(len(array)):
            #print(i, end = 'i ')
            #print(j, end = 'j  ')
            if array[j][i] == True:

                print("█", end = '')
            else :
                print(' ', end = '')
        print("")

    
    
def mapping_image():
    threshold = donnees.threshold
    img = donnees.image_final
    array = [[False for i in range(img.width)] for j in range(img.height)]
    print(img.height)
    print(img.width)
    i=0
    j=0
    for y in array:
        for x in y:
            r,g,b = img.getpixel((i,j))
            if r < threshold:
                array[j][i] = True
                #print ("█", end = '')
            elif g < threshold:
                array[j][i] = True
                #print ("█", end = '')
            elif b < threshold:
                array[j][i] = True
                #print("█", end = '')
            else:
                print ("", end = '')
            i+=1
        i=0
        j+=1
        #print("")
    return array


def contour_image():
    img = donnees.image_final
    array = [[False for i in range(img.width)] for j in range(img.height)]
    liste_pixels = [[0 for i in range(3)] for j in range(5)]
    
    i = 0
    j = 0
    for x in array :
        for y in x :
            try : 
                liste_pixels[0] = img.getpixel((i,j))
                liste_pixels[1] = img.getpixel((i+1,j))
                liste_pixels[2] = img.getpixel((i,j+1))
                liste_pixels[3] = img.getpixel((i-1,j))
                liste_pixels[4] = img.getpixel((i,j-1))
                
                array[j][i] = verification_contour(liste_pixels, donnees.difference)
            except : 
                print ("", end = '')

            finally :
                j +=1
        j=0
        i+=1
    #affichage_booleen(array)
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


#commentaires de debug inutiles
def resizing (img_original, facteur):

    #print(img_original.width, end = 'Img originale width\n')

    #print(img_original.height, end = 'Img originale height\n')
    img_final = img_original.resize((int(img_original.width*facteur),int(img_original.height*facteur)))
    print("resize complet")
    #print(img_final.width, end = 'Img final width\n')
    #print(img_final.height, end = 'Img finale height\n')
    return img_final
    

#methode inutile
def set_height(h):
    global height 
    height = h
#methode inutile
def set_width(w):
    global width 
    width = w



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
    hue_array = [[0 for i in range(img.width)] for j in range(img.height)]
    liste_pixels = [0 for i in range(5)]
    
    
    i=0
    j=0
    for x  in hue_array:
        for y in x:
            r,g,b = img.getpixel((j,i))
            y = testHue(r,g,b)
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
                
                array[j][i] = hue_evaluate(liste_pixels)
            except : 
                print ("", end = '')
            finally :
                j+=1
        j=0
        i+=1
    #affichage_booleen (array)
    return array

def time_estimation ():
    time_in_seconds = 0.0
    for i in range (donnes.image_booleen.len):
        for j in range (donnees.image_booleen[i].len):
            if donnees.image_booleen[i][j] == True:
                time_in_seconds += 0.2
            else :
                time_in_seconds += 0.05
            j+=1
        j=0
        i+=1
    return time_in_seconds

compare = 6
threshold = 60
difference = 34 

img = Image.open("images/angela.png")
facteur = 0.7

######################
### tests initiaux ###
######################
#resized_img = resizing(img, facteur)
#mapping_image(resized_img,threshold)
#color_change(resized_img, difference)
#contour_image(resized_img, difference)

#tableau = [[True, True, False, False, False],[True, True, True, False, False],[False, False, False, False, False],[True, True, True, True, True]]
#affichage_booleen(tableau)



