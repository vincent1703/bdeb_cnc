from PIL import Image

def mappingImage(img, threshold):
    array = [[False]*img.height]*img.width
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
    print(i)
    print(j)

def resizing (img_original, width, height):
    img_final = img_original.resize((width,height))
    return [Image, img_final];
    
threshold = 180
img = Image.open("/home/pi/Documents/couronne.jpeg")
print(img.class)
width = 200
height = 200
img = resizing(img, width, height)
mappingImage(img,threshold)
