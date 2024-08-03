import numpy as np
import PIL.Image

def encode_message(image_path: str, message: str, new_image_path: str, delimiter: str):
    try:

        message_in_binary = "".join(format(ord(character), "08b") for character in message.strip())
        message_in_binary += "".join(format(ord(character), "08b") for character in delimiter.strip())

        image = PIL.Image.open(image_path, "r")

        image_width, image_height = image.size
        image_data_array = np.array(list(image.getdata()))

        channels_available = 4 if image.mode == "RGBA" else 3
        pixels_available = image_data_array.size // channels_available

        if image.mode != "RGB" and image.mode != "RGBA":
            return "The PNG file is not supposed"
        elif len(message_in_binary) > pixels_available:
            return "Not enough pixels to store the message"
        
        bit_index = 0
        for x in range(pixels_available):
            for y in range(0, channels_available):
                if bit_index < len(message_in_binary):
                    image_data_array[x][y] = int(bin(image_data_array[x][y])[2:-1] + message_in_binary[bit_index], 2)
                    bit_index += 1
        
        image_data_array = image_data_array.reshape((image_height, image_width, channels_available))
        new_image = PIL.Image.fromarray(image_data_array.astype("uint8"), image.mode)
        new_image.save(new_image_path)
        return "Encoding was successful"

    except Exception as error:
        return f"The error: {error} occurred"


def decode_message(image_path: str, delimiter: str):
    try:
        image = PIL.Image.open(image_path)

        image_data_array = np.array(list(image.getdata()))

        channels_available = 4 if image.mode == "RGBA" else 3
        pixels_available = image_data_array.size // channels_available

        extracted_bits = "".join([bin(image_data_array[x][y])[-1] for x in range(pixels_available) for y in range(0, channels_available)])
        byte_sized_data = [extracted_bits[i:i+8] for i in range(0, len(extracted_bits), 8)]

        message = "".join([chr(int(byte_sized_data[i], 2)) for i in range(len(byte_sized_data))])

        if delimiter in message:
            return f"Message is: {message[0:message.index(delimiter)]}"
        else:
            return "Failed to extract specific message.\nPerhaps theres no message or the delimiter is incorrect"

    except Exception as error:
        return f"The error: {error} occurred"


# < ------------ NOTES ------------ >
# this program works by replacing the LSB with a bit from the binary version of the message
# this program is suitable for PNG files that use RGB or RBGA

# PIL -> python imaging library
# since PIL is outdated, Pillow is a fork of PIL and retains the import paths from PIL

# a fork refers to creating a new project by copying an existing project's code and modifying it

# least significant bit (LSB) -> the rightmost bit in a binary number, 
#   represents the smallest value, has the least impact on the number's overall value

# when using image.getdata(), pixel values are provided one-by-one without being stored, 
#   so converting to a list with list() is necessary to retain and access all pixel values 
#   simultaneously for further manipulation.

# a pixel in context of PNG files, can have 1, 3 (RGB), or 4 (RGBA) channels, (few examples)
#   - P -> pallete
#   - RGB -> red, green, blue
#   - RGBA -> A stands for alpha, meaning transparency
#   - .mode() is used to return the channel mode in string

# .join() -> Takes an iterable and concatenates its elements into a single string
# format(<value>, "08b") -> Converts an ASCII decimal value into an 8-bit binary string
# ord(<character>) -> Converts a string character into its ASCII decimal value
# delimiter -> Used to indicate the end of the message in the binary string

# .open() -> Opens the image file at the given path in read mode
# .size -> Returns a tuple with integers for width and height of the image
# .getdata() -> Retrieves the pixel data as a sequence of (r, g, b) tuples for RGB images or (r, g, b, a) for RGBA images
#   - It is a generator method that yields pixel values


# .size for the NumPy array gives the total number of values in the array


# line 24 - 27 explanation
# x -> Accesses the pixel in the image
# y -> Accesses the channel within the pixel (0 for Red, 1 for Green, 2 for Blue in RGB)
#    - The channel value is an integer between 0 and 255

# bin() -> Converts the integer channel value to its binary string representation with a '0b' prefix
#    - Example: bin(255) -> '0b11111111'

# [2:] -> Strips the '0b' prefix from the binary string
#    - Example: bin(255)[2:] -> '11111111'

# [2:-1] -> Strips the '0b' prefix and the last bit from the binary string
#    - Example: bin(255)[2:-1] -> '1111111' (removes the last bit)

# + message_in_binary[bit_index] -> Concatenates the next bit from the message to the modified binary string

# int(..., 2) -> Converts the modified binary string back to an integer
#    - 2 specifies that the string is in binary (base-2) format


# line 30 - 32 explanation
# .reshape((image_height, image_width, channels_available)) -> Reshapes the flat array back into the original image dimensions
#    - (image_height, image_width, channels_available) specifies the shape of the 3D array
#    - This converts the flat array into a 3D array with dimensions corresponding to the image size and channels

# PIL.Image.fromarray(image_data_array.astype("uint8"), image.mode) -> Creates an image from an array
#    - .astype("uint8") ensures that the pixel values are in the correct 8-bit format
#    - image.mode specifies the color mode of the image (e.g., 'RGB', 'RGBA')

# .save(new_image_path) -> Saves the new image with the encoded message to the specified path
#    - This writes the modified image data to a file
#    - If the file doesnt exist in the path, the file will be created

# # chr() -> Converts an integer to its corresponding character in unicode
# LSB steganography is not effective for JPEG because the extension uses lossy compression
# Based on a video from NeuralNine