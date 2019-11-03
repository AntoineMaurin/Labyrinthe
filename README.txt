PRESENTATION DU PROJET

Ce projet est un exercice de formation Python intitulé "Aidez MacGyver à s'échapper".

Il implémente un mini jeu de labyrinthe en 2D où l'on incarne le personnage de MacGyver, 
qui a pour but de ramasser trois objets : une aiguille, un tube en platique et 
une fiole d'ether, pour fabriquer une seringue et endormir le garde.

Ce jeu ne possède qu'un seul niveau. La position des murs, du départ et de l'arrivée
est toujours la même, mais les objets sont répartis aléatoirement dans le jeu, et 
changent de place si vous le relancez.
MacGyver est contrôlé par les flèches directionnelles du clavier, et se déplace de case en
case.
Il récupère un objet simplement en se déplaçant dessus.
Le programme s'arrête lorsque vous rencontrez le garde, après avoir indiqué si vous avez 
gagné ou perdu.
Il y a un compteur d'objets en dessous de labyrinthe pendant le jeu.
La structure du labyrinthe peut être modifiée dans le fichier Maze.txt en respectant cependant
certaines règles:
- Le personnage principal est représenté par la lettre majuscule "M" et il ne peut y en avoir
  qu'un seul.
- Le gardien est représenté par la lettre majuscule "G" et il ne peut y en avoir qu'un seul.
- Les murs sont représentés par des "X" et les espaces libres par des "#".
- Toutes les lignes dans ce fichier doivent faire la même longueur.
Ainsi vous pouvez modifier la structure du labyrinthe comme bon vous semble.

COMMENT L'UTILISER

Pour les utilisateurs de Windows :

Un éxécutable standalone est disponible en suivant ce lien :
https://drive.google.com/drive/folders/1YQSlkp7vkq0sguMf42Z1yAIdX4YJNj-k?usp=sharing

Une fois téléchargé, décompressez l'archive zip, puis rendez vous dans le dossier "main",
et double cliquez sur le fichier "main.exe" pour lancer le jeu.

Pour les autres : 

Ce projet fonctionne avec la version de Python 3.6, et nécessite la librairie Pygame.
Pour installer Python sur votre machine, les détails se trouvent ici : https://fr.wikihow.com/installer-Python

Pour installer la librairie Pygame, les détails se trouvent ici : 
https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/1381_a-la-decouverte-de-pygame/5503_installer-et-importer-pygame/

Enfin, une fois les prérequis installés, pour lancer le projet, rendez vous à la racine du répertoire
du projet, et lancez la commande : python main.py
