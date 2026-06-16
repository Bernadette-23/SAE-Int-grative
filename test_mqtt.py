import paho.mqtt.client as mqtt
import mariadb

connexion = mariadb.connect(
    host="192.168.1.10",
    user="root",
    password="motdepasse",
    database="sae204"
)


# Adresse du broker
broker = "broker.hivemq.com"

# Topic à écouter
topic = "IUT/Colmar2026/SAE2.04/Maison1"

# Fonction exécutée lorsqu'un message arrive
def reception(client, userdata, message):
    texte = message.payload.decode()

    print(texte)

    fichier = open("donnees.csv", "a")
    fichier.write(texte + "\n")
    fichier.close()


# Création du client MQTT
client = mqtt.Client()

# Associer la fonction de réception
client.on_message = reception

# Connexion au broker
client.connect(broker)

# Abonnement au topic
client.subscribe(topic)

print("En attente des messages...")

# Boucle infinie
client.loop_forever()

