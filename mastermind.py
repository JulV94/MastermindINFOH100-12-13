#!/usr/bin/python3

# -*-coding:utf-8 -*

# Jeu du Mastermind

def generate_guess(colors):
    """
    Génère une combinaison aléatoire de 4 couleurs prises dans le tuple colors.
    
    Arguments:
    - colors (list) : liste de tuples contenant chacun le symbole puis le nom de la couleur.
        exemple : [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")]
    
    Valeurs de retour:
    str. Retourne un string de 4 lettres qui est la combinaison aléatoire.
    
    Exemples:
    >>> generate_guess([("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    'bjov'
    """
    from random import shuffle

    shuffle(colors)  # On mélange la base de donnée
    guess = ''
    for i in range(4):  # On compose le string
        guess += colors[i][0]

    return guess  # On retourne un string contenant les 4 premières couleurs de la base de données des couleurs mélangée


def valid_colors(comb, colors):
    """
    Vérifie si la combinaison est valide.
    
    Arguments:
    - comb (str) : string d'une combinaison de 4 lettres.
        exemple : 'bjov'
    - colors (list) : liste de tuples contenant chacun le symbole puis le nom de la couleur.
        exemple : [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")]
    
    Valeurs de retour:
    bool. Retourne True si valide sinon False.
    
    Exemples:
    >>> valid_colors("bjov", [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    True
    >>> valid_colors("8k2H", [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    False
    """
    comparaison = [lettre for lettre, nom in
                   colors]  # On retravaille colors car sinon la comparaison avec in est infaisable (liste de tuple -> liste)

    for i in range(len(comb)):  # Pour chaque élément de la combinaison :
        if (not (comb[i] in comparaison)):  # Si l'élément n'est pas dans la liste de couleurs autorisées
            return False  # La combinaison est fausse

    return True  # Si on arrive ici, c'est forcément que rien n'est faux, donc c'est valide


def check_unique(comb):
    """
    Vérifie si une couleur ne se répète pas dans la combinaison.
    
    Arguments:
    - comb (str) : string d'une combinaison de 4 lettres.
        exemple : 'bjov'
    
    Valeurs de retour:
    bool. Retourne True si il n'y a pas de répétition sinon False.
    
    Exemples:
    >>> check_unique("bjov")
    True
    >>> check_unique("bvov"))
    False
    """
    for i in range(len(comb) - 1):  # Pour tout les éléments sauf le dernier
        if (comb[i] in comb[i + 1:]):  # On regarde si il y a le même élément plus loin dans la chaine
            return False  # Alors il y a répétition

    return True  # Si on arrive ici, c'est qu'aucune répétition n'a été trouvée, donc c'est bien vrai


def count_well_placed(guess, comb):
    """
    Compte le nombre de pions bien placés.
    
    Arguments:
    - guess (str) : string d'une combinaison de 4 lettres auquel on compare comb.
        exemple : 'bjov'
    - comb (str) : string d'une combinaison de 4 lettres à comparer à guess.
        exemple : 'bjov'
    
    Valeurs de retour:
    int. Retourne le nombre de pions bien placés compris entre 0 et 4.
    
    Exemples:
    >>> count_well_placed("borv", "bjov")
    2
    """
    count = 0
    for i in range(len(guess)):  # Pour chaque élément
        if (comb[i] == guess[i]):  # Si il est identique à l'élément de même position dans la solution
            count += 1  # On ajoute 1 au compte de bien placés
    return count


def count_colors(guess, comb):
    """
    Compte le nombre de pions de bonne couleur mais mal placés.

    Arguments:
    - guess (str) : string d'une combinaison de 4 lettres auquel on compare comb.
        exemple : 'bjov'
    - comb (str) : string d'une combinaison de 4 lettres à comparer à guess.
        exemple : 'bjov'
    
    Valeurs de retour:
    int. Retourne le nombre de pions de bonne couleur et mal placés compris entre 0 et 4.
    
    Exemples:
    >>> count_colors("borv","bjov")
    1
    """
    count = 0
    for i in range(len(guess)):  # Pour chaque élément
        if (comb[i] in guess):  # Si il est dans la solution
            count += 1  # On augmente le compte de 1
    return count - count_well_placed(guess, comb)  # On renvoie le compte en retirant le nombre d'éléments bien placés


