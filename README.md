# Nebula
A novel approach to monotone image compression.

## Serialisation:
The first 2 bytes in the outputted file are the unique identifier for the final compression algorithm used, which is the first algorithm that must be decoded to decompress the image. Once decoded, the decoded value will be in an identical format allowing for recursive decompression in all algorithms.
```
algorithm_bytecode: 000255 // A unique identifier for each algorithm. (2 bytes)
data: xxxxxx // Serialised value in algorithms respective format (unlimited bytes)
```
