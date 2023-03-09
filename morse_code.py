morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                   'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


# def convert_to_morse_code(text):
#     morse_code = ''
#     for char in text.upper():
#         if char != ' ':
#             morse_code += morse_code_dict[char] + ' '
#         else:
#             morse_code += ' '
#     return morse_code


# # example usage
# text = 'HELLO WORLD'
# morse_code = convert_to_morse_code(text)
# print(morse_code)

user_input = input("Type the text you want to convert into Morse Code: ")

characters = []

for char in user_input:
    characters.append(char.upper())

morse_code = ""

for char in characters:

    if char == " ":
        morse_code += "......."
    else:
        morse_code += morse_code_dict[char]
    morse_code += " "

print(morse_code)
