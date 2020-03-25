from guizero import App, Text, TextBox, PushButton, info, Picture, ButtonGroup, Combo
import donnees


def chercher_fichier():
    donnees.image_path = app.select_file(filetypes=[["Images png", "*.png"], ["Images jpeg", "*.jpeg"],["Images jpg", "*.jpg"], ["Images gif", "*.gif"]])
    chemin_image.value = donnees.image_path

def confirmer_chemin():
    donnees.image_path = chemin_image.value
    global apercu
    apercu = Picture(app, image=donnees.image_path, grid=[3,0])
    apercu.resize(150,150)

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

def affichage_preview():
    donnees.update_premiere_page()
    donnees.generate_image_preview()
    preview = Picture(app, image=donnees.preview_path, grid=[2,5])

app = App(layout="grid", width = 1280, height = 720)

app.info("Bienvenue", "Pour commencer :\n 1) Sélectionnez l'image source\n 2) Sélectionnez les dimensions de la surface d'impression")

chemin_image = TextBox(app, "images/burger.jpeg", grid=[1,0], width = 80)

bouton_selection = PushButton(app, command = chercher_fichier, text = "Sélectionner l'image", grid=[0,0])
bouton_confirmer = PushButton(app, command = confirmer_chemin, text = "Ok", grid=[2,0])

surface_tag = Text(app, "Parametres de l'impression", grid=[1,1])
largeur_tag = Text(app, "Largeur de la surface (mm) ", grid = [0,2], align="left")
largeur_boite = TextBox(app, "100", width = 10, grid = [1,2], align="left")
bouton_confirmer_largeur = PushButton(app, text = "Ok", command = confirmer_largeur, grid = [1,2])

hauteur_tag = Text(app, "Hauteur de la surface(mm)", grid = [0,3], align="left")
hauteur_boite = TextBox(app, "100", width = 10, grid = [1,3], align="left")
bouton_confirmer_hauteur = PushButton(app, text = "Ok", command = confirmer_hauteur, grid = [1,3])
confirmer_chemin()

espacement_tag = Text(app, "Espacement (qualité d'impression)", grid = [0,4], align="left")
selection_espacement = Combo(app, options=["0,4 mm", "0,7 mm", "1 mm", '2 mm', '3 mm', '5 mm'], selected='1 mm', command = confirmer_espacement,  grid=[1,4], align='left')
bouton_confirmer_hauteur = PushButton(app, text = "Ok", command = confirmer_espacement, grid = [1,4])

bouton_preview = PushButton(app, text='generer preview', command=affichage_preview, grid = [1,5])

app.display()
















