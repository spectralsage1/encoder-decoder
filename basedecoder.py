import base64 as b64

def standard_selection():
    encodestandard = input("Type the corresponding number with your desired encoding standard\n1 : Base64\n2 : Base32\n3 : Hexadecimal\n")
    if encodestandard != 1 or 2 or 3:
        raise ValueError("Error: number must be listed above")
    elif encodestandard == 1:
        encodestandard = "Base64"
    elif encodestandard == 2:
        encodestandard = "Base32"
    elif encodestandard == 3:
        encodestandard = "Hexadecimal"

#original_string = input(f"Please enter your {encodestandard} encoded string")
def encryption():

    original_string = input(f"Please enter your {encodestandard} encoded string: ")
    if encodestandard == "Base64":
        decoded_bytes = b64.b64decode(original_string)
        decoded_string = decoded_bytes.decode('utf-8')
        print(f"Your decoded string is: {decoded_string}")
    elif encodestandard == "Base32":
        decoded_bytes = b64.b32decode(original_string)
        decoded_string = decoded_bytes.decode('utf-8')
        print(f"Your decoded string is: {decoded_string}")
    elif encodestandard == "Hexadecimal":
        decoded_bytes = bytes.fromhex(original_string)
        decoded_string = decoded_bytes.decode('utf-8')
        print(f"Your decoded string is: {decoded_string}")


try:
    standard_selection()
except ValueError:
    pass
