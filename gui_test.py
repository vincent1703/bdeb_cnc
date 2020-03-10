from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo

def demarrer_impression(): 
    affichage_dimension_x.value = largeur_image.value

def ajuster_dpi(valeur_curseur):
    affichage_dpi.value = valeur_curseur


app = App(title = "Interface CNC- V1", width = 850, height = 700, layout = "grid")

message_ouverture = Text(app, text="Paramètres d'impression", size=30, font="Arial", color="cyan", grid=[0,0], align = "left")
#affichage_dimension_x = Text(app, text="N/A")
#affichage_dpi = Text(app, text="100")

#update_dimension_x = PushButton(app, command=demarrer_impression, text="Appliquer dimension en x")

#largeur_image = TextBox(app, width=5)

#valeur_dpi = Slider(app, command=ajuster_dpi, start=10, end=200)

#choix_type_impression_texte = Text(app, text="Choix du type d'impression: ", grid=[0,0], align="left")
#choix_type_impression_bouton = Combo(app, options=["Contour", "Monochromatique"], grid=[1,0], align="left") 

#preview_image = Picture(app, image="images/preview_contour.gif")

app.display()