def check_win(guess, comb):
    """
    Vérifie si les 2 combinaisons sont identiques.
    
    Arguments:
    - guess (str) : string d'une combinaison de 4 lettres auquel on compare comb.
        exemple : 'bjov'
    - comb (str) : string d'une combinaison de 4 lettres à comparer à guess.
        exemple : 'bjov'
    
    Valeurs de retour:
    bool. Retourne True si comb est identique à guess sinon False.
    
    Exemples:
    >>> check_win("borv", "borv")
    True
    >>> check_win("borv", "bjov")
    False
    """
    return count_well_placed(guess, comb) == 4  # On teste si les 4 éléments sont bien placés


def to_colors_name(comb, colors):
    """
    Donne l'écriture complète de la combinaison donnée avec un séparateur ', '.
    
    Arguments:
    - comb (str) : string d'une combinaison de 4 lettres.
        exemple : 'bjov'
    - colors (list) : liste de tuples contenant chacun le symbole puis le nom de la couleur.
        exemple : [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")]
    
    Valeurs de retour:
    string. Retourne le nom des 4 couleurs de la combinaison.
    
    Exemples:
    >>> to_colors_name("bjov", [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    "bleu, jaune, orange, vert"
    """
    res = ''
    for i in range(len(comb)):  # Pour chaque élément
        for j in range(len(colors)):  # Pour chaque tuple de colors :
            if comb[i] == colors[j][0]:  # Si le premier élément est le même que celui de la combinaison
                res += colors[j][1] + ", "  # On ajoute le nom de cet élément à la string de résultat + le séparateur
    return res[:len(res) - 2]  # On renvoit le résultat sans le dernier séparateur inutile


def is_4_long(comb):
    """
    Vérifie si la combinaison a bien une longueur de 4.
    
    Arguments:
    - comb (str) : string d'une combinaison de 4 lettres.
        exemple : 'bjov'
    
    Valeurs de retour:
    bool. Retourne True si la combinaison comporte 4 éléments, False sinon.
    
    Exemples:
    >>> is_4_long("bjov")
    True
    >>> is_4_long("bjo")
    Veuillez entrer une combinaison de longueur 4 !
    False
    """
    if len(comb) < 4 or len(comb) > 4:  # Si la combinaison ne vaut pas 4 éléments
        print("Veuillez entrer une combinaison de longueur 4 !")  # On l'annonce et on retourne False
        return False
    return True


def is_valid_letters(comb, colors):
    """
    Vérifie que la combinaison contient bien que des lettres et des lettres valides.
    
    Arguments:
    - comb (str) : string d'une combinaison de 4 lettres.
        exemple : 'bjov'
    
    Valeurs de retour:
    bool. Retourne True si la combinaison comporte des lettres valides, False sinon.
    
    Exemples:
    >>> is_valid_letters("bjov")
    True
    >>> is_valid_letters("bjo2")
    Veuillez entrer une combinaison de couleurs existantes !
    Veuillez n'utiliser que des lettres !
    False
    """
    no_error = True
    if not (valid_colors(comb, colors)):  # Si ce ne sont pas des couleurs de la base de données colors
        print("Veuillez entrer une combinaison de couleurs existantes !")  # On l'annonce et on met False
        no_error = False
    if not (comb.isalpha()):  # Si ce ne sont pas des lettres
        print("Veuillez n'utiliser que des lettres !")  # On l'annonce et on met False
        no_error = False
    return no_error


def is_valid_comb(comb, colors):
    """
    Vérifie si la combinaison est valide.
    
    Arguments:
    - comb (str) : string d'une combinaison de 4 lettres.
        exemple : 'bjov'
    - colors (list) : liste de tuples contenant chacun le symbole puis le nom de la couleur.
        exemple : [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")]
    
    Valeurs de retour:
    bool. True si elle est valide, False sinon.
    
    Exemples:
    >>> is_valid_comb("bjov", [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    True
    >>> is_valid_comb("b6ov", [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    False
    """
    no_error = True
    if not (is_4_long(comb)):  # On teste si la combinaison vaut 4 de long
        no_error = False
    if not (is_valid_letters(comb, colors)):  # On teste si les lettres rentrées sont valides
        no_error = False
    if not (check_unique(comb)):  # Si ce ne sont pas des couleurs différentes
        print("Veuillez entrer une combinaison de couleurs différentes !")  # On l'annonce et on met False
        no_error = False
    return no_error


