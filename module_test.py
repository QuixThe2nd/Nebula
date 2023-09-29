import modules.serialiser

raw_image = [
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
]

serialiser = modules.serialiser.Serializer()
serialiser.serialize(raw_image)
print(serialiser.output)