#import RPi.GPIO as GPIO
import donnees

def impression_fake():
    global array
    array = donnes.image_booleen
    
     for i in range(len(array[0])):
        for j in range(len(array)):
            #print(i, end = 'i ')
            #print(j, end = 'j  ')
            if array[j][i] == True:
                print("0", end = '')
            else:
                print(" ", end = '')
        print("")


def impression():
    global array
    array = donnees.image_booleen
    global espacement
    espacement = donnees.espacement

    reset_buse()

    for i in range(len(array[0])):
        for j in range(len(array)):
            #print(i, end = 'i ')
            #print(j, end = 'j  ')
            if array[j][i] == True:
                impression_point()
            prochain_point()                                               
                    
        prochaine_ligne()


# Fait en sorte que le petit servo imprime un point
def impression_point():

# Fait avancer la buse au point suivant (à droite) 
def prochain_point():

# Fait passer la buse à la ligne suivante (hauteur) et la remet à gauche (début de la ligne)
def prochaine_ligne():

# Remet la buse dans le coin en haut à gauche
def reset_buse():

# Valeur en mm qui détermine la distance que doit parcourir la buse pour passer au point suivant et à la ligne suivante
espacement = 1
array = 0
