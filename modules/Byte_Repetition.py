# Converts 0000 1111 to 04 14
import struct

class Byte_Repetition:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.id = 1

    def input(self, data: list[list[int]]) -> bytes:
        output = int(self.id).to_bytes(2, byteorder='big')
        last_byte = None
        repetitions = 0
        for byte in data:
            if byte == last_byte:
                repetitions += 1
            else:
                if last_byte != None:
                    output += repetitions.to_bytes(2, byteorder='big') + last_byte.to_bytes()
                last_byte = byte
                repetitions = 1
        output += repetitions.to_bytes(2, byteorder='big') + last_byte.to_bytes()
        return output