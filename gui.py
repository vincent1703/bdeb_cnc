from guizero import App, Text, TextBox, PushButton, info, Picture, ButtonGroup, Combo, Window, Picture, Slider
import donnees
import controle_machine 
import cnc_v1
import enums
import tkinter as tk
from PIL import Image
from tkinter import Label, Scale
import os

#va chercher un fichier dans le folder images
#type acceptes: jpeg et jpg
#sauvegarde le chemin complet de l'image
def chercher_fichier():
    donnees.parametres[enums.Param.PATH] = app.select_file(folder=(os.path.dirname(os.path.abspath(__file__)) + "/images/"), filetypes=[["Images jpeg", "*.jpeg"],["Images jpg", "*.jpg"]])
    chemin_image.value = donnees.parametres[enums.Param.PATH]

#selection d'une sauvaegarde et envoie du chemin complet
def ouvrir_save():
    path = app.select_file(folder = os.path.dirname(os.path.abspath(__file__)) + "/sauvegardes/")
    cnc_v1.load_fichier(path)

#selction du nom de la sauvegarde et envoie le nom choisi
def save_file():
    nom = app.question("Sauvegarde", "Entrez le nom de la sauvegarde", initial_value = "save")
    try:
        cnc_v1.save_fichier(nom)
    except:
        info_invalide("Sauvagarde impossible\nChoisir un nom valide")

#affichage miniature de l'image choisie
#return 0 indication aucun probleme
def confirmer_chemin():
    img = Image.open(donnees.parametres[enums.Param.PATH]) 
    global apercu
    apercu = Picture(premiere, image= img, grid=[3,0], width=100, height=100)
    return 0

#prend la valeur entree et la verifie avant de la sauvegarder
#return ok :        0 si execution reussi sinon 1
def confirmer_hauteur():
    ok = 1
    try:
        temp = int(hauteur_boite.value)
        if temp <= donnees.HAUTEUR_MAX and temp >= 10:
            donnees.hauteur_surface = temp
            hauteur_boite.value = donnees.hauteur_surface
            ok = 0
        else:
            hauteur_boite.value = "100"
            message = str("hauteur incompatible\nChoisir entre 10 et " + donnees.hauteur_machine_max)
            info_invalide(message)
    except:
        hauteur_boite.value = "100"
        info_invalide("hauteur invalide")
    return ok

#prend la valeur entree et la verifie avant de la sauvegarder
#return ok :        0 si execution reussie sinon 1
def confirmer_largeur():
    ok = 1
    try:
        temp = int(largeur_boite.value)
        if temp <= donnees.LARGEUR_MAX and temp >= 10:
            donnees.largeur_surface = temp
            largeur_boite.value = donnees.largeur_surface
            ok = 0
        else:
            largeur_boite.value = "100"
            message = str("hauteur incompatible\nChoisir entre 10 et " + donnees.largeur_machine_max)
            info_invalide(message)
    except:
        largeur_boite.value = "100"
        info_invalide("largeur invalide")
    return ok

#prend la valeur choisie parmis la liste et la sauvegarde
#return 0 pour confirmer que bien complete
def confirmer_espacement():
    valeur = 1.0
    if (selection_espacement.value == '1 mm'):
        valeur = 1
    elif (selection_espacement.value == '0,4 mm'):
        valeur = 0.4
    elif (selection_espacement.value == '0,8 mm'):
        valeur = 0.8
    elif (selection_espacement.value == '2 mm'):
        valeur = 2
    elif (selection_espacement.value == '3 mm'):
        valeur = 3
    elif (selection_espacement.value == '5 mm'):
        valeur = 5
    donnees.parametres[enums.Param.ESPACEMENT] = valeur
    return 0

#prend la valeur choisie parmis la liste et la sauvegarde
#return 0 si execution reussie sinon return 1
def confirmer_mode_impression():
    valeur = enums.Mode.CONTRASTE
    if (bouton_mode.value == "Contraste"):
        pass
    elif (bouton_mode.value == "Luminosité"):
        valeur = enums.Mode.LUMINOSITE
    elif (bouton_mode.value == "Couleur"):
        valeur = enums.Mode.COULEUR
    elif (bouton_mode.value == "Auto(contraste)"):
        valeur = enums.Mode.AUTO
    else:
        info_invalide("mode invalide")
        return 1
    donnees.parametres[enums.Param.MODE] = valeur
    return 0

