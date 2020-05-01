from app.helpers.parity_computer import ParityComputer
from app.helpers.packet_helper import PacketHelper
import struct

class FrameBuilder:
    bcd_table_with_lsb_first = [
            [0x0, 0x0, 0x0, 0x0],
            [0x1, 0x0, 0x0, 0x0],
            [0x0, 0x1, 0x0, 0x0],
            [0x1, 0x1, 0x0, 0x0],
            [0x0, 0x0, 0x1, 0x0],
            [0x1, 0x0, 0x1, 0x0],
            [0x0, 0x1, 0x1, 0x0],
            [0x1, 0x1, 0x1, 0x0],
            [0x0, 0x0, 0x0, 0x1],
            [0x1, 0x0, 0x0, 0x1]
        ]
    bin_table_with_lsb_first = [
            [0x0, 0x0, 0x0],
            [0x1, 0x0, 0x0]
        ]

    @staticmethod
    def __build_qdm_part_on_2_bits(qdm_part):
        return [0x1 if qdm_part > 7 else 0x0, qdm_part % 2]

    @staticmethod
    def __build_qdm_part_on_4_bits(qdm_part):
        if qdm_part > 9:
            raise Exception('QDM part has to be on a single digit')
        return FrameBuilder.bcd_table_with_lsb_first[qdm_part]
        
    @staticmethod
    def __build_frequency_index(freq):
        if freq <= 0:
            raise Exception('Freq has to start from 1')
        return FrameBuilder.bin_table_with_lsb_first[freq]

    @staticmethod
    def __bin_list_to_bytes(bin_list):
        return bytes([int("".join(str(i) for i in bin_list), 2)])

    @staticmethod
    def __wrap(frame):
        frame = frame + [ParityComputer.compute(frame)]
        return FrameBuilder.__bin_list_to_bytes(frame)

    def __build_frame_1(self, qdm_part, frequency_index):
        return FrameBuilder.__wrap(FrameBuilder.__build_qdm_part_on_2_bits(qdm_part) + FrameBuilder.__build_frequency_index(frequency_index) + [
            0x1, 0x0
        ])

    def __build_frame_2(self, qdm_part):
        return FrameBuilder.__wrap(FrameBuilder.__build_qdm_part_on_4_bits(qdm_part) + [
            0x1, 0x0, 0x1
        ])

    def __build_frame_3(self, qdm_part):
        return FrameBuilder.__wrap(FrameBuilder.__build_qdm_part_on_4_bits(qdm_part) + [
            0x0, 0x1, 0x1
        ])

    def __build_frame_4(self, frequency_index):
        return FrameBuilder.__wrap([0x1, 0x0] + FrameBuilder.__build_frequency_index(frequency_index) + [
            0x0, 0x0
        ])

    def build(self, packet):
        frenquency_index = PacketHelper.get_frenquency_index(packet)
        qdm = PacketHelper.get_qdm(packet)
        qdm_hundreds = int(qdm / 100) % 10
        qdm_tens = int(qdm / 10) % 10
        qdm_units = int(qdm) % 10
        return [
            self.__build_frame_1(qdm_hundreds, frenquency_index),
            self.__build_frame_2(qdm_tens),
            self.__build_frame_3(qdm_units),
            self.__build_frame_4(frenquency_index)
        ]