#####################
#text user interface#
import donnees
import cnc_v1
import enums
import os
from PIL import Image

#menu principal
#7 options
def menu_principal():
    continuer = True
    while(continuer):
        choix = -1
        #message de choix d'option
        print("\n\tMENU PRINCIPAL")
        print("choisissez une option parmis les suivantes")
        print("------------------------------------------")
        print("#0 Choix de l'image")
        print("#1 Selection des dimensions")
        print("#2 Selection de l'espacement")
        print("#3 Selection du mode d'impression")
        print("#4 Ajustement du parametre d'impression")
        print("#5 Generation de l'image preview")
        print("#6 Affichage des choix actuels")
        print("#7 Commencer l'impression")
        print("#8 Utiliser une sauvegarde existante")
        print("#9 Enregistrer une sauvegarde")
        print("#10 Quitter")
        print("------------------------------------------")
        try:
            choix = int(input("Votre choix: "))
            print("")
        except:
            choix = -1
        #switch n'existe pas en python
        if choix == 0:
            image_path()
        elif choix == 1:
            largeur_longueur()
        elif choix == 2:
            espacement()
        elif choix == 3:
            mode_impression()
        elif choix == 4:
            parametre()
        elif choix == 5:
            generer_preview()
        elif choix == 6:
            affichage_actuel()
        elif choix == 7:
            impression()
        elif choix == 8:
            ouvrir_fichier()
        elif choix == 9:
            save_fichier()
        elif choix == 10:
            continuer = quitter()
        else:
            print('Ce choix est invalide veuillez recommencer')

#selection image_path
def image_path():
    print("Selection de l'image\n")
    valide = False
    prefix = os.path.dirname(os.path.abspath(__file__))
    ajout_dir = "/images/"
    donnees.parametres[enums.Param.PATH] = prefix + "/images/mendel.png"
    while(not valide):
        temp = input("nom de l'image et type: ")
        temp = prefix + ajout_dir + temp
        try:
            img = Image.open(temp)
            donnees.parametres[enums.Param.PATH] = temp
            valide = True
            print(donnees.parametres[enums.Param.PATH], end='  *image choisie*\n')
        except:
            print(temp)
            print("Choix d'image invalide")
            entry = input("Voulez-vous recommencer[Oui/non]? ")
            if "non" in entry.lower():
                valide = True


#ouverture de sauvegarde
def ouvrir_fichier():
    print("Ouverture d'un fichier de sauvegarde\n")
    valide = False
    prefix = os.path.dirname(os.path.abspath(__file__))
    ajout_dir = "/sauvegardes/"
    while(not valide):
        print("liste de fichiers disponibles")
        print(os.listdir(prefix + ajout_dir))
        choix = input("\nvotre choix: ")
        temp = prefix + ajout_dir + choix
        try:
            test = os.open(temp,os.O_RDONLY)
            print("ouverture reussi")
            cnc_v1.load_fichier(temp)
            valide = True
        except:
            print("Ce choix de fichier est invalide")
            entry = input("Voulez-vous recommencer[Oui/non]? ")
            if "non" in entry.lower():
                valide = True


#sauvegarde d'un fichier
def save_fichier():
    print("Sauvegarde des parametres actuels\n")
    cnc_v1.save_fichier("automatique")
    print("Sauvegarde effectuee avec succes")



#selection largeur et longueur
def largeur_longueur():
    print("Selection de la largeur et de la longueur\n")
    donnees.largeur_surface = validation("largeur(mm)", 1, donnees.LARGEUR_MAX, 1)
    donnees.hauteur_surface = validation("hauteur(mm)", 1, donnees.HAUTEUR_MAX, 1)

#selection espacement
def espacement():
    print("Selection de l'espacement\n")
    donnees.parametres[enums.Param.ESPACEMENT] = validation("espacement(mm)", 0.2, 5.0, 0.2)


#selection mode d'impression
def mode_impression():
    print("Selection du mode d'impression\n")
    print("choix #0 : contrastes")
    print("choix #1 : contours (lumiosite)")
    print("choix #2 : contours (couleur)")
    donnees.parametres[enums.Param.MODE] = enums.Mode(validation("mode", 0, 3, 1))
    print("")
    parametre()

