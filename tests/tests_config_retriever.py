import unittest
from app.helpers import ConfigRetriever

class TestsConfigRetriever(unittest.TestCase):
    def test_get_mac_address(self):
        mac_address = ConfigRetriever.get_mac_address('enp0s25')
        self.assertEqual(str(mac_address), str([60, 151, 14, 70, 104, 25]))
