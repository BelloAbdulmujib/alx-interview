#!/usr/bin/python3
""" UTF-8 Validation(data) """


def validUTF8(data):
    """
    A method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    num_of_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for j in data:

        mask_byte = 1 << 7

        if num_of_bytes == 0:

            while mask_byte & j:
                num_of_bytes += 1
                mask_byte = mask_byte >> 1

            if num_of_bytes == 0:
                continue

            if num_of_bytes == 1 or num_of_bytes > 4:
                return False

        else:
            if not (j & mask_1 and not (j & mask_2)):
                return False

        num_of_bytes -= 1

    if num_of_bytes == 0:
        return True

    return False
