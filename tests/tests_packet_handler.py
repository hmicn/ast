import unittest
from app.packet_handler import PacketHandler
from tests.mocks import MockNetworkBroadcaster
from tests.mocks import MockFrameBuilder
from tests.mocks import MockAsterixReceiver

class TestsPacketHandler(unittest.TestCase):
    def setUp(self):
        self.__service = PacketHandler(MockNetworkBroadcaster(), MockFrameBuilder())
        self.__asterix_recevier = MockAsterixReceiver()

    def test_handle(self):
        sent = self.__service.handle(self.__asterix_recevier.get_packet_valid())
        self.assertTrue(sent)
        sent = self.__service.handle(self.__asterix_recevier.get_packet_frequency_index_invalid())
        self.assertFalse(sent)
        sent = self.__service.handle(self.__asterix_recevier.get_packet_asterix_version_invalid())
        self.assertFalse(sent)
