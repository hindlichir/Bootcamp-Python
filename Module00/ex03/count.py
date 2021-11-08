import string


def text_analyzer(*args):
    """You can use this function if you want to know how many upper &
    lower letters, spaces & punctuation marks you have in a given text.
    Very important informations, I know!"""
    if len(args) == 0:
        txt = input("What is the text to analyze?\n>> ")
    elif len(args) == 2:
        print("ERROR")
        return None
    else:
        txt = args[0]
    upper = sum(c.isupper() for c in txt)
    lower = sum(c.islower() for c in txt)
    space = sum(c.isspace() for c in txt)
    punctuation = sum(string.punctuation.find(c) != -1 for c in txt)
    print("The text contains", len(txt), "characters")
    print("-", upper, "upper letters")
    print("-", lower, "lower letters")
    print("-", punctuation, "punctuation marks")
    print("-", space, "spaces")
