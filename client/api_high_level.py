import zmq

# Fonction du client
def send_requests():
    context = zmq.Context()

    # Connecter au broker via son adresse IP et port frontend
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.1.10:5570")  # Adresse IP du broker

    # Envoyer des requêtes au broker
    for i in range(5):
        message = f"Tâche {i + 1}"
        print(f"Client : envoi de la tâche -> {message}")
        socket.send_string(message)

        # Réception de la réponse du broker (via un travailleur)
        response = socket.recv_string()
        print(f"Client : réponse reçue -> {response}")

    # Nettoyage du contexte
    socket.close()
    context.term()

if __name__ == "__main__":
    print("Lancement du client...")
    send_requests()
