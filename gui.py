from guizero import App, Text, TextBox, PushButton, info, Picture, ButtonGroup, Combo, Window, Picture, Slider
import donnees
import tkinter as tk
from tkinter import Label, Scale
import os

#va chercher un fichier dans le folder images
#type acceptes: png, jpeg, jpg, gif
def chercher_fichier():
    donnees.image_path = app.select_file(folder=(os.path.dirname(os.path.abspath(__file__)) + "/images/"), filetypes=[["Images png", "*.png"], ["Images jpeg", "*.jpeg"],["Images jpg", "*.jpg"], ["Images gif", "*.gif"]])
    chemin_image.value = donnees.image_path

#affichage miniature de l'image choisie
def confirmer_chemin():
    #global apercu
    #apercu = Picture(premiere, image=donnees.image_path, grid=[3,0], width=150, height=150)
    print ("apercu image " + donnees.image_path)
    return 0

def confirmer_hauteur():
    ok = 1
    try:
        temp = int(hauteur_boite.value)
        if temp <= donnees.hauteur_machine_max and temp >= 10:
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

def confirmer_largeur():
    ok = 1
    try:
        temp = int(largeur_boite.value)
        if temp <= donnees.largeur_machine_max and temp >= 10:
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

def confirmer_espacement():
    if (selection_espacement.value == '1 mm'):
        donnees.espacement = 1
    elif (selection_espacement.value == '0,4 mm'):
        donnees.espacement = 0.4
    elif (selection_espacement.value == '0,7 mm'):
        donnees.espacement = 0.7
    elif (selection_espacement.value == '2 mm'):
        donnees.espacement = 2
    elif (selection_espacement.value == '3 mm'):
        donnees.espacement = 3
    elif (selection_espacement.value == '5 mm'):
        donnees.espacement = 5
    return 0

def confirmer_mode_impression():
    if (bouton_mode.value == "Contraste"):
        donnees.mode = 0
    elif (bouton_mode.value == "Contours (luminosité)"):
        donnees.mode = 1
    elif (bouton_mode.value == "Contours (couleur)"):
        donnees.mode = 2
    else :
        donnees.mode = 1
        return 1
        info_invalide("mode invalide")
    return 0

def affichage_preview():
    confirmer_mode_impression()
    donnees.generate_image_preview()
    print ("mode : " + str(donnees.mode))
    try:
        preview.enabled = False
    except:
        print("",end='')
    #preview = Picture(deuxieme, image=donnees.preview_path, grid=[1,1])

def fermer():
    quitter = app.yesno("Quitter", "Voulez-vous quitter l'application?")
    if quitter == True:
        app.destroy()

def confirmation_premiere_page():
    ok = 0
    ok = ok + confirmer_largeur()
    ok = ok + confirmer_hauteur()
    ok = ok + confirmer_espacement()
    ok = ok + confirmer_chemin()
    if ok == 0:
        donnees.update_premiere_page()
        deuxieme_page()

def info_invalide(message):
    app.error("information invalide", message)
    
def deuxieme_page():
    deuxieme.show(wait = True)

def fenetre_depart():
    global app
    app = App(title='CNC_BdeB', layout="grid", width = 1280, height = 720, visible=False)
    app.info("Bienvenue", "Pour commencer :\n 1) Sélectionnez l'image source\n 2) Sélectionnez les dimensions de la surface d'impression")

def page_ajustement():
    ajustement.show(wait=True)

def changement_contraste(contraste_value):
    text_contraste.value = contraste_value

def changement_luminosite(luminosite_value):
    text_luminosite.value = luminosite_value

def changement_couleur(couleur_value):
    text_couleur.value = couleur_value

def ajuster():
    donnees.threshold = int(text_contraste.value)
    donnees.difference = int(text_luminosite.value)
    donnees.compare = int(text_couleur.value)
    ajustement.hide()

def informations():
    info = "image: " + str(os.path.basename(donnees.image_path)) + "\nlargeur(mm): " + str(donnees.largeur_nouvelle * donnees.espacement) + "\nhauteur(mm): " + str(donnees.hauteur_nouvelle * donnees.espacement) + "\nespacement(mm): " + str(donnees.espacement)
    app.info("informations", info)

fenetre_depart()
premiere = Window(app, layout="grid", title = "Paramètres d'impression", width = 880, height = 720, visible=True)
premiere.when_closed = fermer

#############################
### boutons premiere page ###
#############################
chemin_image = TextBox(premiere, "images/mendel.png", grid=[1,0], width = 40)
    
bouton_selection = PushButton(premiere, command = chercher_fichier, text = "Sélectionner l'image", grid=[0,0])
bouton_confirmer = PushButton(premiere, command = confirmer_chemin, text = "Ok", grid=[2,0])

bouton_fermeture = PushButton(premiere, command = fermer, text="fermer", grid=[2,6])

surface_tag = Text(premiere, "Parametres de l'impression", grid=[1,1])
largeur_tag = Text(premiere, "Largeur de la surface (mm) ", grid = [0,2], align="left")
largeur_boite = TextBox(premiere, "100", width = 10, grid = [1,2], align="left")

hauteur_tag = Text(premiere, "Hauteur de la surface(mm)", grid = [0,3], align="left")
hauteur_boite = TextBox(premiere, "100", width = 10, grid = [1,3], align="left")

espacement_tag = Text(premiere, "Espacement (qualité d'impression)", grid = [0,4], align="left")
selection_espacement = Combo(premiere, options=["0,4 mm", "0,7 mm", "1 mm", '2 mm', '3 mm', '5 mm'], selected='1 mm', command = confirmer_espacement,  grid=[1,4], align='left')

bouton_confirmer_premiere_page = PushButton(premiere, text = "Confirmer les informations", command = confirmation_premiere_page, grid = [0,5])


deuxieme = Window(premiere, layout="grid", title = "Lancement de l'impression", width = 900, height = 500)
deuxieme.hide()

#############################
### boutons deuxieme page ###
#############################
texte_mode = Text(deuxieme,  "Mode d'impression : ", size=15, grid=[0,0])
bouton_mode = ButtonGroup(deuxieme, grid=[1,0], options = ['Contraste', 'Contours (luminosité)', 'Contours (couleur)'], selected = 'Contours (luminosité)', horizontal = True)

bouton_preview = PushButton(deuxieme, text='generer preview', command=affichage_preview, grid = [0,1])

bouton_parametre = PushButton(deuxieme, text="parametre d'impression", command=page_ajustement, grid=[2,0])

bouton_info = PushButton(deuxieme, text="informations", command=informations, grid=[0,2])


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

app.display()














