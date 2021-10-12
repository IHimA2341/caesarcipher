# Used to repeatedly get the input if not inputted.
def get_input(input_message: str) -> str:
    input_text: str = ""
    while input_text == "":
        input_text = input(input_message)
    return input_text

# Encodes the text like a Caesar cipher.
def encode_text(text: str, rotate_number: int):
    # Sees where the capital letters are to put them back later.
    cap_list: List[int] = []
    for i in range(0, len(text) - 1):
        if text[i].isupper():
            cap_list.append(i)

    # Puts all the characters into their decimal equivalents and rotates them.
    ord_list = [ord(char.lower()) for char in list(text)]
    rotated_ord_list = [number if number == 32 else (number + rotate_number) - 26 if number + rotate_number > 122 else number + rotate_number for number in ord_list]
    # Turns them back into a string and prints it out
    rotated_text_list = [chr(number) for number in rotated_ord_list]

    # Puts the capital letters back
    for i in range(0, len(rotated_text_list)):
        if i in cap_list:
            rotated_text_list[i] = rotated_text_list[i].upper()
    
    print("".join(rotated_text_list))


# Decodes the shifted text.
def decode_text(text: str, rotate_number: int):
    # Sees where the capital letters are to put them back later.
    cap_list: List[int] = []
    for i in range(0, len(text) - 1):
        if text[i].isupper():
            cap_list.append(i)

    # Puts all the characters into their decimal equivalents and rotates them.
    ord_list = [ord(char.lower()) for char in list(text)]
    rotated_ord_list = [number if number==32 else (number-rotate_number) + 26 if number - rotate_number < 97 else number - rotate_number for number in ord_list]
    # Turns them back into a string and prints it out
    rotated_text_list = [chr(number) for number in rotated_ord_list]

    # Puts the capital letters back
    for i in range(0, len(rotated_text_list)):
        if i in cap_list:
            rotated_text_list[i] = rotated_text_list[i].upper()
    
    print("".join(rotated_text_list))


if __name__ == "__main__":
    # Gets the input from the user.
    input_text: str = get_input("What text would you like to rotate? ")
    choice: str = get_input("Would you like to encode or decode? ")
    if choice.lower() == "decode":
        print("Note: Not inputting anything will use the brute force technique instead, showing all possible combinations.")
    number: str = input("What number would you like to rotate the next by? ")
    if number == "" and choice.lower() == "decode":
        # Brute force approach
        for i in range(27):
            decode_text(input_text, i)
    elif choice.lower == "encode":
        encode_text(input_text, int(number))
    else:
        decode_text(input_text, int(number))
    
