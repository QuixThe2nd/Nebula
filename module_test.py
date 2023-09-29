from modules.serialiser import Serializer

raw_image = [
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
]

serialiser = Serializer()
serialiser.serialize(raw_image)
print(serialiser.output)