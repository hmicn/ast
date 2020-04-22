class PacketHandler:
    def __init__(self, broadcaster, frame_builder):
        self.__broadcaster = broadcaster
        self.__frame_builder = frame_builder

    def handle(self, packet):
        icmp = self.__frame_builder.build(packet)
        self.__broadcaster.broadcast(icmp)