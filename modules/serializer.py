import struct

class Serializer:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.id = 0

    def serialize(self, data: list[list[int]]) -> bytes:
        output = int(self.id).to_bytes(2, byteorder='big')
        for row in data:
            for pixel in row:
                output += pixel.to_bytes()
        return output
