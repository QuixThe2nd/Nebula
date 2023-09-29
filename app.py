from modules.image import Image

IMAGE_PATH = "test.png"
pixelArray = Image(IMAGE_PATH).read()
print(pixelArray)
