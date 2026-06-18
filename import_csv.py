import mariadb
from datetime import datetime

# Connexion à la base
connexion = mariadb.connect(
    host="10.129.5.76",
    user="toto",
    password="bernana",
    database="sae"
)

curseur = connexion.cursor()

# Lecture du fichier CSV
fichier = open("donnees.csv", "r")

for ligne in fichier:

    # Exemple :
    # Id=B8A5F3569EFF,piece=sejour,date=16/06/2026,time=09:13:36,temp=8.33

    infos = ligne.strip().split(",")

    nom_capteur = infos[0].split("=")[1]
    piece = infos[1].split("=")[1]
    date = infos[2].split("=")[1]
    heure = infos[3].split("=")[1]
    temp = infos[4].split("=")[1]

    # Vérifier si le capteur existe
    curseur.execute(
        "SELECT id FROM capteurs WHERE nom_capteur = %s",
        (nom_capteur,)
    )

    resultat = curseur.fetchone()

    # Si le capteur n'existe pas
    if resultat is None:

        curseur.execute(
            "INSERT INTO capteurs(nom_capteur,piece) VALUES(%s,%s)",
            (nom_capteur, piece)
        )

        connexion.commit()

        curseur.execute(
            "SELECT id FROM capteurs WHERE nom_capteur = %s",
            (nom_capteur,)
        )

        resultat = curseur.fetchone()

    capteur_id = resultat[0]

    # Insertion de la mesure
    timestamp = datetime.strptime(
        date + " " + heure,
        "%d/%m/%Y %H:%M:%S"
    )

    curseur.execute(
        "INSERT INTO donnees(capteur_id,valeur,timestamp) VALUES(%s,%s,%s)",
        (capteur_id, temp, timestamp)
    )

    connexion.commit()

fichier.close()
connexion.close()