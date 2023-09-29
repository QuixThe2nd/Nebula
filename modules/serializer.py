import struct
from utils.dimensions import dimensions

class Serializer:
    def __init__(self):
        pass

    def serialize(self, data: list[list[int]]) -> bytes:
        output = b'\x00\x00' +  b''.join([struct.pack('H', number) for number in dimensions(data)])
        for row in data:
            for pixel in row:
                output += struct.pack('H', pixel)
        return output