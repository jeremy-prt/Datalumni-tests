# Your code goes here
def mystery_number():
    for number in range(1, 1001):
        number = str(number) # conversion en string pour analyser les caractères du nombre

        if '1' not in number and '7' not in number and len(number) >= 2: # vérifier si 7 et 1 non présent + la longueur supérieur/égal à 2 chiffres
            somme_number = sum(int(char) for char in number)  # somme de tous les chiffres dans le nombre

            if somme_number <= 10 and (int(number[0]) + int(number[1])) % 2 == 1: # vérifier si la somme est inférieur ou égale à 10 + les 2 premiers chiffres additionés font un résultat impair
                if int(number[-2]) == 4 and int(number[-1]) == len(number): # vérifier si le 2nd chiffre = 4 + si la longueur du nombre = le dernier chiffre du nombre
                    return number



mystery_number = mystery_number()

print(f'Le nombre mystère est le : {mystery_number}')

# -------Réalisé en 30 minutes-------