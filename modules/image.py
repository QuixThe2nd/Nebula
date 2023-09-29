import cv2

class Image:
    def __init__(self, path: str):
        self.path = path

    def read(self) -> list[list[int]]:
        return cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)
