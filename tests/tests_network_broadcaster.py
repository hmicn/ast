import unittest
from app import NetworkBroadcaster
from app.helpers import ConfigRetriever
from tests.mocks import MockFrameBuilder

class TestsNetworkBroadcaster(unittest.TestCase):
    def setUp(self):
        outgoing_broadcast_config = ConfigRetriever.get_outgoing_broadcast_config()
        source_mac = ConfigRetriever.get_mac_address(
            outgoing_broadcast_config['source_if'])
        self.__service = NetworkBroadcaster(
            outgoing_broadcast_config['source_if'], outgoing_broadcast_config['target_mac'], source_mac, outgoing_broadcast_config['port'])
        self.__frame_builder = MockFrameBuilder()

    def test_build(self):
        frames = self.__frame_builder.build(None)
        sent_lengths = self.__service.broadcast(frames)
        self.assertEqual(str(sent_lengths), str([14, 14, 14, 14]))
