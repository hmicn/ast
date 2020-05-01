import socket
import struct

class NetworkBroadcaster:
    def __init__(self, interface, mac_destination, mac_source, port):
        self.__interface = interface
        self.__mac_destination = mac_destination
        self.__mac_source = mac_source
        self.__port = port

    def __sendeth(self, ethernet_packet, payload):
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        s.bind((self.__interface, self.__port))
        # TODO: CHECK protocol + packet building
        return s.send(ethernet_packet + b"1" + payload)

    @staticmethod
    def pack(byte_sequence):
        return b"".join(map(lambda x: bytes([x]), byte_sequence))

    def broadcast(self, frames):
        ethernet_packet = self.__mac_destination + self.__mac_source
        header = NetworkBroadcaster.pack(ethernet_packet)
        sent_legnths = []
        for frame in frames:
            r = self.__sendeth(header, frame)
            print("Sent Ethernet payload of length %d bytes" % r)
            sent_legnths.append(r)
        return sent_legnths
