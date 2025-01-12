import zmq
import threading

class Broker(threading.Thread):
    def run(self):
        context = zmq.Context()

        # Socket ROUTER pour les clients
        frontend = context.socket(zmq.ROUTER)
        frontend.bind('tcp://*:5570')

        # Socket DEALER pour les workers
        backend = context.socket(zmq.DEALER)
        backend.bind('inproc://backend')

        print("Broker démarré : liaison entre clients et workers.")
        
        # Lancer un proxy pour relier frontend et backend
        zmq.proxy(frontend, backend)

        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":
    broker = Broker()
    broker.start()
    broker.join()
