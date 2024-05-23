# **Le Jeu du Pendu**

Le jeu du pendu est un classique jeu de devinettes où le joueur tente de deviner un mot en proposant des lettres à tour de rôle. Chaque lettre correctement devinée est révélée dans le mot, tandis que les lettres incorrectes réduisent le nombre de chances du joueur. Le but est de deviner le mot complet avant d'épuiser toutes les chances.

## **Fonctionnement du jeu**

### **Choix du mot :** 
Le jeu sélectionne aléatoirement un mot à partir d'une liste de mots stockée dans un fichier texte.

### **Affichage du mot :** 
Le mot à deviner est affiché sous forme de tirets pour chaque lettre non encore devinée. Les lettres correctement devinées sont révélées dans le mot.

### **Saisie des lettres :** 
Le joueur saisit une lettre à deviner à chaque tour. Le programme vérifie si la lettre est dans le mot et met à jour l'affichage en conséquence.

### **Chances :** 
Le joueur dispose d'un nombre limité de chances pour deviner le mot complet. Chaque lettre incorrecte réduit le nombre de chances disponibles.

### **Indices :** 
En cas de difficulté, le jeu peut fournir un indice en révélant une lettre qui n'est pas dans le mot, à condition qu'il ne reste plus qu'une seule chance.

### **Tours de jeu :**
Si l'utilisateur perd ou gagne, le programme propose à l’utilisateur de recommencer ou de quitter le jeu du pendu.

## **Emplacement des mots**

Les mots utilisés dans le jeu sont stockés dans un fichier texte nommé "mots_pendu.txt". Chaque mot est enregistré sur une ligne distincte du fichier. Pour utiliser un fichier texte différent, il suffit d'ajouter son fichier dans le repository GitHub et d'y faire appel dans la fonction choisir_mot().

## **Principales fonctions**

#### **choisir_mot() :** Cette fonction sélectionne aléatoirement un mot à partir de la liste de mots dans le fichier texte.

#### **affichage_mot(mot, lettres_choisies) :** Cette fonction génère l'affichage du mot à deviner, révélant les lettres correctement devinées.

#### **jeu_du_pendu() :** Cette fonction gère le déroulement complet du jeu, y compris la boucle principale du jeu et la gestion des tours de jeu.