def comb_input(colors):
    """
    Renvoie la combinaison entrée par l'utilisateur quand elle est valide.
    
    Arguments:
    - colors (list) : liste de tuples contenant chacun le symbole puis le nom de la couleur.
        exemple : [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")]
    
    Valeurs de retour:
    string. Retourne le nom des 4 couleurs de la combinaison.
    
    Exemples:
    >>> comb_input([("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    Devinez la combinaison : rj4l
    Veuillez entrer une combinaison de couleurs existantes !
    Veuillez n'utiliser que des lettres !
    Devinez la combinaison : rjvb
    'rjvb'
    """
    valid = False  # On dit artificiellement que la combinaison est actuellement fausse
    while not (valid):  # Tant que la combinaison est fausse
        comb = input("Devinez la combinaison : ")  # Entrer une combinaison
        comb = comb.lower()  # On convertit le tout en minuscules
        valid = is_valid_comb(comb, colors)  # On teste la validité
    return comb


def feed_back(guess, comb, colors):
    """
    Répond en fonction de la combinaison donnée.
    
    Arguments:
    - guess (str) : string d'une combinaison de 4 lettres auquel on compare comb.
        exemple : 'bjov'
    - comb (str) : string d'une combinaison de 4 lettres.
        exemple : 'bjov'
    - colors (list) : liste de tuples contenant chacun le symbole puis le nom de la couleur.
        exemple : [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")]
    
    Valeurs de retour:
    void. Aucune.
    
    Exemples:
    >>> feed_back("bjov", "bvjr",[("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    Vous avez joué la combinaison : bleu, jaune, orange, rouge
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 1
    Nombre de pions de la bonne couleur mais mal placés :  2
    """
    print("Vous avez joué la combinaison :", to_colors_name(comb, colors))
    print("Réponse :")
    if not (count_well_placed(guess, comb) or count_colors(guess, comb)):  # On annonce si rien n'est bon
        print("Aucun pion bien placé")
    else:  # Ou ce qui est bon
        if count_well_placed(guess, comb):
            print("Nombre de pions de la bonne couleur bien placés :", count_well_placed(guess, comb))
        if count_colors(guess, comb):
            print("Nombre de pions de la bonne couleur mais mal placés : ", count_colors(guess, comb))
    print("")  # Donne de l'air dans la "mise en page"


def game(guess, colors):
    """
    Fait se dérouler le corps d'une partie de mastermind.
    
    Arguments:
    - guess (str) : string d'une combinaison de 4 lettres auquel on compare comb.
        exemple : 'bjov'
    - colors (list) : liste de tuples contenant chacun le symbole puis le nom de la couleur.
        exemple : [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")]
    
    Valeurs de retour:
    bool. True si on a gagné, False si on a perdu.
    
    Exemples:
    >>>game("bjov", "bvjr",[("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    Il vous reste 10 essai(s)
    Devinez la combinaison : rjvb
    Vous avez joué la combinaison : rouge, jaune, vert, bleu
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 2

    Il vous reste 9 essai(s)
    Devinez la combinaison : rjoc
    Vous avez joué la combinaison : rouge, jaune, orange, blanc
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 1

    Il vous reste 8 essai(s)
    Devinez la combinaison : rvoc
    Vous avez joué la combinaison : rouge, vert, orange, blanc
    Réponse :
    Aucun pion bien placé

    Il vous reste 7 essai(s)
    Devinez la combinaison : tjfc
    Vous avez joué la combinaison : violet, jaune, fuchsia, blanc
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 3

    Il vous reste 6 essai(s)
    Devinez la combinaison : tjfb
    Vous avez joué la combinaison : violet, jaune, fuchsia, bleu
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 4
    True
    """
    essais_restant = 10  # On donne 10 essais
    while essais_restant > 0:  # On redonne une chance tant qu'il reste des essais
        print("Il vous reste", essais_restant, "essai(s)")
        comb = comb_input(colors)  # Renvoie une combinaison valide
        feed_back(guess, comb, colors)

        if check_win(guess, comb):  # On vérifie si le joueur a gagné
            return True  # Alors on revoie True
        essais_restant -= 1
    return False  # Si on arrive ici, c'est que les chances sont épuisées sans avoir gagné donc False


