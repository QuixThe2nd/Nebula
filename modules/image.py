import cv2

class Image:
    def __init__(self, path: str):
        self._path: str = path
        self._data: list[list[int]] = []

    def read(self) -> None:
        self._data = cv2.imread(self._path, cv2.IMREAD_GRAYSCALE).tolist()

    def data(self) -> list[list[int]]:
        return self._data
