import cv2
import numpy as np

class Image:
    def __init__(self, path: str):
        self._path: str = path

    def read(self) -> list[list[int]]:
        pixels = cv2.imread(self._path, cv2.IMREAD_GRAYSCALE)
        pixels = np.divide(pixels, 255)
        return (pixels > 0.5).astype(int).tolist()