#confirme et actualise les informations
#affiche l'image preview de l'impression
def affichage_preview():
    confirmer_mode_impression()
    print(type(donnees.parametres[enums.Param.MODE]))
    donnees.update_premiere_page()
    donnees.image_loading_array()
    estimation_temps()
    img = donnees.parametres[enums.Param.PREVIEW]
    print(img)
    vider()
    large = int(donnees.parametres[enums.Param.LARGEUR] * donnees.parametres[enums.Param.ESPACEMENT])
    haut = int(donnees.parametres[enums.Param.HAUTEUR] * donnees.parametres[enums.Param.ESPACEMENT])
    global preview
    preview = Picture(deuxieme, image=img, grid=[1,1], width = large, height = haut)

#enleve le preview precedent si existant
def vider():
    try:
        preview.destroy()
    except:
        pass

#validation pour quitter l'application
def fermer():
    quitter = app.yesno("Quitter", "Voulez-vous quitter l'application?")
    if quitter == True:
        app.destroy()

#confirme les elements de la premiere page
#si tout est valide ouvre la seconde page
def confirmation_premiere_page():
    ok = 0
    ok = ok + confirmer_largeur()
    ok = ok + confirmer_hauteur()
    ok = ok + confirmer_espacement()
    ok = ok + confirmer_chemin()
    if ok == 0:
        donnees.update_premiere_page()
        deuxieme_page()

#param message :        nom de l'information invalide
#affiche un probleme a l'utilisateur
def info_invalide(message):
    app.error("information invalide ", message)
    
#affiche la seconde page
def deuxieme_page():
    deuxieme.show(wait = True)

#cache la seconde page
def retour():
    deuxieme.hide()

#fenetre d'accueil avec informations de base
def fenetre_depart():
    global app
    app = App(title='CNC_BdeB', layout="grid", width = 1280, height = 720, visible=False)
    app.info("Bienvenue", "Pour commencer :\n 1) Sélectionnez l'image source\n 2) Sélectionnez les dimensions de la surface d'impression")

#affiche la page d'ajustement
def page_ajustement():
    ajustement.show(wait=True)

#param contraste_value :    valeur du slider de contraste
#ecrit la valeur du slider de contraste dans la boite a cote
def changement_contraste(contraste_value):
    text_contraste.value = contraste_value

#param luminosite_value :   valeur du slider de luminosite
#ecrit la valeur du slider de luminosite dans la boite a cote
def changement_luminosite(luminosite_value):
    text_luminosite.value = luminosite_value

#param couleur_value :      valeur du slider de couleur
#ecrit la valeur du slider de couleur dans la boite a cote
def changement_couleur(couleur_value):
    text_couleur.value = couleur_value

#enregistre les valeurs des sliders d'ajustement
def ajuster():
    donnees.parametres[enums.Param.THRESHOLD] = int(text_contraste.value)
    donnees.parametres[enums.Param.DIFFERENCE] = int(text_luminosite.value)
    donnees.parametres[enums.Param.COMPARE] = int(text_couleur.value)
    ajustement.hide()

#affiche les informations actuelles de l'impression
def informations():
    confirmer_mode_impression()
    donnees.image_loading_array()
    info = ""
    for x in donnees.parametres:
        info = info + x.name + " :" + str(donnees.parametres[x])+ "\n" 
    app.info("informations", info)

#affiche l'estimation de temps de l'impression
def estimation_temps():
    donnees.generate_estimation()
    text_estimation.value = "estimation:\n" + str(donnees.parametres[enums.Param.ESTIMATION])

#pars l'impression et sauvegarde les parametres actuels
def imprimer():
    validation = app.yesno("Impression", "Voulez-vous commencer l'impression?")
    if validation:
        cnc_v1.save_fichier("last_print")
        controle_machine.impression()

fenetre_depart()
premiere = Window(app, layout="grid", title = "Paramètres d'impression", width = 880, height = 720, visible=True)
premiere.when_closed = fermer

