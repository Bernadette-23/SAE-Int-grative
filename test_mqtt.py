import paho.mqtt.client as mqtt

# Adresse du broker
broker = "broker.hivemq.com"

# Topic à écouter
topic = "IUT/Colmar2026/SAE2.04/Maison1"

# Fonction exécutée lorsqu'un message arrive
def reception(client, userdata, message):
    print(message.payload.decode())

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