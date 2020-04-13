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


# Fait en sorte que le solenoide s'actionne pour l'impression
def impression_point():
    print('point imprime')



# Fait avancer la buse au point suivant (à droite) 
def prochain_point():
   
    for i in range(int((float(donnees.espacement) / float(STEP_DISTANCE)))):
        GPIO.output(DIR_X, SH)
        GPIO.output(STEP_X, 1)
        sleep(DELAIS_STEP)
        
        GPIO.output(STEP_X, 0)
        sleep(DELAIS_STEP)
        
        donnees.nb_step_x += 1

        print("buse tassee a droite d'un step")
    print("buse tassee a droite d'un point")
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)

# Fait passer la buse à la ligne suivante (hauteur) et la remet à gauche (début de la ligne)
def prochaine_ligne():
    for i in range(donnees.nb_step_x):
        GPIO.output(DIR_X, SAH)
        GPIO.output(STEP_X, 1)
        sleep(DELAIS_STEP)

        GPIO.output(STEP_X, 0)
        sleep(DELAIS_STEP)
        donnees.nb_step_x -= 1 
        print('buse tassee a gauche dun step')
    print('buse tassee a gauche dun point')
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)

    for i in range(int(float(donnees.espacement)/float(STEP_DISTANCE))):
        GPIO.output(DIR_Y, SH)
        GPIO.output(STEP_Y, 1)
        sleep(DELAIS_STEP)

        GPIO.output(STEP_Y, 0)
        sleep(DELAIS_STEP)
        donnees.nb_step_y += 1
        print('buse tassee en bas dun step')
    print('buse tassee en bas dun point')
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)

# Remet la buse dans le coin en haut à gauche
def reset_buse():
    for i in range(donnees.nb_step_x):
        GPIO.output(DIR_X, SAH)
        GPIO.output(STEP_X, 1)
        sleep(DELAIS_STEP)

        GPIO.output(STEP_X, 0)
        sleep(DELAIS_STEP)
        donnees.nb_step_x -= 1 
        print('buse tassee a gauche dun step')
    print('buse tassee a gauche dun point')
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)

    for i in range(donnees.nb_step_y):
        GPIO.output(DIR_Y, SAH)
        GPIO.output(STEP_Y, 1)
        sleep(DELAIS_STEP)

        GPIO.output(STEP_Y, 0)
        sleep(DELAIS_STEP)
        donnees.nb_step_y -= 1
        print('buse tassee en haut dun step')
    print('buse tassee en haut dun point')
    print(donnees.nb_step_x)
    print(donnees.nb_step_y)




##############
# CONSTANTES #
##############

STEP_DISTANCE = 0.2     # Valeur en mm qui détermine la distance que doit parcourir la buse pour passer au point suivant et à la ligne suivante
                            # 1 step = 40mm(circonference) / 200 step(por 1 tour) = 0.2 mm / step
                            # 1 step = 40mm / 200 step = 0.2 mm / step
DELAIS_STEP = 0.002     # Delais entre chaque step, en secondes, determine la vitesse
SPR = 200               # Nombre de Step Par Rotation
DELAIS_SOLENOIDE = 0.5  # Delais que doit passer le relais du solenoide en position activee pour que l'impression se fasse. ***MODIFIER DONNEES DIFFERENT MODES ?

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
SH = 1                  # Valeur du sens de rotation horaire (1)
SAH = 0                 # Valeur du sens de rotation antihoraire (0)

# Initialisation des pins et du layout GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_X, GPIO.OUT)
GPIO.setup(DIR_Y, GPIO.OUT)
GPIO.setup(EN_X, GPIO.OUT)
GPIO.setup(EN_Y, GPIO.OUT)
GPIO.setup(STEP_X, GPIO.OUT)
GPIO.setup(STEP_Y, GPIO.OUT)



###########################################
# Code test a rouler apres initialisation #
###########################################


for i in range (5):
    prochain_point()

prochaine_ligne()
for i in range(20):
    prochain_point()

prochaine_ligne()
for i in range(30):
    prochain_point()

prochaine_ligne()
for i in range(60):
    prochain_point()

prochaine_ligne()
for i in range(100):
    prochain_point()

prochaine_ligne()

for i in range(50):
    prochain_point()

prochaine_ligne()

for i in range (30):
    prochain_point()

prochaine_ligne()
prochaine_ligne()

reset_buse()



GPIO.cleanup()










################################################################################################################################################################





