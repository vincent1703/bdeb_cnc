from guizero import App, Text, TextBox, PushButton, info, Picture, ButtonGroup, Combo, Window, Picture
import donnees
import tkinter as tk
from tkinter import Label

def chercher_fichier():
    donnees.image_path = app.select_file(filetypes=[["Images png", "*.png"], ["Images jpeg", "*.jpeg"],["Images jpg", "*.jpg"], ["Images gif", "*.gif"]])
    chemin_image.value = donnees.image_path

def confirmer_chemin():
    #donnees.image_path = chemin_image.value
    print(donnees.image_path)
    #global apercu
    #apercu = Picture(premiere, image=donnees.image_path, grid=[3,0], width=150, height=150)
    #apercu.resize(150,150)

def confirmer_hauteur():
    donnees.hauteur_surface = int(hauteur_boite.value)
    hauteur_boite.value = donnees.hauteur_surface

def confirmer_largeur():
    donnees.largeur_surface = int(largeur_boite.value)
    largeur_boite.value = donnees.largeur_surface

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

def confirmer_mode_impression():
    if (bouton_mode.value == "Contraste"):
        donnees.mode = 0
    elif (bouton_mode.value == "Contours (luminosité)"):
        donnees.mode = 1
    elif (bouton_mode.value == "Contours (couleur)"):
        donnees.mode = 2
    else :
        donnees.mode = 1

def affichage_preview():
    #donnees.update_premiere_page()
    confirmer_mode_impression()
    donnees.generate_image_preview()
    print (donnees.mode , end=" mode\n")
    #preview = Picture(deuxieme, image=donnees.preview_path, grid=[1,1])

def fermer():
    app.destroy()

def confirmation_premiere_page():
    confirmer_largeur()
    confirmer_hauteur()
    confirmer_espacement()
    confirmer_chemin()
    donnees.update_premiere_page()
    deuxieme_page()
    
def deuxieme_page():
    deuxieme.show(wait = True)

def fenetre_depart():
    global app
    app = App(title='CNC_BdeB', layout="grid", width = 1280, height = 720, visible=False)
    app.info("Bienvenue", "Pour commencer :\n 1) Sélectionnez l'image source\n 2) Sélectionnez les dimensions de la surface d'impression")

def boutons_premiere_page():
    chemin_image = TextBox(premiere, "images/mendel.png", grid=[1,0], width = 40)
    
    bouton_selection = PushButton(premiere, command = chercher_fichier, text = "Sélectionner l'image", grid=[0,0])
    bouton_confirmer = PushButton(premiere, command = confirmer_chemin, text = "Ok", grid=[2,0])

    bouton_fermeture = PushButton(premiere, command = fermer, text="fermer", grid=[2,6])

    surface_tag = Text(premiere, "Parametres de l'impression", grid=[1,1])
    largeur_tag = Text(premiere, "Largeur de la surface (mm) ", grid = [0,2], align="left")
    largeur_boite = TextBox(premiere, "100", width = 10, grid = [1,2], align="left")
    #bouton_confirmer_largeur = PushButton(premiere, text = "Ok", command = confirmer_largeur, grid = [1,2])

    hauteur_tag = Text(premiere, "Hauteur de la surface(mm)", grid = [0,3], align="left")
    hauteur_boite = TextBox(premiere, "100", width = 10, grid = [1,3], align="left")
    #bouton_confirmer_hauteur = PushButton(premiere, text = "Ok", command = confirmer_hauteur, grid = [1,3])

    espacement_tag = Text(premiere, "Espacement (qualité d'impression)", grid = [0,4], align="left")
    selection_espacement = Combo(premiere, options=["0,4 mm", "0,7 mm", "1 mm", '2 mm', '3 mm', '5 mm'], selected='1 mm', command = confirmer_espacement,  grid=[1,4], align='left')
    #bouton_confirmer_hauteur = PushButton(premiere, text = "Ok", command = confirmer_espacement, grid = [1,4])
    bouton_confirmer_premiere_page = PushButton(premiere, text = "Confirmer les informations", command = confirmation_premiere_page, grid = [0,5])

def boutons_deuxieme_page():
    texte_mode = Text(deuxieme,  "Mode d'impression : ", size=15, grid=[0,0])
    bouton_mode = ButtonGroup(deuxieme, grid=[1,0], options = ['Contraste', 'Contours (luminosité)', 'Contours (couleur)'], selected = 'Contours (luminosité)', horizontal = True)
    bouton_preview = PushButton(deuxieme, text='generer preview', command=affichage_preview, grid = [0,1])


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
#bouton_confirmer_largeur = PushButton(premiere, text = "Ok", command = confirmer_largeur, grid = [1,2])

hauteur_tag = Text(premiere, "Hauteur de la surface(mm)", grid = [0,3], align="left")
hauteur_boite = TextBox(premiere, "100", width = 10, grid = [1,3], align="left")
#bouton_confirmer_hauteur = PushButton(premiere, text = "Ok", command = confirmer_hauteur, grid = [1,3])

espacement_tag = Text(premiere, "Espacement (qualité d'impression)", grid = [0,4], align="left")
selection_espacement = Combo(premiere, options=["0,4 mm", "0,7 mm", "1 mm", '2 mm', '3 mm', '5 mm'], selected='1 mm', command = confirmer_espacement,  grid=[1,4], align='left')
#bouton_confirmer_hauteur = PushButton(premiere, text = "Ok", command = confirmer_espacement, grid = [1,4])
bouton_confirmer_premiere_page = PushButton(premiere, text = "Confirmer les informations", command = confirmation_premiere_page, grid = [0,5])


deuxieme = Window(premiere, layout="grid", title = "Lancement de l'impression", width = 900, height = 500)
deuxieme.hide()

#############################
### boutons deuxieme page ###
#############################
texte_mode = Text(deuxieme,  "Mode d'impression : ", size=15, grid=[0,0])
bouton_mode = ButtonGroup(deuxieme, grid=[1,0], options = ['Contraste', 'Contours (luminosité)', 'Contours (couleur)'], selected = 'Contours (luminosité)', horizontal = True)
bouton_preview = PushButton(deuxieme, text='generer preview', command=affichage_preview, grid = [0,1])


app.display()














