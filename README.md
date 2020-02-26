# bdeb_cnc
26 février 2020

Document d’analyse : CNC 2020



*   Membres de l'équipe : François Tourigny, Olivier Godfroy et Vincent Moreau
*   Description du projet 
    *   Idée : Fabriquer et programmer une machine CNC qui pourra des images provenant de dessins monochromes numérisés sur des surfaces variés.
    *   Utilité : Cette machine, avec le programme associé, permettra à l’équipe de robotique de fabriquer avec une solution facile et clef en main des surfaces imprimées, notamment pour le kiosque, la fabrication de pièces décoratives ou fonctionnelles pour la vidéo, les installations du local, etc. Le but est vraiment d’à partir d’une machine simple, de la rendre utile et facile à employer en ayant une approche permettant aux utilisateurs d’importer des sketch ou images monochromes et de les convertir en impressions rapidement, aisément, en démarrant la machine en quelques étapes. La machine permettra de voir la progression et d’avoir un temps de complétion de la tâche estimé pour permettre de bien planifier la réalisation des projets.
    *   Innovation: Faire une machine robotisée simple avec 2 stepper motor est simple. Faire un programme qui le commande l’est aussi. Par contre, l’intégration des deux systèmes pour permettre une utilisation optimale et facile pour l’utilisateur de la machine est là où tout le coeur de l’innovation réside. Notre logiciel va être adaptable aux changements physique de fonctionnalités sur la machine, aux différents matériaux, et permettra à l’utilisateur d’utiliser la machine CNC à son plein potentiel en ajustant des paramètres pour optimiser la machine au travail demandé.
    *   Utilisations et destinataire : Comme précisé précédemment, cette machine accompagnée de son contrôleur permettra aux membres de l’équipe de robotique du Collège de Bois-de-Boulogne de fabriquer rapidement et facilement des pièces décoratives et fonctionnelles de qualité, variés et personnalisées.
    *   Lien avec les autres matières : Il y a des notions de physique mécanique, avec les systèmes de déplacement et de mouvement (force, masse, inertie, travail) et d’électricité (courant, tension, magnétisme). De plus, il faudra utiliser des notions de mathématiques, notamment discrètes, pour créer une représentation virtuelle des positions de l’image où l’impression aura lieu et pour calculer les trajectoires de la buse, tout comme le temps estimé, le tout avec la programmation contrôlant la machine pour qu’elle exécute les tâches calculées.
    *   Technologies à utiliser : Il faudra programmer, en Python, le logiciel qui détermine quelles actions doit faire la machine pour exécuter la tâche d’impression ou de gravure. Ce logiciel devra aussi pouvoir importer l’image numérisée à l’aide d’une interface graphique montrant à l’utilisateur ce qui se passe. Il y aura aussi saisie de paramètres par l’utilisateur, comme la résolution et la taille de la surface à graver. Le logiciel calculera et affichera le temps d’impression et la progression. Le code pourra être partagé et travaillé en mode collaboratif avec Git. L’ensemble du code sera exécuté et l’interface sera affichée sur le Raspberry Pi. Pour contrôler les moteurs, un contrôleur #8825 adaptant le 12V aux contrôles du Pi à travers l’interface de contrôle GPIO. Pour utiliser cette interface, la librairie GPIO sera utilisée en Python sur le code du Raspberry Pi. La librairie Pillow devrait être utilisée pour effectuer le traitement de l’image pour développer la matrice de booléen pour impression.
*   Classes du programme : 
    *   Main ou équivalent en Python
    *   Classe pour l’affichage graphique
    *   Classe pour les paramètres définis par l’utilisateur et pour le stockage des données de l’image
    *   Classe pour le contrôle des moteurs pas-à-pas (import librairie GPIO)
    *   Classe pour l’exécution de l’impression selon les données (type de modèle) et retournant l’affichage
*   Tutoriels et liens utiles : 
    *   [https://projectiot123.com/2019/01/29/raspberry-pi-gpio-pins-with-stepper-motor-using-l298-motor-controller/](https://projectiot123.com/2019/01/29/raspberry-pi-gpio-pins-with-stepper-motor-using-l298-motor-controller/)
    *   [https://www.rototron.info/raspberry-pi-stepper-motor-tutorial/](https://www.rototron.info/raspberry-pi-stepper-motor-tutorial/)
    *   [https://www.youtube.com/watch?v=LUbhPKBL_IU](https://www.youtube.com/watch?v=LUbhPKBL_IU)
    *   [https://gpiozero.readthedocs.io/en/stable/](https://gpiozero.readthedocs.io/en/stable/)
    *   [https://pinout.xyz/#](https://pinout.xyz/#) 
    *   

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/real-doc0.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/real-doc0.png "image_tooltip")

*   Planification préliminaire:
    *   1 – 15 février : Commande et réception des pièces et matériaux nécessaires à la fabrication de la CNC. (cela inclut les composantes électroniques, contrôleurs, etc.)
    *   16 – 28 février : Construction de la machine et début des tests des contrôleurs de moteurs Arduino.
    *   28 février – 6 mars : Début de la création du programme (focus sur le contrôle des moteurs à travers Raspberry Pi GPIO et contrôleurs 8825)
    *   7 mars – 31 mars : Conception, réalisation et test du programme de gestion des images et de l’impression. Contrôle de la machine selon les paramètres.
    *   1<sup>er</sup> – 17 avril : Finalisation du programme avec interface utilisateur, ajustements et précision de la machine avec tests tactiques.
    *   18 – 30 avril : Ajustements en fonction de la buse, du type d’impression et finalisation du programme pour usage clef en main par l’utilisateur.
*   Division des tâches 
    *   Olivier : Fabrication des pièces de la CNC, impression 3D, assemblage et focus sur le contrôle des moteurs avec le #8825
    *   Vincent : Librairie GPIO, interface graphique python, traitement d’image
    *   François : Librairie Pillow, interface graphique, traitement d’image
