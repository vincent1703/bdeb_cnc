import RPi.GPIO as GPIO
import donnees
from time import sleep

DIR = 20
STEP = 21
CW = 1
CCW = 0
SPR = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = 1/500
for i in range(5):
    for i in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    for i in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay*0.7)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay*0.7)

    for i in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay*0.5)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay*0.5)

    for i in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay*0.5)
        GPIO.output(STEP, GPIO.LOW)
        #sleep(delay*0.5)
    for i in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay*1.7)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay*1.7)

    for i in range(step_count*5):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay*0.4)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay*0.4)


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
    print('patate')

# Fait avancer la buse au point suivant (à droite) 
def prochain_point():
    print('patate')

# Fait passer la buse à la ligne suivante (hauteur) et la remet à gauche (début de la ligne)
def prochaine_ligne():
    print('patate')

# Remet la buse dans le coin en haut à gauche
def reset_buse():
    print('patate')

# Valeur en mm qui détermine la distance que doit parcourir la buse pour passer au point suivant et à la ligne suivante
espacement = 1
array = 0