#selection du parametre selon mode
def parametre():
    print("Ajustement du parametre d'impression\n")
    if donnees.parametres[enums.Param.MODE] == enums.Mode.CONTRASTE:
        param_0()
    elif donnees.parametres[enums.Param.MODE] == enums.Mode.LUMINOSITE:
        param_1()
    elif donnees.parametres[enums.Param.MODE] == enums.Mode.COULEUR:
        param_2()
    elif donnees.parametres[enums.Param.MODE] == enums.Mode.AUTO:
        param_0()
    else:
        print("Probleme de selection du mode")

#explications pour l'ajustement des parametres
def param_0():
    print("Dans le mode contraste, le parametre determine la valeur RGB (0-255) necessaire a une des trois couleurs pour la considerer comme foncee.\nPlus cette valeur est grande, moins il y aura de points a imprimer\nLa valeur doit se situer entre 20 et 200\n")
    donnees.parametres[enums.Param.THRESHOLD] = validation("parametre", 20, 200, 1)
def param_1():
    print("Dans le mode contour de luminosite, le parametre determine la difference de valeur RGB(0-255) necessaire entre 2 pixels voisins pour considerer un changement de luminosite.\nPlus cette valeur est grande par rapport au nombre de pixels, moins il y aura de points a imprimer.\nLa valeur doit se situer entre 2 et 100\n")
    donnees.parametres[enums.Param.DIFFERENCE] = validation("parametre", 2, 100, 1)
def param_2():
    print("Dans le mode contour de couleur, le parametre determine la difference de valeur hue(0-360) necessaire entre 2 pixels voisins pour considerer un changement de couleur.\nPlus cette valeur est grande par rapport au nombre de pixels, moins il y aura de points a imprimer.\nLa valeur doit se trouver entre 2 et 100\n")
    donnees.parametres[enums.Param.COMPARE] = validation("parametre", 2, 100, 1)

def actualiser_infos():
    donnees.update_premiere_page()
    donnees.image_loading_array()
    donnees.generate_estimation()

#generer preview
def generer_preview():
    actualiser_infos()
    print("Une nouvelle image preview a ete generee\n")
    print("temps d'impression prevu " + donnees.parametres[enums.Param.ESTIMATION],end='\n\n')

#affichage des choix actuels
def affichage_actuel():
    actualiser_infos()
    for x in donnees.parametres:
        print(x.name + ": " + str(donnees.parametres[x]))


#debuter l'impression avec verification
def impression():
    print ("Voici les informations de l'impression: ")
    affichage_actuel()
    reponse = input("Souhaitez-vous imprimer cette image[Oui/non]?")
    if "non" in reponse.lower():
        print("impression annulee")
    else:
        print("debut de l'impression")

#verification pour quitter
def quitter():
    continuer = False
    entry = input("Souhaitez-vous quitter[Oui/non]?")
    if "non" in entry.lower():
        continuer = True
    return continuer
#message d'accueil
def accueil():
    print("\n#################################################")
    print("### Bienvenue dans la version texte de la CNC ###")
    print("#################################################\n")
    menu_principal()


##################
### VALIDATION ###
##################
def validation(param_string, minimum,  maximum, modulo):
    valide = False
    while(not valide):
        try:
            valeur = float(input(param_string + ": "))
            if valeur >= minimum:
                if valeur <= maximum:
                    if (10*valeur) % (10*modulo) == 0:
                        valide = True
                    else:
                        print("Veuillez entrer un chiffre divisible par " + str(modulo))
                else:
                    print("Veuillez entrer un chiffre plus petit ou egal a " + str(maximum))
            else:
                print("Veuillez entrer un chiffre plus grand ou egal a " + str(minimum))
        except:
            print("Invalide veuillez entrer un chiffre entre " + str(minimum) + " et " + str(maximum))
    return valeur

#fin des methodes
######################
accueil()
#fin du programme
######################
