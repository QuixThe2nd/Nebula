import cv2

class Image:
    def __init__(self, path: str):
        self._path: str = path

    def read(self) -> list[list[int]]:
        return cv2.imread(self._path, cv2.IMREAD_GRAYSCALE).tolist()