#############################
### boutons premiere page ###
#############################
chemin_image = TextBox(premiere, "images/burger.jpeg", grid=[1,0], width = 40)
    
bouton_selection = PushButton(premiere, command = chercher_fichier, text = "Sélectionner l'image", grid=[0,0])
bouton_confirmer = PushButton(premiere, command = confirmer_chemin, text = "Ok", grid=[2,0])

bouton_fermeture = PushButton(premiere, command = fermer, text="fermer", grid=[2,6])

surface_tag = Text(premiere, "Parametres de l'impression", grid=[1,1])
largeur_tag = Text(premiere, "Largeur de la surface (mm) ", grid = [0,2], align="left")
largeur_boite = TextBox(premiere, "100", width = 10, grid = [1,2], align="left")

hauteur_tag = Text(premiere, "Hauteur de la surface(mm)", grid = [0,3], align="left")
hauteur_boite = TextBox(premiere, "100", width = 10, grid = [1,3], align="left")

espacement_tag = Text(premiere, "Espacement (qualité d'impression)", grid = [0,4], align="left")
selection_espacement = Combo(premiere, options=["0,4 mm", "0,8 mm", "1 mm", '2 mm', '3 mm', '5 mm'], selected='1 mm', command = confirmer_espacement,  grid=[1,4], align='left')

bouton_confirmer_premiere_page = PushButton(premiere, text = "Confirmer les informations", command = confirmation_premiere_page, grid = [0,5])

deuxieme = Window(premiere, layout="grid", title = "Lancement de l'impression", width = 900, height = 500)
deuxieme.hide()

#############################
### boutons deuxieme page ###
#############################
texte_mode = Text(deuxieme,  "Mode d'impression : ", size=15, grid=[0,0])
bouton_mode = ButtonGroup(deuxieme, grid=[1,0], options = ['Contraste', 'Luminosité', 'Couleur', 'Auto(contraste)'], selected = 'Contours (luminosité)', horizontal = True)

bouton_preview = PushButton(deuxieme, text='generer preview', command=affichage_preview, grid = [0,1])

bouton_parametre = PushButton(deuxieme, text="parametre d'impression", command=page_ajustement, grid=[2,0])

text_estimation = Text(deuxieme, "estimation temps", size=15, grid=[0,4])

bouton_info = PushButton(deuxieme, text="informations", command=informations, grid=[0,2])

bouton_sauvegarder = PushButton(deuxieme, text = "sauvegarder", command = save_file, grid = [0,3])

bouton_ouvrir_sauvegarde = PushButton(deuxieme, text = "Ouvrir une sauvegarde", command = ouvrir_save, grid = [0,5])

bouton_imprimer = PushButton(deuxieme, text = "imprimer", command = imprimer, grid= [1,3])

bouton_retour = PushButton(deuxieme, text = "retour", command = retour, grid = [2,2])

bouton_fermer = PushButton(deuxieme, text = "fermer", command = fermer, grid = [2,3])

########################
### page ajustements ###
########################
ajustement = Window(app, layout="grid", title="ajustements",width=600,height=400)
ajustement.hide()
ajustement.when_closed = ajuster

titre_contraste = Text(ajustement, "contraste", grid=[0,0], align="bottom")
contraste = Slider(ajustement,command=changement_contraste,end=200,grid=[1,0],start=20,enabled=True,width=400,height=20)
text_contraste = Text(ajustement,contraste.value, grid=[2,0],align="bottom")

titre_luminosite = Text(ajustement, "luminosite", grid=[0,1], align="bottom")
luminosite = Slider(ajustement,command=changement_luminosite,end=100,grid=[1,1],start=2 ,enabled=True,width=400,height=20)
text_luminosite = Text(ajustement,contraste.value, grid=[2,1],align="bottom")

titre_couleur = Text(ajustement, "couleur", grid=[0,2], align="bottom")
couleur = Slider(ajustement,command=changement_couleur,end=80 ,grid=[1,2],start=2 ,enabled=True,width=400,height=20)
text_couleur = Text(ajustement,contraste.value, grid=[2,2],align="bottom")


#debut du programme
app.display()














