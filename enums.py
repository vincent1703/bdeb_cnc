from enum import Enum
class Param (Enum):
    PATH = 0
    LARGEUR = 1
    HAUTEUR = 2
    ESPACEMENT = 3
    MODE = 4
    THRESHOLD = 5
    DIFFERENCE = 6
    COMPARE = 7
    ESTIMATION = 8

class Mode (Enum):
    CONTRASTE = 0
    LUMINOSITE = 1
    COULEUR = 2
