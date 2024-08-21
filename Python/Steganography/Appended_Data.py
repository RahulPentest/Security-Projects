def encode_message(image_path: str, message: str):
    try:
        with open(image_path, "ab") as image:
            image.write(message.encode("utf-8"))
            return "Message encoded successfully"
    except Exception as error:
        return f"The error: '{error}' occurred"

def decode_message(image_path: str):
    iend_chunk = b"\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82"
    eoi_marker = b"\xFF\xD9"

    try:
        end_of_file_indicator = eoi_marker if "jpeg" in image_path else iend_chunk

        with open(image_path, "rb") as image:
            image_data = image.read()
            offset = image_data.index(end_of_file_indicator)
            image.seek(offset + len(end_of_file_indicator))
            return f"The message is: {image.read()}"

    except Exception as error:
        return f"The error: '{error}' occurred"


# < ------------ NOTES ------------ >
# Appended Data Steganography
# this program works by appending the payload after the IEND chunk or the EOI marker

# basic information about PNG files
#   - uses lossless compression
#   - the PNG file signature -> refers to the first 8 bytes of a PNG file
#     - the PNG file signature is -> 89 50 4e 47 0d 1a 0a (hexadecimal)
#     - the PNG file signature is always the same for ALL PNG files because,
#       it is used by software to recognize the file as a PNG
#   - IEND chunk -> refers to the last 12 bytes of a PNG file
#     - the IEND chunk is -> 00 00 00 00 49 45 4E 44 AE 42 60 82 (hexadecimal)
#     - the IEND chunk is always the same for ALL PNG files
#   - terminology,
#     - IHDR -> header
#     - PLTE -> palette table
#     - IDAT -> image data
#     - IEND -> image end, end of file

# basic information about JPEG files
#   - uses lossy compression, LSB steganography is less effective
#   - the JPEG file signature -> refers to the first 2 bytes of a JPEG file
#      - the JPEG file signature is -> FF D8 (hexadecimal)
#      - the JPEG files signature is always the same for All JPEG files
#   - EOI marker -> refers to the last 2 bytes of a JPEG file
#      - the EOI marker is -> FF D9 (hexadecimal)
#      - the EOI marker is always the same for ALL JPEG files

# b"" -> denotes a byte string for handling raw binary data
#   - it will convert characters inside it to bytes according to the character's ASCII value
# \x -> a way to encode hexadecimal values into byte strings
# ab -> appending bytes (it is a file mode)
# rb -> reading bytes (it is a file mode)

#   .read() (when the file mode is rb) -> will return a bytes object
#   .seek() -> moves the file cursor to a specified position in the file, 
#       allowing you to read from or write to that location
# <parameter_name>: <data type>  -> it is referred to as type hint
# Based on a video from NeuralNine