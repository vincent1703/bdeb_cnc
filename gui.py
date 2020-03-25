from guizero import App, Text, TextBox, PushButton, info, Picture
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
    donnees.hauteur_surface = hauteur_boite.value
    hauteur_boite.value = donnees.hauteur_surface

def confirmer_largeur():
    donnees.largeur_surface = largeur_boite.value
    largeur_boite.value = donnees.largeur_surface

app = App(layout="grid", width = 1280, height = 720)

app.info("Bienvenue", "Pour commencer :\n 1) Sélectionnez l'image source\n 2) Sélectionnez les dimensions de la surface d'impression")

chemin_image = TextBox(app, "/home/vincent/bdeb_cnc/images/apercu.png", grid=[1,0], width = 80)

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

bouton_merde = PushButton(app, text = "oh shit tabarnak", grid = [2,4])

app.display()

