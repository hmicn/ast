import socket
import struct
import asterix

class AsterixReceiver:
    def __init__(self, multicast_group, port):
        self.__multicast_group = multicast_group
        self.__port = port

        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__sock.bind(('', self.__port))
        mreq = struct.pack("=4sl", socket.inet_aton(self.__multicast_group), socket.INADDR_ANY)
        self.__sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def get_packet(self):
        return asterix.parse(self.__sock.recv(4096))