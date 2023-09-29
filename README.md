# Nebula
A novel approach to monotone image compression.

## Serialisation:
The first 2 bytes in the compressed file are used as the unique identifier for the final compression algorithm, which is the first algorithm that must be decoded to decompress the image. Once decoded, the decoded value will be in an identical format allowing for recursive decompression in all algorithms.
