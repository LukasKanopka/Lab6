#Laurynas Lukas Kanopka
def encode(input_str):
    new = []
    for char in input_str:
        char_value = int(char)
        if char_value < 7:
            new_char = str(char_value + 3)
        else:
            new_char = str(char_value - 7)
        new.append(new_char)
    return "".join(new)
#Changes made on Laurynas Lukas Kanopka by Alessandro De-La-O
def decode(encoded_str):
    original = []
    for char in encoded_str:
        char_value = int(char)
        if char_value < 3:
            original_char = str(char_value + 7)
        else:
            original_char = str(char_value - 3)
        original.append(original_char)
    return "".join(original)

def print_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")

if __name__ == '__main__':
    input_str = input("Enter a string: ")
    new_str = encode(input_str)
    print(new_str)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
