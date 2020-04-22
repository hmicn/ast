from app import AsterixReceiver
from app import PacketHandler
from app import FrameBuilder
from app import Broadcaster

if __name__ == '__main__':
    # broadcaster emits new frame to system
    broadcaster = Broadcaster("eth0", [0x52, 0x54, 0x00, 0x12, 0x35, 0x02], [0xfe, 0xed, 0xfa, 0xce, 0xbe, 0xef, 0x08, 0x00])

    # building frame 
    frame_builder = FrameBuilder()

    handler = PacketHandler(broadcaster, frame_builder)
    receiver = AsterixReceiver(handler, "232.1.1.11", 21111)