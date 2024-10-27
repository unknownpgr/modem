import numpy as np


class Codec:
    def __init__(self):
        self.sync_signal = [0, 1] * 16
        self.preamble = [0, 0, 0, 1, 0, 0, 0, 1] * 2
        self.preamble_buffer = []
        self.byte_buffer = []

    def encode_bits(self, bits):
        return self.sync_signal + self.preamble + bits

    def encode_string(self, string):
        data = []
        byte_data = string.encode("utf-8")
        for byte in byte_data:
            for i in range(8):
                data.append((byte >> i) & 1)
        return self.encode_bits(data)

    def decode(self, bit):
        if bit is None:
            return None

        # Clear byte buffer when preamble is detected
        self.preamble_buffer.append(bit)
        if len(self.preamble_buffer) > len(self.preamble):
            self.preamble_buffer.pop(0)
        if self.preamble_buffer == self.preamble:
            self.byte_buffer = []
            return None

        # Decode byte when 8 bits are received
        self.byte_buffer.append(bit)
        if len(self.byte_buffer) == 8:
            byte = 0
            for i in range(8):
                byte |= self.byte_buffer[i] << i
            self.byte_buffer = []
            return bytes([byte])

        return None
