import random


def shuffle_list(words):
    for i in range(len(words) - 1, 0, -1):
        j = random.randint(0, i + 1)
        words[i], words[j] = words[j], words[i]
    return words


def handle_option(words, option):
    if option == "ordered":
        return sorted(words, key=str.lower)
    elif option == "unique":
        tmp_set = set()
        tmp_list = words
        words = []
        for elem in tmp_list:
            if elem not in tmp_set:
                words.append(elem)
                tmp_set.add(elem)
        return words
    elif option == "shuffle":
        return shuffle_list(words)
    else:
        print("ERROR")
        return None


def generator(text, sep=" ", option=None):
    if isinstance(text, str):
        words = text.split(sep)
        if option is not None:
            words = handle_option(words, option)
        if words is not None:
            for elem in words:
                yield elem
    else:
        print("ERROR")
