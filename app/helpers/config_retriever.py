import fcntl
import socket
import struct

class ConfigRetriever:
    @staticmethod
    def get_incoming_broadcast_config():
        return {

            'address' : '212.12.213.23',
            'port' : 12432
        }

    @staticmethod
    def get_outgoing_broadcast_config():
        return {
            'source_if' : 'enp0s25',
            'target_mac' : [0x52, 0x54, 0x00, 0x12, 0x35, 0x02],
            'port' : 12432
        }

    @staticmethod
    def get_mac_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
        return [b for b in info[18:24]]