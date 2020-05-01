from app import AsterixReceiver
from app import PacketHandler
from app import FrameBuilder
from app import NetworkBroadcaster
from app import Server
from app.helpers import ConfigRetriever

if __name__ == '__main__':
    # setting up receiver
    incoming_broadcast_config = ConfigRetriever.get_incoming_broadcast_config()
    receiver = AsterixReceiver(incoming_broadcast_config['address'], incoming_broadcast_config['port'])

    # setting up broadcaster
    outgoing_broadcast_config = ConfigRetriever.get_outgoing_broadcast_config()
    source_mac = ConfigRetriever.get_mac_address(outgoing_broadcast_config['source_if'])
    broadcaster = NetworkBroadcaster(outgoing_broadcast_config['source_if'], outgoing_broadcast_config['target_mac'], source_mac, outgoing_broadcast_config['port'])
    
    # setting up handler
    frame_builder = FrameBuilder()
    handler = PacketHandler(broadcaster, frame_builder)

    # setting up server
    server = Server(receiver, handler)
    server.serve()