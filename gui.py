from guizero import App, Text, TextBox, PushButton, info
import donnees

def chercher_fichier():
    donnees.image_path = app.select_file(filetypes=[["Images png", "*.png"], ["Images jpeg", "*.jpeg"],["Images jpg", "*.jpg"], ["Images gif", "*.gif"]])

app = App(layout="grid")

app.info("Bienvenue", "Pour commencer :\n 1) Sélectionnez l'image source\n 2) Sélectionnez les dimensions de la surface d'impression")

#indication_image = Text(app, "Image sélectionnée:", grid=[0,0])
chemin_image = TextBox(app, "123", grid=[0,1])


bouton_selection = PushButton(app, command = chercher_fichier, text = "Sélectionner l'image", grid=[0,0])

app.display()

