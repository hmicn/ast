from app import AsterixReceiver
from app import Dumper
from app.helpers import ConfigRetriever

if __name__ == '__main__':
    # setting up receiver
    incoming_broadcast_config = ConfigRetriever.get_incoming_broadcast_config()
    receiver = AsterixReceiver(incoming_broadcast_config['address'], incoming_broadcast_config['port'])

    # setting up dumper
    dumper = Dumper(receiver)
    dumper.serve()