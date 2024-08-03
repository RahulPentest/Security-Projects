def encode_message(image_path, message):
    try:
        with open(image_path, "ab") as image:
            image.write(message.encode("utf-8"))
            return "Message encoded successfully"
    except Exception as error:
        return f"The error: '{error}' occurred"

def decode_message(image_path):
    file_end = b"\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82"
    try:
        with open(image_path, "rb") as image:
            image_data = image.read()
            offset = image_data.index(file_end)
            image.seek(offset + len(file_end))
            return f"The message is: {image.read()}"

    except Exception as error:
        return f"The error: '{error}' occurred"

# < ------------ NOTES ------------ >
# this program works by appending the payload after the IEND chunk of a PNG file
#
# basic information about PNG files
#   - the PNG file signature -> refers to the first 8 bytes of a PNG file
#     - the PNG file signature is -> 89 50 4e 47 0d 1a 0a (hexadecimal)
#     - the PNG file signature is always the same for ALL PNG files because,
#       it is used by software to recognize the file as a PNG
#   - IEND chunk -> refers to the last 12 bytes of a PNG file
#     - the IEND chunk is -> 00 00 00 00 49 45 4E 44 AE 42 60 82 (hexadecimal)
#     - the IEND chunk is always the same for ALL PNG files
#     - softwares that work with PNG files will ignore any data after the IEND chunk because,
#       the data after the IEND chunk has nothing to do with the PNG file therefore,
#       data can be hidden after the IEND chunk and still be extracted
#   - terminology,
#     - IHDR -> header
#     - PLTE -> palette table
#     - IDAT -> image data
#     - IEND -> image end, end of file
# b"" -> denotes a byte string for handling raw binary data
#   - it will convert characters inside it to bytes according to the character's ASCII value
# \x -> a way to encode hexadecimal values into byte strings
# ab -> appending bytes (it is a file mode)
# rb -> reading bytes (it is a file mode)
#
#   .read() (when the file mode is rb) -> will return a bytes object
#   .seek() -> moves the file cursor to a specified position in the file, 
#       allowing you to read from or write to that location