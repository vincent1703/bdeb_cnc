import RPi.GPIO as GPIO
    import donnees



def impression(image):
    if(image = contour) :
        array = donnees.image_contour_booleen
        hauteur = donnees.image_contour["hauteur"]
        largeur = donnees.image_contour["largeur"]
        
    reset_buse()

    i=0
    j=0

    for x in array:
        for y in x:
            if array[i][j]==True:
                impression_point()
            prochain_point()
            j += 1
        i += 1
        prochaine_ligne()
        j =  0



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
hauteur = 1
largeur = 1

hauteur_mm = 1
largeur_mm = 1


