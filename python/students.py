# Your code goes here


import csv
import json

def read_csv(filename):
    with open(filename, 'r', encoding='latin-1') as csvfile: #latin car 
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    return rows

def number_category():
    users_per_degree = {}
    for row in rows:
        degree = row["Diplome"]
        user_category = row["School admin"]

        # vérifier si le diplôme est déjà dans le dictionnaire
        if degree not in users_per_degree:
            users_per_degree[degree] = {}

        # compte chaque diplôme pour chaque catégorie de personne
        if user_category not in users_per_degree[degree]:
            users_per_degree[degree][user_category] = 1
        else:
            users_per_degree[degree][user_category] += 1

    for degree, categories in users_per_degree.items():
        print(f'\n- {degree}')
        for category, count in categories.items():
            print(f' -> {category} : {count}')
    return users_per_degree



if __name__ == "__main__":
    
    filename = 'students.csv'
    
    # Ecrivez une fonction permettant de récupérer toutes les lignes
    # du fichier CSV dans une list() `rows`
    rows = read_csv(filename)
    print(f'\nLe fichier brut contient {len(rows)} lignes')

    # Les étudiants ont chacun un diplôme qui leur est attribué
    # La variable `degrees` contient la liste des diplômes
    degrees = set(row["Diplome"] for row in rows)
    print(f'\nLe fichier contient {len(degrees)} diplômes uniques')
    
    
    # Donnez, dans un dict, pour chaque diplôme le nombre d'étudiant
    # par catégorie d'utilisateur (student, alumni, ...)
    #
    #   - Master Un -> Student : 123
    #               -> Alumni : 456
    #               -> ...
    #   - Master Deux -> ...
    #
    users_per_degree = number_category()
    
    # Enregistrez le dictionnaire dans un nouveau fichier `degree_count.json`
    # TODO
    with open('degree_count.json', 'w') as json_file:
        json.dump(users_per_degree, json_file, indent=2)
    print(f'\nFichier `degree_count.json` enregistré !')
    
    
    #----------Realisé en 1h----------