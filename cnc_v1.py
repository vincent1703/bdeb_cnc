from PIL import Image
import tkinter as tk
import random

def affichage_booleen (array):
    for x in array:
        for y in x:
            if y == True:
                print("█", end = '')
            else :
                print(" ", end = '')
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
        
    liste_contour = [[False for i in range(img.width)] for j in range(img.height)]
    liste_pixels = [[0 for i in range(3)] for j in range(5)]
    
    s = 0
    t = 0
    for p in liste_contour :
        for q in p :
            try : 
                liste_pixels[0] = img.getpixel((t,s))
                liste_pixels[1] = img.getpixel((t+1,s))
                liste_pixels[2] = img.getpixel((t,s+1))
                liste_pixels[3] = img.getpixel((t-1,s))
                liste_pixels[4] = img.getpixel((t,s-1))
                
                liste_contour[s][t] = verification_contour(liste_pixels, difference)
            except : 
                print ("", end = '')

            finally :
                t +=1
        t=0
        s+=1

            
    
    
    
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


def resizing (img_original, width, height):
    img_final = img_original.resize((width,height))
    return img_final
    
def interface ():
    frame = tk.Frame
    
def set_height(h):
    global height 
    height = h

def set_width(w):
    global width 
    width = w

threshold = 60
difference = 34 

img = Image.open("/home/patate42/bdeb_cnc/images/nou.png")
width = 350
height = 238
resized_img = resizing(img, width, height)
mapping_image(resized_img,threshold)

contour_image(resized_img, difference)

tableau = [[True, True, False, False, False],[True, True, True, False, False],[False, False, False, False, False],[True, True, True, True, True]]
affichage_booleen(tableau)

print(height)
set_height(33)
print(height)


