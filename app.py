from modules.image import Image
from modules.serializer import Serializer

IMAGE_PATH = "test.png"
image = Image(IMAGE_PATH)
data = image.read()

serializer = Serializer()
serialized = serializer.serialize(data)
print(serialized)
