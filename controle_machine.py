import RPi.GPIO as GPIO
import donnees
from time import sleep
import time
import threading
from PIL import Image


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
    
    img = Image.open(donnees.PREVIEW_PATH)
    
   
    for i in range(img.height):
        for j in range(img.width):
            rgb_img = img.convert('RGB')
            r, g, b = rgb_img.getpixel((j, i))
            
            if r<200:
                point()
            prochain_point()
        prochaine_ligne()

            
                    
# Fait en sorte que le solenoide s'actionne pour l'impression
def impression_point():
    print('point imprime')

def droite():
    GPIO.output(DIR_X, SAH)
    GPIO.output(STEP_X, 1)
    sleep(DELAIS_STEP_X)
    GPIO.output(STEP_X, 0)
    sleep(DELAIS_STEP_X)

def gauche():
    GPIO.output(DIR_X, SH)
    GPIO.output(STEP_X, 1)
    sleep(DELAIS_STEP_X)
    GPIO.output(STEP_X, 0)
    sleep(DELAIS_STEP_X)

def haut():
    GPIO.output(DIR_Y, SH)
    GPIO.output(STEP_Y, 1)
    sleep(DELAIS_STEP_Y)
    GPIO.output(STEP_Y, 0)
    sleep(DELAIS_STEP_Y)

def bas():
    GPIO.output(DIR_Y, SAH)
    GPIO.output(STEP_Y, 1)
    sleep(DELAIS_STEP_Y)
    GPIO.output(STEP_Y, 0)
    sleep(DELAIS_STEP_Y)


# Fait avancer la buse au point suivant (à droite) 
def prochain_point():
   
    for i in range(int((float(donnees.espacement) / float(STEP_DISTANCE)))):
        GPIO.output(DIR_X, SAH)
        GPIO.output(STEP_X, 1)
        sleep(DELAIS_STEP_X)
        
        GPIO.output(STEP_X, 0)
        sleep(DELAIS_STEP_X)
        
        donnees.nb_step_x += 1

        print("buse tassee a droite d'un step")
    print("buse tassee a droite d'un point")
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)

# Fait passer la buse à la ligne suivante (hauteur) et la remet à gauche (début de la ligne)
def prochaine_ligne():
    GPIO.output(EN_Y, 0)
    for i in range(donnees.nb_step_x):
        GPIO.output(DIR_X, SH)
        GPIO.output(STEP_X, 1)
        sleep(DELAIS_STEP_X)

        GPIO.output(STEP_X, 0)
        sleep(DELAIS_STEP_X)
        donnees.nb_step_x -= 1 
        print('buse tassee a gauche dun step')
    print('buse tassee a gauche dun point')
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)

    for i in range(int(float(donnees.espacement)/float(STEP_DISTANCE))):
        GPIO.output(DIR_Y, SH)
        GPIO.output(STEP_Y, 1)
        sleep(DELAIS_STEP_Y)

        GPIO.output(STEP_Y, 0)
        sleep(DELAIS_STEP_Y)
        donnees.nb_step_y += 1
        print('buse tassee en bas dun step')
    print('buse tassee en bas dun point')
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)
    GPIO.output(EN_Y, 1)
# Remet la buse dans le coin en haut à gauche

def point_on():
    GPIO.output(TRS, 1)

def point_off():
    GPIO.output(TRS, 0)

def point():
    GPIO.output(TRS, 1)
    sleep(DELAIS_SOLENOIDE/2)
    GPIO.output(TRS, 0)
    sleep(DELAIS_SOLENOIDE/2)

def man_1():
    GPIO.output(EN_Y, 0)
    while(True):
        if GPIO.input(MAN_DROITE) == 1:
            droite()
        if GPIO.input(MAN_GAUCHE) == 1:
            gauche()
        if GPIO.input(MAN_HAUT) == 1:
            haut()
        if GPIO.input(MAN_BAS) == 1:
            bas()

def man_2():
    while(True):
        sleep(0.01)
        if GPIO.input(MAN_POINT) == 1:
            point_on()
        else:
            point_off()

    



def reset_buse():
    GPIO.output(EN_Y, 0)
    for i in range(donnees.nb_step_x):
        GPIO.output(DIR_X, SH)
        GPIO.output(STEP_X, 1)
        sleep(DELAIS_STEP_X)

        GPIO.output(STEP_X, 0)
        sleep(DELAIS_STEP_X)
        donnees.nb_step_x -= 1 
        print('buse tassee a gauche dun step')
    print('buse tassee a gauche dun point')
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)

    for i in range(donnees.nb_step_y):
        GPIO.output(DIR_Y, SAH)
        GPIO.output(STEP_Y, 1)
        sleep(DELAIS_STEP_Y)

        GPIO.output(STEP_Y, 0)
        sleep(DELAIS_STEP_Y)
        donnees.nb_step_y -= 1
        print('buse tassee en haut dun step')
    print('buse tassee en haut dun point')
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)
    GPIO.output(EN_Y, 1)



