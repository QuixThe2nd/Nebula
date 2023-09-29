from modules.image import Image

IMAGE_PATH = "test.png"
image = Image(IMAGE_PATH)
image.read()
print(image.data())

image.serialize()
print(image.serialized())
