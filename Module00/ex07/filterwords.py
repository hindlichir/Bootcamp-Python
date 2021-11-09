import string
import sys

args = sys.argv
if len(args) != 3:
    print("ERROR")
else:
    if isinstance(args[1], str) and args[2].isdigit():
        args[1] = args[1].translate(str.maketrans('', '', string.punctuation))
        lst = args[1].split()
        max = int(args[2])
        new_lst = [elem for elem in lst if len(elem) > max]
        print(new_lst)
    else:
        print("ERROR")
