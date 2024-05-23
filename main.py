import random  # import de la librairie ramdom


# fonction permettant de choisir un mot dans une liste de mots contenu dans un fichier .txt
def choisir_mot():
    with open("mots_pendu.txt", "r") as file:  # ouverture du fichier mots_pendu.txt en mode lecture "r"
        mots = file.readlines()  # creation d'une liste mots contenant l'ensemble des mots du fichier .txt
    return random.choice(mots).strip().lower()  # choix d'un mot aléatoire dans la liste mots, suppression des
                                                # espaces/tabulations/etc (strip) et suppression des accents (lower)


# fonction permettant l'affichage du mot (lettres ou _) durant le jeu avec deux arguments 1. le mot (chaine de
# caractere) 2. les lettres du mots choisies par l'utilisateur (liste)
def affichage_mot(mot, lettres_choisies):
    mot_affiche = ""  # creation d'une chaine de caractere vide pour afficher le mot
    for lettre in mot:  # boucle parcourant chaque lettre du mot
        if lettre in lettres_choisies:  # verification si la lettre du mot est contenue dans la liste lettres_choisies
            mot_affiche += lettre + " "  # si c'est le cas on affiche la lettre
        else:  # si la lettre n'a pas été chosie par l'utilisateur
            mot_affiche += "_ "  # on la remplace par un _
    return mot_affiche.strip()  # on retourne mot_affiche dans son etat actuel (melange de lettres et de _)


# fonction permettant de jouer au jeu du pendu faisant intervenir le choix du mot, son affichage, le nombre
# chances qu'il reste à l'utilisateur et l'affichage de message d'informations
def jeu_du_pendu():
    while True:
        mot = choisir_mot()  # choix d'un mot par appel de la fonction definie precedemment
        lettres_mot = []  # stockage des lettres choisies par l'utilisateur dans une liste
        chances = 6  # definition du nombre de chances

        # message introduction
        print("Bienvenue au jeu du pendu!")
        print("Le mot à deviner comporte", len(mot), "lettres.")

        # boucle verifiant le nombre de chances de l'utilisateur
        while chances > 0:
            print("\nMot à deviner:", affichage_mot(mot, lettres_mot))  # affichage du mot à deviner (lettres et _)
            # par appel de la fonction
            choix_lettre = input("Entrez une lettre : ").lower()  # assignation de la lettre choisie (sans accents) par l'utilisateur à
                                                                  # une variable

            if len(choix_lettre) != 1 or not choix_lettre.isalpha():  # verification s'il s'agit d'une seule lettre et
                                                                      # que la lettre soit alphabetique
                print("Veuillez entrer une seule lettre alphabétique.")
                continue

            if choix_lettre in lettres_mot:  # verification si la lettre n'a pas deja été choisie par l'utilisateur (si
                                             # elle est deja dans la liste)
                print("Vous avez déjà deviné cette lettre.")
                continue

            lettres_mot.append(choix_lettre)  # ajout de la lettre choisie dans la liste des lettres choisies

            if choix_lettre in mot:  # verification si la lettre est dans le mot
                print(f"Bravo! La lettre '{choix_lettre}' fait partie du mot.")
                if all(letter in lettres_mot for letter in mot):  # verification si toutes les lettres ont été trouvées
                    print(f"Félicitations! Vous avez deviné le mot: '{mot}'.")
                    break  # fin du jeu si le mot a été deviné
            else:  # si la lettre ne fait pas partie du mot
                print(f"Désolé, la lettre '{choix_lettre}' ne fait pas partie du mot.")
                chances -= 1  # on retire une chance
                if chances == 1:  # si le nombre de chance vaut 1
                    lettre_indice = random.choice([letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in lettres_mot and mot])  # choix d'une lettre aleatoire
                                                                                                                                             # qui ne fait pas partie du mot
                                                                                                                                             # ni des lettres deja choisies
                    print(f"Indice: La lettre '{lettre_indice}' n'est pas dans le mot.")  # affichage de la
                                                                                          # lettre_indice
                print(f"Il vous reste {chances} chances.")
        else:  # si le nombre de chance est nul
            print(f"Désolé, vous avez épuisé toutes vos chances. Le mot était '{mot}'.")

        choix = input("\nVoulez-vous rejouer ? (oui/non) : ").lower()
        if choix != 'oui':
            break

jeu_du_pendu() # execution de la fonction jeu_du_pendu()