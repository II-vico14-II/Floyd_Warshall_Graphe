import glob #Permet de détecter des fichiers particuliers (ici ce sera des fichiers en .txt)
import numpy as np #Permet de faire les calcula mathématiques et ainsi importer le nombre "Infini" et 
from os import system, name #Permet d'interragir avec le système d'exploitation, seulement la console/powershell dans ce programme

#Fonctions

def recup_file(): #Récupère tous les graphes en .txt

    filenames = glob.glob('./examples_graphs/*.txt') #Détecte les fichiers en .txt

    graphes = {} #Dictionnaire qui aura pour clefs le nom des graphes et leur valeur le contenu du fichier en .txt

    for file in filenames:
        numbers = []
        with open(file, 'r') as f:
            for line in f:
                numberl  = [int(line) for line in line.split()] #Permet de séparer chaque ligne et chaque valeur par ligne dans les cases
                
                numbers.append(numberl) 
            graphes[str(file[18:]).replace(".txt", "")] = numbers #Ajoute une clef avec sa valeur

    '''
    print("Voici la liste des fichiers:")
    for key in graphes:
        print(key)

    print(graphes)
    '''

    return graphes


def create_matrix(graphes, name='exemple'):  #Créé la matrice des valeurs
    builder = graphes[name] #Récupère la matrice du dictionnaire 'graphes' grâce à son nom

    sommets, arcs = builder[0][0], builder[1][0] #Récupère le nombre de sommets et le nombre d'arcs

    matrix = np.full((sommets, sommets), np.Inf)

    builder = builder[2:] #Supprime les deux premières cases de la liste builder car inutiles

    for i in builder: #On construit la matrice
        matrix[i[0]][i[1]] = i[2]

    #print(matrix)

    return matrix


def floydWarshall(M): #Floyd Warshamll

    n = np.shape(M)[0]
  
    for i in range(0,n):
        M[i][i] = 0
    

    print("Valeurs intermédiaires")

    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n): #Affiche les valeurs intermédiaires
                print(f"M[{i}][{j}] = {M[i][j]}")
                print(f"M[{i}][{k}] = {M[i][k]}")
                print(f"M[{k}][{j}] = {M[k][j]}")

                if (M[i][j] > M[i][k] + M[k][j]):
                    M[i][j] = M[i][k] + M[k][j]
                print(M)

    return M

def list_graphes(graphes): #Affiche la liste des graphes disponibles
    print("Voici la liste des fichiers:")
    for key in graphes:
        print(f"{key} : {graphes[key]}")


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def absorbant(M): #Détecte si circuit absorbant
    #calcul des degrés
    degree = 0
    for i in range(np.shape(M)[0]):
        if M[i][i] < 0:
            return True

    return False


