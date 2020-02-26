from PIL import Image
import tkinter as tk

def mappingImage(img, threshold):
    array = [[False]*img.width]*img.height
    print(img.height)
    print(img.width)
    i=0
    j=0
    for x in array:
        for y in array[i]:
            r,g,b = img.getpixel((i,j))
            if r < threshold:
                array[i][j] = True
                print ("r", end = '')
            elif g < threshold:
                array[i][j] = True
                print ("g", end = '')
            elif b < threshold:
                array[i][j] = True
                print("b", end = '')
            else:
                print (" ", end = '')
            i+=1
        i=0
        j+=1
        print("")

def resizing (img_original, width, height):
    img_final = img_original.resize((width,height))
    return img_final
    
def interface ():
    frame = tk.Frame
    
threshold = 40
img = Image.open("/home/pi/Documents/burger.jpeg")
width = 160
height = 90
resized_img = resizing(img, width, height)
mappingImage(resized_img,threshold)
