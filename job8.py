L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]  # déclaration des listes pour les testes
# L = [5, 3, 8, 1]
# L = [1, 2, 3, 4]


def my_sort(L):  # définition de la fonction my_sort qui a un paramètre de type "Liste"
    taille = 0  # définition d'une variable pour la liste
    coup = 0  # définition d'une variable pour connaitre le nombre coup
    for loop in L:  # boucle pour connaitre la taille d'une chaine de caracteres
        taille = taille + 1

    for i in range(taille):  # boucle listant chaque élément de la liste
        for j in range(
            i + 1, taille
        ):  # boucle qui permet de vérifier chaque éléments (on ne test qu'a partir du 2eme élément)
            if (
                L[i] > L[j]
            ):  # si n > n+1, sinon on passe à la valeur suivant jusqu'a la derniere valeur
                L[i], L[j] = L[j], L[i]  # on permutte les 2 valeurs
                coup += 1  # on ajoute 1 au compteur de coup
    print(f"Nombre total de coups nécessaires pour trier la liste {coup}")
    print(f"liste triée : {L}")


my_sort(L)  # Appel de la fonction avec le parametre L
