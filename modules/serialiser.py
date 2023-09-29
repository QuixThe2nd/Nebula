from utils.dimensions import dimensions
import struct

class Serializer:
    def __init__(self):
        self.output = b''

    def serialise(self, data):
        self.output = b'\x00\x00' +  b''.join([struct.pack('H', number) for number in dimensions(data)])
        for row in data:
            for pixel in row:
                self.output += struct.pack('H', pixel)
