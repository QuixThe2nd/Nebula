from modules.image import Image
from modules.serializer import Serializer
from modules.Byte_Repetition import Byte_Repetition
from utils.dimensions import dimensions

IMAGE_PATH = "test.png"
image = Image(IMAGE_PATH)
data = image.read()
print(f"Image Size: {len(data)*len(data[0])}")

dimensions = dimensions(data)

serializer = Serializer(dimensions)
serialized = serializer.serialize(data)
print(f"Serialized Size: {len(serialized)}")

repetition = Byte_Repetition(dimensions)
compressed = repetition.input(serialized)
print(f"Compressed Size: {len(compressed)}")