##############
# CONSTANTES #
##############

STEP_DISTANCE = 0.2     # Valeur en mm qui détermine la distance que doit parcourir la buse pour passer au point suivant et à la ligne suivante
                            # 1 step = 40mm(circonference) / 200 step(por 1 tour) = 0.2 mm / step
                            # 1 step = 40mm / 200 step = 0.2 mm / step
DELAIS_STEP_Y = 0.002     # Delais entre chaque step, en secondes, determine la vitesse
DELAIS_STEP_X = 0.0007    # Delais entre chaque step, en secondes, determine la vitesse
SPR = 200               # Nombre de Step Par Rotation
DELAIS_SOLENOIDE = 0.05  # Delais que doit passer le relais du solenoide en position activee pour que l'impression se fasse. ***MODIFIER DONNEES DIFFERENT MODES ?

#######################
# Variables de classe #
#######################

#nb_step_x = 0           #Compteur du nombre de step faits de gauche a droite dans le plan d'impression
#nb_step_y = 0           #Compteur du nombre de step faits de haut en bas dans le plan d'impression



#############################################################################
# Plan de reference #                                                       #
#####################                                                       #
#                                                                           #
#      Buse                                                                 #
#      ↓                      🢂 x                                           #
#   O------------------------O                                              #
#   | ***                    |                                              #
#   | ***   🡆  🡆  🡆  🡆  🡆 ⤶  |                                              #
#   | ***    <------------   |                                              #
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |          Haut    🡹 (y)                       #
#   |        <------------   |          Bas     🡻 (y)                       #
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |          Gauche  🡸 (x)                       #
#   |        <------------   |          Droite  🡺 (x)                       #
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |                                              #
#   |        <------------   |                                              #
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |                                              #
#   |        <------------   |                                              #
#   |       🡆  🡆  🡆  🡆  🡆 ⤶  |                                              #
#   |        <------------   |                                              #
#   |                        |                                              #
#   O------------------------O                                              #
#  🢃                                                                        #
#  y                                                                        #
#                                                                           #
#  Note : impression de gauche a droite, de haut en bas (toujours)          #
#                                                                           #
#############################################################################


###################
# Setup pins GPIO #
###################

EN_X = 2                # Pin poour activer le controleur 1 (X)
EN_Y = 3                # Pin poour activer le controleur 2 (Y)
DIR_X = 20              # Numero de la pin utilisee pour la direction du stepper deplacant de gauche a droite 
DIR_Y = 19              # Numero de la pin utilisee pour la direction du stepper deplacant de haut en bas
STEP_X = 21             # Numero de la pin utilisee pour activer d'un step le stepper deplacant de gauche a droite 
STEP_Y = 26             # Numero de la pin utilisee pour activer d'un step le stepper deplacant de haut en bas
MAN_DROITE = 15
MAN_GAUCHE = 14
MAN_HAUT = 22
MAN_BAS = 18
MAN_POINT = 27

SH = 1                  # Valeur du sens de rotation horaire (1)
SAH = 0                 # Valeur du sens de rotation antihoraire (0)
TRS = 4


# Initialisation des pins et du layout GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_X, GPIO.OUT)
GPIO.setup(DIR_Y, GPIO.OUT)
GPIO.setup(EN_X, GPIO.OUT)
GPIO.setup(EN_Y, GPIO.OUT)
GPIO.setup(STEP_X, GPIO.OUT)
GPIO.setup(STEP_Y, GPIO.OUT)
GPIO.setup(TRS, GPIO.OUT)
GPIO.setup(MAN_DROITE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MAN_GAUCHE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MAN_HAUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MAN_BAS, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MAN_POINT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


###########################################
# Code test a rouler apres initialisation #
###########################################

#for i in range(50):
#    for i in range(50):
#        point()
#        prochain_point()
#    prochaine_ligne()

try:
    
    GPIO.output(TRS, 0)
        
    impression()

    reset_buse()


#    for i in range(10):
#        prochaine_ligne()
#        for i in range(10):
#            prochain_point()
#    for i in range(10):
#        point()
#    for i in range(10):
#        prochain_point()
#        point()
#    prochaine_ligne()
#
#
#    for i in range(100):
#        prochaine_ligne()
#    for i in range(100):
#        prochain_point()
#    for i in range(100):
#        prochaine_ligne()
#    reset_buse()


    t1 = threading.Thread(target=man_1)
    t2 = threading.Thread(target=man_2)


    t1.start()
    t2.start()

    t1.join()
    t2.join()


#    while(True):
#        
#        if GPIO.input(MAN_DROITE) == 1:
#            droite()
#
#        if GPIO.input(MAN_GAUCHE) == 1:
#            gauche()
#
#        if GPIO.input(MAN_HAUT) == 1:
#            haut()
#
#        if GPIO.input(MAN_BAS) == 1:
#            bas()
#
#        if GPIO.input(MAN_POINT) == 1:
#            point()

except:
    GPIO.cleanup()


#GPIO.cleanup()










################################################################################################################################################################





