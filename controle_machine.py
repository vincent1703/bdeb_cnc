import RPi.GPIO as GPIO
import donnees
from time import sleep

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


# Fait en sorte que le solenoide s'actionne pour  l'impression
def impression_point():
    print('point imprime')



# Fait avancer la buse au point suivant (à droite) 
def prochain_point():
   
    for i in range(int((float(donnees.espacement) / float(STEP_DISTANCE)))):
        GPIO.output(DIR_X, SH)
        GPIO.output(STEP_X, 1)
        sleep(0.002)
        GPIO.output(STEP_X, 0)
        sleep(0.002)
        global nb_step_x
        nb_step_x += 1

        print("buse tassee a droite d'un step")
    print("buse tassee a droite d'un point")
    print(nb_step_x)
    print(nb_step_y)

# Fait passer la buse à la ligne suivante (hauteur) et la remet à gauche (début de la ligne)
def prochaine_ligne():
    print('patate')

# Remet la buse dans le coin en haut à gauche
def reset_buse():
    print('patate')























##############
# CONSTANTES #
##############

STEP_DISTANCE = 0.2     # Valeur en mm qui détermine la distance que doit parcourir la buse pour passer au point suivant et à la ligne suivante
                            # 1 step = 40mm(circonference) / 200 step(por 1 tour) = 0.2 mm / step
                            # 1 step = 40mm / 200 step = 0.2 mm / step
DELAIS = 0.002          # Delais entre chaque step, en secondes, determine la vitesse
SPR = 200               # Nombre de Step Par Rotation


#######################
# Variables de classe #
#######################

nb_step_x = 0           #Compteur du nombre de step faits de gauche a droite dans le plan d'impression
nb_step_y = 0           #Compteur du nombre de step faits de haut en bas dans le plan d'impression



#####################
# Plan de reference #
#####################
#
#      Buse 
#      ↓                      🢂 x
#   O------------------------O
#   | ***                    |
#   | ***   🡆  🡆  🡆  🡆  🡆 ⤶  |
#   | ***    <------------   |
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |          Haut    🡹 (y)
#   |        <------------   |          Bas     🡻 (y)
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |          Gauche  🡸 (x)
#   |        <------------   |          Droite  🡺 (x)
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |
#   |        <------------   |
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |
#   |        <------------   |
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |
#   |        <------------   |
#   |                        |
#   O------------------------O
#  🢃
#  y
# 
#  Note : impression de gauche a droite, de haut en bas, en mode portrait (toujours)
#


###################
# Setup pins GPIO #
###################

DIR_X = 20              # Numero de la pin utilisee pour la direction du stepper deplacant de gauche a droite 
DIR_Y = 19              # Numero de la pin utilisee pour la direction du stepper deplacant de haut en bas
STEP_X = 21             # Numero de la pin utilisee pour activer d'un step le stepper deplacant de gauche a droite 
STEP_Y = 26             # Numero de la pin utilisee pour activer d'un step le stepper deplacant de haut en bas
SH = 1                  # Valeur du sens de rotation horaire (1)
SAH = 0                 # Valeur du sens de rotation antihoraire (0)

# Initialisation des pins et du layout GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_X, GPIO.OUT)
GPIO.setup(DIR_Y, GPIO.OUT)
GPIO.setup(STEP_X, GPIO.OUT)
GPIO.setup(STEP_Y, GPIO.OUT)


for i in range(40):
    prochain_point()