def full_game(colors):
    """
    Fait se dérouler une partie entière de mastermind.
    
    Arguments:
    - colors (list) : liste de tuples contenant chacun le symbole puis le nom de la couleur.
        exemple : [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")]
    
    Valeurs de retour:
    void. Aucune.
    
    Exemples:
    >>>full_game([("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")])
    Il vous reste 10 essai(s)
    Devinez la combinaison : rjvb
    Vous avez joué la combinaison : rouge, jaune, vert, bleu
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 2

    Il vous reste 9 essai(s)
    Devinez la combinaison : rjoc
    Vous avez joué la combinaison : rouge, jaune, orange, blanc
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 1

    Il vous reste 8 essai(s)
    Devinez la combinaison : rvoc
    Vous avez joué la combinaison : rouge, vert, orange, blanc
    Réponse :
    Aucun pion bien placé

    Il vous reste 7 essai(s)
    Devinez la combinaison : tjfc
    Vous avez joué la combinaison : violet, jaune, fuchsia, blanc
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 3

    Il vous reste 6 essai(s)
    Devinez la combinaison : tjfb
    Vous avez joué la combinaison : violet, jaune, fuchsia, bleu
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 4
    
    BRAVO !
    """
    guess = generate_guess(colors)  # On génère la solution
    if game(guess, colors):  # Si on a pas gagné, Bravo
        print("BRAVO !")
    else:  # Sinon on donne la solution
        print("Vous avez écoulé vos essais... Dommage !")
        print("La bonne combinaison était :", to_colors_name(guess, colors), "(" + guess.upper() + ")")


def show_rules(colors):
    """
    Affiche les règles du Mastermind.
    
    Arguments:
    - colors (list) : liste de tuples contenant chacun le symbole puis le nom de la couleur.
        exemple : [("b", "bleu"), ("v", "vert"), ("j", "jaune"), ("r", "rouge"), ("o", "orange")]
    
    Valeurs de retour:
    void. Aucune.
    
    Exemples:
    >>>show_rules(colors)
    ****************JEU DU MASTERMIND*****************
    *                                                *
    *                 Règles du jeu :                *
    *                 ---------------                *
    *  Le but du jeu est de trouver une combinaison  *
    *  que l'ordinateur aura choisie aléatoirement.  *
    * Vous disposez de 10 essais pour parvenir à la  *
    *    combinaison. Celle-ci est composée de 4     *
    *   lettres représentant chacune une couleur.    *
    *   A chaque essais, l'ordinateur vous dit le    *
    *  nombre de couleurs correctes et bien placées  *
    * ainsi que le nombre de couleurs correctes mais *
    *                  mal placées.                  *
    *                                                *
    **************************************************
    
    Le code des couleurs est :
    --------------------------
    
    b = bleu
    v = vert
    j = jaune
    r = rouge
    o = orange

    """
    print("""    ****************JEU DU MASTERMIND*****************
    *                                                *
    *                 Règles du jeu :                *
    *                 ---------------                *
    *  Le but du jeu est de trouver une combinaison  *
    *  que l'ordinateur aura choisie aléatoirement.  *
    * Vous disposez de 10 essais pour parvenir à la  *
    *    combinaison. Celle-ci est composée de 4     *
    *   lettres représentant chacune une couleur.    *
    *   A chaque essais, l'ordinateur vous dit le    *
    *  nombre de couleurs correctes et bien placées  *
    * ainsi que le nombre de couleurs correctes mais *
    *                  mal placées.                  *
    *                                                *
    **************************************************

    Le code des couleurs est :
    --------------------------
    """)
    for i in range(len(colors)):
        print("   ", colors[i][0], "=", colors[i][1])
    print("")


