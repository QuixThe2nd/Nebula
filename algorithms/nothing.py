class Nothing():
    def __init__(self):
        pass

    def compress(self, image: list[list[int]]) -> bytes:
        return b''

    def decompress(self, compressed: bytes) -> list[list[int]]:
        return []
