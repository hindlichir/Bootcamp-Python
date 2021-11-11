class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(words, list) or not isinstance(coefs, list):
            return -1
        for elem in words:
            if not isinstance(elem, str):
                return -1
        for elem in coefs:
            if not isinstance(elem, float) and not isinstance(elem, int):
                return -1
        if len(words) != len(coefs):
            return -1
        zipped_list = list(zip(words, coefs))
        count = 0
        for elem in zipped_list:
            count = count + len(elem[0]) * elem[1]
        return count

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(words, list) or not isinstance(coefs, list):
            return -1
        for elem in words:
            if not isinstance(elem, str):
                return -1
        for elem in coefs:
            if not isinstance(elem, float) and not isinstance(elem, int):
                return -1
        if len(words) != len(coefs):
            return -1
        count = 0
        for index, elem in enumerate(words):
            count = count + len(elem) * coefs[index]
        return count
