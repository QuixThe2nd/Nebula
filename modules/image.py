import cv2
from .serializer import Serializer

class Image:
    def __init__(self, path: str):
        self._path: str = path
        self._data: list[list[int]] = []
        self._serializer: Serializer = Serializer()

    def read(self) -> None:
        self._data = cv2.imread(self._path, cv2.IMREAD_GRAYSCALE).tolist()

    def serialize(self) -> None:
        self._serializer.serialize(self._data)

    def data(self) -> list[list[int]]:
        return self._data
    
    def serialized(self) -> bytes:
        return self._serializer.output()
