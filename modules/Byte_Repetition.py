# Converts 0000 1111 to 04 14
import struct

class Byte_Repetition:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.id = 1

    def input(self, data: bytes) -> bytes:
        output = int(self.id).to_bytes(2, byteorder='big')
        last_byte = data[0]  # Initialize last_byte to the first byte of the input data
        repetitions = 0
        for byte in data:
            if byte == last_byte:
                repetitions += 1
            else:
                output += repetitions.to_bytes(2, byteorder='big') + last_byte.to_bytes(1, byteorder='big')
                last_byte = byte
                repetitions = 1
        output += repetitions.to_bytes(2, byteorder='big') + last_byte.to_bytes(1, byteorder='big')
        return output
