import zmq
import argparse
import time

# Fonction principale pour le travailleur
def worker(worker_id, broker_ip):
    context = zmq.Context()

    # Connexion au broker sur son port backend
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{broker_ip}:5571")  # Adresse IP du broker

    print(f"Travailleur {worker_id} : connecté au broker ({broker_ip})")

    while True:
        # Envoi d'un signal de disponibilité au broker
        socket.send_string(f"Travailleur {worker_id} prêt")
        
        # Réception d'une tâche du broker
        task = socket.recv_string()
        print(f"Travailleur {worker_id} : tâche reçue -> {task}")

        # Simulation de traitement de la tâche
        time.sleep(2)  # Simuler une tâche longue
        result = f"{task} traité par Travailleur {worker_id}"

        # Retourner le résultat au broker
        socket.send_string(result)

if __name__ == "__main__":
    # Parser les arguments pour obtenir l'ID du travailleur et l'adresse IP du broker
    parser = argparse.ArgumentParser(description="Travailleur ZeroMQ")
    parser.add_argument("--worker-id", type=int, required=True, help="ID du travailleur")
    parser.add_argument("--broker-ip", type=str, required=True, help="Adresse IP du broker")
    args = parser.parse_args()

    # Lancer le travailleur
    worker(args.worker_id, args.broker_ip)
