from utils.dimensions import dimensions
import struct

class Serializer:
    def __init__(self):
        self._output = b''

    def serialize(self, data: list[list[int]]) -> None:
        self._output = b'\x00\x00' +  b''.join([struct.pack('H', number) for number in dimensions(data)])
        for row in data:
            for pixel in row:
                self._output += struct.pack('H', pixel)

    def output(self) -> bytes:
        return self._output
