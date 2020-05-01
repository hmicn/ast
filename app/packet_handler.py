from app.helpers.packet_helper import PacketHelper

class PacketHandler:
    def __init__(self, broadcaster, frame_builder):
        self.__broadcaster = broadcaster
        self.__frame_builder = frame_builder

    def handle(self, packet):
        if not PacketHelper.is_asterix_version_205(packet) or not PacketHelper.is_frequency_index_valid(packet):
            return False
        frames = self.__frame_builder.build(packet)
        self.__broadcaster.broadcast(frames)
        return True