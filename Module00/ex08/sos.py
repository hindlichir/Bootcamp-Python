import string
import sys

dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': ' '}

for c in string.whitespace:
    dict[c] = c

def encoder(av):
    new = ""
    for txt in av:
        txt = txt.translate(str.maketrans('', '', string.whitespace))
        for c in txt.upper():
            new = new + dict[c] + ' '
    new = new[:-1]
    return new

args = sys.argv
if (len(args) == 1):
    pass
else:
    error = 0
    for txt in args[1:]:
        txt = txt.translate(str.maketrans('', '', string.whitespace))
        if not txt.isalnum():
            error = 1
    if error == 1:
        print("ERROR")
    else:
        coded_txt = encoder(args[1:])
        print(coded_txt)
