from F_1_fonctions import absorbant, recup_file, create_matrix, floydWarshall, clear, list_graphes
from F_1_interface import interface, interface2


def main():
    
    graphes = recup_file() #Récupère les fichiers
    choix = 0
    matrix = [] #Future matrice des plus cours chemins
    clear() #Clear le contenu de la soncole
    while choix != 4:
        print("                      Bienvenue sur l'interface de menu \n\n Veuillez choisir une fonctionnalité: ")
        print("1 - Afficher tous les graphes  \n 2 - Choisir un graphe \n 3 - FloydWarshall \n 4 - Quitter \n")
                
                
        choix = int(input("Votre choix :"))
                
        if (choix == 1):
            list_graphes(graphes) #Liste tous les graphes
        elif (choix == 2):
            nom = input("Nom du graphe : ")
            matrix = create_matrix(graphes, nom) #Créé la matrice des valeurs
            print("Voici la matrice", nom)
            print(matrix)
            interface(matrix) #Affiche la matrice dans l'interface graphique

        elif (choix == 3):
            if(absorbant(matrix)): #Détecte si circuit absorbant
                print("Erreur, circuit absorbant détecté ! \n ANNULATION !!!!")
            else:

                matrix = floydWarshall(matrix)
                if(absorbant(matrix)): #Détecte si circuit absorbant après FlyodWarshall
                    print("Erreur, circuit absorbant détecté ! \n ANNULATION !!!!")
                else:
                    print("Voici la matrice des plus courts chemins !")
                    print(matrix)
                    interface2(matrix)
                

if __name__ == "__main__": #Main
    main() #Lance la fonction main
    quit() #Quitte le programme