# Test Javascript
## Règles du jeu
- Vous utiliserez le projet pré-générer dans `javascript/app`
- Vous utiliserez uniquement du **Javascript/Typescript vanilla** et **Vue.js** (version 3)
- **Aucune dépendance** n'est autorisée (uniquement les API Javascript standard)
- Vous considérerez que l'utilisateur utilise un navigateur moderne et à jour
- Pas de prérequis pour le rendu esthétique, vous utiliserez votre framework CSS préféré

## Livrable attendu

Vous devez créer une app affichant une liste d'utilisateurs. Les informations proviennent d'une app fictive et sont rendues disponibles à travers une API REST.

L'application contient les fonctionnalités suivantes :
- Les données relatives aux utilisateurs sont récupérables [via une API REST](https://randomuser.me/)
- L'app est divisée en deux composants : la **liste des utilisateurs** et **le profil détaillé**
- Liste des utilisateurs :
    - La liste est composée de 10 utilisateurs
    - Les utilisateurs sont listés par leur `Prénom NOM`
    - Lorsqu'on clique sur un utilisateur, sont profil détaillé s'affiche
    - L'utilisateur actif (sélectionné) apparaît en surbrillance dans la liste
    - Un bouton `Ajouter un utilisateur` est présent au bas de la liste et ajoute un nouvel utilisateur dans la liste (les données de cet utilisateur sont récupérées [via l'API REST](https://randomuser.me/))
- Profil utilisateur détaillé
    - Si aucun utilisateur n'est sélectionné, un message nous invite à cliquer sur le nom d'un utilisateur dans la liste
    - Le profil détaillé affiche les informations suivantes :
        - `Photo`
        - `Civilité`, `Prénom`, `Nom`
        - `Nationalité`
        - `Date de naissance`
        - `Ville`
        - `Pays`
        - `Email`
        - `Téléphone`
        - `Mobile`
        - `Username`
        - `UUID`
    - Deux boutons d'action sont présents dans le profil :
        - `Dupliquer l'utilisateur` : Crée une copie de l'utilisateur dans la liste (avec la mention `(copie)` à côté de sont nom) et le sélectionne
        - `Supprimer l'utilisateur` : Supprime l'utilisateur de la liste et le désélectionne
        - Remarque : aucune action (`POST`, `DELETE`) ne doit être faite sur l'API pour ces deux boutons. Seule la liste déjà récupérée (et en mémoire) sera modifiée


### Exemple de rendu
![Exemple datalumni-test-vue](https://github.com/waldeck-dev/datalumni-technical-tests/blob/main/javascript/datalumni-test-vue2.png?raw=true)

*Votre travail ne doit pas nécessairement ressembler parfaitement à cet exemple*
