#####################
#text user interface#
import donnees
import cnc_v1
import enums
import os
from PIL import Image

#menu principal
#10 options
#appelle la methode de l'option choisie
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
            print('Ce choix est invalide veuillez recommencer\n')

#selection image_path
#propose les differents choix
#prend le nom de l'image et enregistre le path complet
def image_path():
    print("Selection de l'image\n")
    valide = False
    prefix = os.path.dirname(os.path.abspath(__file__))
    ajout_dir = "/images/"
    donnees.parametres[enums.Param.PATH] = prefix + ajout_dir + "mendel.png"
    while(not valide):
        texte = str("liste image:\n" + str(os.listdir(prefix + ajout_dir)) + "\nVotre choix: ")
        temp = validation_texte(texte)
        path = prefix + ajout_dir + temp
        try:
            img = Image.open(path)
            donnees.parametres[enums.Param.PATH] = path
            valide = True
            print(donnees.parametres[enums.Param.PATH], end='  *image choisie*\n')
        except:
            valide = not validation_bool("Image invalide. Voulez-vous recommencer?[Oui/non]")

#ouverture de sauvegarde
#propose les differentes sauvegardes
#envoie le choix pour prendre les infos
def ouvrir_fichier():
    print("Ouverture d'un fichier de sauvegarde\n")
    valide = False
    prefix = os.path.dirname(os.path.abspath(__file__))
    ajout_dir = "/sauvegardes/"
    while(not valide):
        texte = str("liste fichier:\n" + str(os.listdir(prefix + ajout_dir)) + "\nVotre choix: ")
        choix = validation_texte(texte)
        fichier = prefix + ajout_dir + choix
        try:
            test = os.open(fichier,os.O_RDONLY)
            cnc_v1.load_fichier(fichier)
            valide = True
        except:
            valide = not validation_bool("Fichier invalide. Voulez-vous recommencer?[Oui/non]")


#sauvegarde d'un fichier
#demande le nom choisi pour la sauvegarde
#envoie le nom choisi
def save_fichier():
    valide = False
    print("Sauvegarde des parametres actuels\n")
    nom_fichier = validation_texte("Entrez le nom de la sauvegarde: ")
    cnc_v1.save_fichier(nom_fichier)

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
#offre les modes et fait la selection
def mode_impression():
    print("Selection du mode d'impression\n")
    texte = str("choix #0 : contrastes\nchoix #1 : contours(luminosite)\nchoix #2 : contours(couleur)\nchoix #3 : Automatique(contrastes)\nmode")
    donnees.parametres[enums.Param.MODE] = enums.Mode(validation(texte, 0, 3, 1))
    parametre()

#selection du parametre selon mode
#redirige vers le bon parametre
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
#prendre le choix et enregistrer la valeur
def param_0():
    print("Dans le mode contraste, le parametre determine la valeur RGB (0-255) necessaire a une des trois couleurs pour la considerer comme foncee.\nPlus cette valeur est grande, moins il y aura de points a imprimer\nLa valeur doit se situer entre 20 et 200\n")
    donnees.parametres[enums.Param.THRESHOLD] = validation("parametre", 20, 200, 1)
def param_1():
    print("Dans le mode contour de luminosite, le parametre determine la difference de valeur RGB(0-255) necessaire entre 2 pixels voisins pour considerer un changement de luminosite.\nPlus cette valeur est grande par rapport au nombre de pixels, moins il y aura de points a imprimer.\nLa valeur doit se situer entre 2 et 100\n")
    donnees.parametres[enums.Param.DIFFERENCE] = validation("parametre", 2, 100, 1)
def param_2():
    print("Dans le mode contour de couleur, le parametre determine la difference de valeur hue(0-360) necessaire entre 2 pixels voisins pour considerer un changement de couleur.\nPlus cette valeur est grande par rapport au nombre de pixels, moins il y aura de points a imprimer.\nLa valeur doit se trouver entre 2 et 100\n")
    donnees.parametres[enums.Param.COMPARE] = validation("parametre", 2, 100, 1)

#update les informations entrees par l'utilisateur
def actualiser_infos():
    donnees.update_premiere_page()
    donnees.image_loading_array()
    donnees.generate_estimation()

#generer preview
#afficher le temps prevu
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
#sauvegarde les parametres actuels
def impression():
    affichage_actuel()
    if validation_bool("Souhaitez-vous imprimer cette image[Oui/non]?"):
        cnc_v1.save_fichier("last_print")
        controle_machine.impression()

#verification pour quitter
def quitter():
    return not validation_bool("Souhaitez-vous quitter[Oui/non]?")

#message d'accueil
def accueil():
    print("\n#################################################")
    print("### Bienvenue dans la version texte de la CNC ###")
    print("#################################################\n")
    menu_principal()


##################
### VALIDATION ###
##################
#param  param_string :  nom du parametre que l'utilateur selectionne
#param  minimum :       valeur minimale acceptee
#param  maximum :       valeur maximale acceptee
#param  modulo :        valeur par laquelle le choix doit etre divisible
#return valeur:         valeur valide choisie par l'utilisateur
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


#param texte :      indication de ce que l'utilisateur doit entrer
#return entry :     ce que l'utilisateur a confirme comme son choix
def validation_texte(texte):
    valide = False
    while(not valide):
        entry = input(texte)
        valide = validation_bool(str("Confirmez-vous " + entry + "?[Oui/non]"))
    return entry


#param texte :      indication de ce que l'utilisateur doit entrer
#return :           retourne True or False selon le choix de l'utilisateur(default True)
def validation_bool(texte):
    entry = input(texte)
    if "non" in entry.lower():
        return False
    return True


#fin des methodes
######################
accueil()
