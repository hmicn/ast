class MockAsterixReceiver:
    def get_packet_valid(self):
        return {
            'qdm' : 234,
            'frenquency_index' : 1,
            'asterix_version' : 'v205'
        }
        
    def get_packet_frequency_index_invalid(self):
        return {
            'qdm' : 234,
            'frenquency_index' : 4,
            'asterix_version' : 'v205'
        }

    def get_packet_asterix_version_invalid(self):
        return {
            'qdm' : 234,
            'frenquency_index' : 1,
            'asterix_version' : 'v209'
        }