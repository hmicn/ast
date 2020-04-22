import socket
import struct
import asterix

class AsterixReceiver:
    def __init__(self, handler, multicast_group, port):
        self.__multicast_group = multicast_group
        self.__port = port
        self.__handler = handler

    def serve(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', self.__port))
        mreq = struct.pack("=4sl", socket.inet_aton(self.__multicast_group), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        while True:
            asterix_packet = sock.recv(10240)
            parsed = asterix.parse(asterix_packet)
            self.__handler.handle(parsed)