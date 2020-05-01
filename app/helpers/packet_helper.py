class PacketHelper:
    @staticmethod
    def get_qdm(packet):
        return int(packet['qdm'])

    @staticmethod
    def get_frenquency_index(packet):
        return int(packet['frenquency_index'])

    @staticmethod
    def is_asterix_version_205(packet):
        return packet['asterix_version'] == 'v205'

    @staticmethod
    def is_frequency_index_valid(packet):
        return PacketHelper.get_frenquency_index(packet) <= 2