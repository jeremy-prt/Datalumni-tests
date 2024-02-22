# Tests techniques : SQL
Dans cette partie, il vous est demandé de rédiger des requêtes SQL permettant de répondre aux problèmes posés.

## Base de données
Une base de données [SQLite 3](https://www.sqlite.org/) est fournie pour ces tests.
```
./sql/db.sqlite3
```
Vous pouvez visualiser le schéma de base de données et les données elles-mêmes grâce à un logiciel dédié : [DB Browser for SQLite
](https://sqlitebrowser.org/) ou [DBeaver](https://dbeaver.io/), par exemple.

## À propos des données
Les données fournies sont fictives et émulent un système de commandes. Elle sont organisées de la manière suivante:

| Table | Description |
|---|---|
| `user` | Utilisateurs enregistrés dans le système et suceptibles de passer commande |
| `order` | En-tête de commande contenant les données relative à une commande |
| `order_line` | Détails d'un ligne de commande |

IMG

---

# Tests
## Test n°1
**Colonnes à afficher** :
| # | Nom | Details |
|:---:|---|---|
| 1 | `User ID` | ID unique de l'utilisateur |
| 2 | `Full name` | Nom complet de l'utilisateur: Prénom NOM |
| 3 | `Order ID` | ID unique de la commande |
| 4 | `Order Status` | Statut de la commande :<br>`Received`, `Paid`, `Prepared`, `Shipped`, `Delivered`<br>à déterminer en fonction des dates disponibles dans la table `order` |

**Autres consignes** :
- N'afficher que les commandes de l'`id` `1337` à `1500` (inclus)
- Ordonner les lignes par nom (`last_name`) décroissant

Sauvegarder la requête dans `./sql/test1.sql`

---

## Test n°2
**Colonnes à afficher** :
| # | Nom | Details |
|:---:|---|---|
| 1 | `Year` | Année |
| 2 | `Order count` | Nombre de commandes |
| 3 | `Line count` | Nombre de lignes de commande |

**Autres consignes** :
- Grouper les résultats par années, de `2010` à `2020` (inclus)

Sauvegarder la requête dans `./sql/test2.sql`

---

## Test n°3
Certains utilisateurs ayant fait une commande précédemment n'existent plus dans la table `user`.

**Colonnes à afficher** :
| # | Nom | Details |
|:---:|---|---|
| 1 | `Missing user ID` | ID de l'utilisateur |

**Autres consignes** :
- Lister uniquement les `user_id` des utilisateurs que n'existent plus dans la table `user`

Sauvegarder la requête dans `./sql/test3.sql`

---

## Test n°4
Calculer le rang des utilsateurs en fonction du Chiffre d'Affaires qu'ils représentent (du plus élevé au plus faible) pour l'année 2018 et comparer avec le rang de 2019.

*Colonnes à afficher** :
| # | Nom | Details |
|:---:|---|---|
| 1 | `User ID` | ID unique de l'utilisateur |
| 2 | `Full name` | Nom complet de l'utilisateur: Prénom NOM |
| 3 | `Rank 2018` | Rang de l'utilisateur en CA pour 2018 |
| 4 | `Rank 2019` | Rang de l'utilisateur en CA pour 2019 |

**Autres consignes** :
- N'afficher que les utilisateurs du top `10` de `2018` (seulement 10 lignes)

Sauvegarder la requête dans `./sql/test4.sql`
