import sys
import string


def print_error(type):
    if type == 0:
        print("InputError: only numbers\n")
    elif type == 1:
        print("InputError: too few argumets\n")
    elif type == 2:
        print("InputError: too many arguments\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n   python operations.py 10 3")


def print_result(nb1, nb2):
    types = ["Sum:        ", "Difference: ", "Product:    "]
    types = types + ["Quotient:   ", "Remainder:  "]
    if nb2 == 0:
        quotient = "ERROR (div by zero)"
        remainder = "ERROR (modulo by zero)"
    else:
        quotient = str(nb1 / nb2)
        remainder = str(nb1 % nb2)
    results = [str(nb1+nb2), str(nb1-nb2), str(nb1*nb2), quotient, remainder]
    for i in range(0, 5):
        print(types[i], results[i])


error = 0
args = sys.argv
if len(args) != 3:
    if len(args) == 1:
        print_error(-1)
    elif len(args) < 3:
        print_error(1)
    else:
        print_error(2)
else:
    if args[1].isdigit() or (args[1][0] == '-' and args[1][1:].isdigit()):
        nb1 = int(args[1])
    else:
        error = 1
    if args[2].isdigit() or (args[2][0] == '-' and args[2][1:].isdigit()):
        nb2 = int(args[2])
    else:
        error = 1
    if error == 1:
        print_error(0)
    else:
        print_result(nb1, nb2)