def mastermind():
    """
    Fonction principale du jeu du Mastermind.
    Exécute une partie de Mastermind.
    (Fonction impure)
    
    Arguments:
    Aucun.
    
    Valeurs de retour:
    void. Aucune.
    
    Exemples:
    >>> mastermind()
    ****************JEU DU MASTERMIND*****************
    *                                                *
    *                 Règles du jeu :                *
    *                 ---------------                *
    *  Le but du jeu est de trouver une combinaison  *
    *  que l'ordinateur aura choisie aléatoirement.  *
    * Vous disposez de 10 essais pour parvenir à la  *
    *    combinaison. Celle-ci est composée de 4     *
    *   lettres représentant chacune une couleur.    *
    *   A chaque essais, l'ordinateur vous dit le    *
    *  nombre de couleurs correctes et bien placées  *
    * ainsi que le nombre de couleurs correctes mais *
    *                  mal placées.                  *
    *                                                *
    **************************************************
    
    Le code des couleurs est :
    --------------------------
    
    b = bleu
    v = vert
    j = jaune
    r = rouge
    o = orange

    Il vous reste 10 essai(s)
    Devinez la combinaison : rjvb
    Vous avez joué la combinaison : rouge, jaune, vert, bleu
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 2

    Il vous reste 9 essai(s)
    Devinez la combinaison : rjoc
    Vous avez joué la combinaison : rouge, jaune, orange, blanc
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 1

    Il vous reste 8 essai(s)
    Devinez la combinaison : rvoc
    Vous avez joué la combinaison : rouge, vert, orange, blanc
    Réponse :
    Aucun pion bien placé

    Il vous reste 7 essai(s)
    Devinez la combinaison : tjfc
    Vous avez joué la combinaison : violet, jaune, fuchsia, blanc
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 3

    Il vous reste 6 essai(s)
    Devinez la combinaison : tjfb
    Vous avez joué la combinaison : violet, jaune, fuchsia, bleu
    Réponse :
    Nombre de pions de la bonne couleur bien placés : 4

    BRAVO !
    Voulez-vous rejouer ? (o/n) : o
    Il vous reste 10 essai(s)
    Devinez la combinaison : rjoc
    Vous avez joué la combinaison : rouge, jaune, orange, blanc
    Réponse :
    Nombre de pions de la bonne couleur mais mal placés :  3

    Il vous reste 9 essai(s)
    Devinez la combinaison : HGOc
    Veuillez entrer une combinaison de couleurs existantes !
    Devinez la combinaison : s
    Veuillez entrer une combinaison de longueur 4 !
    Veuillez entrer une combinaison de couleurs existantes !
    Devinez la combinaison : 55
    Veuillez entrer une combinaison de longueur 4 !
    Veuillez entrer une combinaison de couleurs existantes !
    Veuillez n'utiliser que des lettres !
    Veuillez entrer une combinaison de couleurs différentes !
    Devinez la combinaison : cccc
    Veuillez entrer une combinaison de couleurs différentes !
    Devinez la combinaison : fvcj
    Vous avez joué la combinaison : fuchsia, vert, blanc, jaune
    Réponse :
    Nombre de pions de la bonne couleur mais mal placés :  2

    Il vous reste 8 essai(s)
    Devinez la combinaison : 
    ...
    """
    continuer = True  # On crée une variable pour détecter si on rejoue
    colors = [("r", "rouge"), ("j", "jaune"), ("v", "vert"), ("b", "bleu"), ("o", "orange"), ("c", "blanc"),
              ("t", "violet"), ("f", "fuchsia")]  # On crée la base de donnée colors
    show_rules(colors)  # On affiche les règles du jeu

    while (continuer):  # On démarre une boucle sur des parties
        full_game(colors)  # On lance une partie

        rejoue = input("Voulez-vous rejouer ? (o/n) : ")  # On demande au joueur si il veut rejouer
        if rejoue.lower() != "o":  # Si il ne répond pas oui
            continuer = False  # On casse la boucle des parties
            print("Au revoir !")


if __name__ == "__main__":  # Si le fichier n'est pas un module, qu'il est appelé seul (en main)
    mastermind()  # Lancer le jeu
