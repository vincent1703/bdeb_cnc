from PIL import Image
import tkinter as tk

def mappingImage(img, threshold):
    array = [[False]*img.width]*img.height
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

def resizing (img_original, width, height):
    img_final = img_original.resize((width,height))
    return img_final
    
def interface ():
    frame = tk.Frame
    
threshold = 40
img = Image.open("/home/pi/Documents/testImage.jpeg")
width = 200
height = 200
resized_img = resizing(img, width, height)
mappingImage(resized_img,threshold)
