from PIL import Image
import tkinter as tk
import random
from array import *

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

    
    
    
    
    
    
def mapping_image(img, threshold):
    array = [[False for i in range(img.width)] for j in range(img.height)]
    print(img.height)
    print(img.width)
    i=0
    j=0
    for y in array:
        for x in y:
            r,g,b = img.getpixel((i,j))
            if r < threshold:
                x = True
                print ("█", end = '')
            elif g < threshold:
                x = True
                print ("█", end = '')
            elif b < threshold:
                x = True
                print("█", end = '')
            else:
                print (" ", end = '')
            i+=1
        i=0
        j+=1
        print("")

def contour_image(img, difference):
        
    liste_contour = [[False for i in range(img.height)] for j in range(img.width)]
    liste_pixels = [[0 for i in range(3)] for j in range(5)]
    
    i = 0
    j = 0
    for x in liste_contour :
        for y in x :
            try : 
                liste_pixels[0] = img.getpixel((i,j))
                liste_pixels[1] = img.getpixel((i+1,j))
                liste_pixels[2] = img.getpixel((i,j+1))
                liste_pixels[3] = img.getpixel((i-1,j))
                liste_pixels[4] = img.getpixel((i,j-1))
                
                liste_contour[i][j] = verification_contour(liste_pixels, difference)
            except : 
                print ("", end = '')

            finally :
                j +=1
        j=0
        i+=1
    affichage_booleen(liste_contour)

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


def resizing (img_original, facteur):

    print(img_original.width, end = 'Img originale width\n')

    print(img_original.height, end = 'Img originale height\n')
    img_final = img_original.resize((int(img_original.width*facteur),int(img_original.height*facteur)))
    
    print(img_final.width, end = 'Img final width\n')
    print(img_final.height, end = 'Img finale height\n')
    return img_final
    
def interface ():
    frame = tk.Frame
    
def set_height(h):
    global height 
    height = h

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

def hue_evaluate (array, compare):
    for pixel in array:
        if (pixel - array[0]) > compare:
            return True
        elif (array[0] - pixel) > compare:
            return True
    return False

def color_change (img, compare):
    tab_bool = [[False for i in range(img.height)] for j in range(img.width)]
    hue_array = [[0 for i in range(img.height)] for j in range(img.width)]
    liste_pixels = [0 for i in range(5)]
    
    
    i=0
    j=0
    for x  in hue_array:
        for y in x:
            r,g,b = img.getpixel((i,j))
            y = testHue(r,g,b)
            try :
                r,g,b =  img.getpixel((i,j))
                liste_pixels[0] = testHue(r,g,b)
                r,g,b =  img.getpixel((i+1,j))
                liste_pixels[1] = testHue(r,g,b) 
                r,g,b =  img.getpixel((i,j+1))
                liste_pixels[2] = testHue(r,g,b)
                r,g,b =  img.getpixel((i-1,j))
                liste_pixels[3] = testHue(r,g,b)
                r,g,b =  img.getpixel((i,j-1))
                liste_pixels[4] = testHue(r,g,b)
                
                tab_bool[i][j] = hue_evaluate(liste_pixels, compare)
            except : 
                print ("", end = '')
            finally :
                j+=1
        j=0
        i+=1
    affichage_booleen (tab_bool)


compare = 6
threshold = 60
difference = 34 

img = Image.open("/home/vincent/bdeb_cnc/images/angela.png")
facteur = 0.7
resized_img = resizing(img, facteur)
mapping_image(resized_img,threshold)
color_change(resized_img, difference)
contour_image(resized_img, difference)

#tableau = [[True, True, False, False, False],[True, True, True, False, False],[False, False, False, False, False],[True, True, True, True, True]]
#affichage_booleen(tableau)



