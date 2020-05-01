import unittest
from app.frame_builder import FrameBuilder
from .mocks import MockAsterixReceiver

class TestsFrameBuilder(unittest.TestCase):
    def setUp(self):
        self.__service = FrameBuilder()
        self.__asterix_receiver = MockAsterixReceiver()

    def test_build(self):
        packet = self.__asterix_receiver.get_packet_valid()
        frames = self.__service.build(packet)
        self.assertEqual(str(frames), str([b'$', b'\xca', b"'", b'\xa0']))
