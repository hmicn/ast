import socket

class Broadcaster:
    def __init__(self, interface, mac_destination, mac_source):
        self.__interface = interface
        self.__mac_destination = mac_destination
        self.__mac_source = mac_source

    def __sendeth(self, ethernet_packet, payload):
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        s.bind((self.__interface, 0))
        return s.send(ethernet_packet + payload)

    @staticmethod
    def pack(byte_sequence):
        return b"".join(map(chr, byte_sequence))

    def broadcast(self, icmp):
        # src=fe:ed:fa:ce:be:ef, dst=52:54:00:12:35:02, type=0x0800 (IP)
        ethernet_packet = self.__mac_destination + self.__mac_source

        # src=10.0.2.15, dst=195.88.54.16 (vg.no), checksum, etc.
        # ipv4_header = [0x45, 0x00, 0x00, 0x54, 0x05, 0x9f, 0x40, 0x00, 0x40, 0x01,
        #     0x2f, 0x93, 0x0a, 0x00, 0x02, 0x0f, 0xc3, 0x58, 0x36, 0x10]

        # echo (ping) request, checksum 2b45, etc

        # payload = "".join(map(chr, ipv4_header + icmp_ping))
        # payload = "".join(map(chr, icmp))

        # Construct Ethernet packet with an IPv4 ICMP PING request as payload
        # r = sendeth(pack(ethernet_packet),
        #             pack(ipv4_header + icmp_ping))    
        r = self.__sendeth(Broadcaster.pack(ethernet_packet), Broadcaster.pack(icmp))
        print("Sent Ethernet w/o [IPv4] ICMP payload of length %d bytes" % r)
