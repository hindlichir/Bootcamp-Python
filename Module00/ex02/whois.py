import sys


def analyze_integer(nb):
    if nb == 0:
        print("I'm Zero.")
    elif nb % 2 == 1:
        print("I'm Odd.")
    else:
        print("I'm Even.")


args = sys.argv
if len(args) == 2:
    if args[1].isdigit():
        nb = int(args[1])
        analyze_integer(nb)
    elif args[1][0] == '-' and args[1][1:].isdigit():
        nb = int(args[1][1:])
        analyze_integer(nb)
    else:
        print("ERROR")
elif len(args) != 1:
    print("ERROR")
