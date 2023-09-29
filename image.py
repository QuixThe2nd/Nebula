import cv2

class Image:
    def __init__(self, path: str):
        self.path = path

    def read(self):
        return cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)

# print(Image("test.png").read())
