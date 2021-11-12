from contextlib import contextmanager
import string


class CsvReader:
    def __init__(self, filename=None, sep='.', h=False, s_top=0, s_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = h
        self.skip_top = s_top
        self.skip_bottom = s_bottom
        self.file = None

    def __enter__(self):
        try:
            open(self.filename, 'r')
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")
        except Exception:
            print("Something wrong hqppened while opening file.")
        else:
            self.file = open(self.filename, 'r')
            count = self.get_line_count()
            self.file.close()
            self.file = open(self.filename, 'r')
            if self.check_if_corrupted(count) == 1:
                self.__exit__(0, 0, 0)
                self.file = None
                return None
            else:
                self.__exit__(0, 0, 0)
                self.file = open(self.filename, 'r')
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        if self.file is not None:
            self.file.close()

    def check_if_corrupted(self, count):

        lst = []
        for i in range(0, count):
            tmp_lst = []
            line = list(self.file.readline().split(','))
            for elem in line:
                if elem.strip():
                    tmp_lst.append(elem.strip())
            lst.append(tmp_lst)
        if lst is None:
            return 1
        for i in range(0, len(lst) - 1):

            if len(lst[i]) != len(lst[i + 1]):
                return 1
        return 0

    def get_line_count(self):
        if self.file is not None:
            for count, line in enumerate(self.file):
                pass
            return count
        else:
            return -1

    def getdata(self):
        self.__enter__()
        if self.file is not None:
            count = self.get_line_count()
            self.__exit__(0, 0, 0)
            self.__enter__()
            lst = []
            if self.header:
                tmp_lst = []
                line = list(self.file.readline().split(','))
                for elem in line:
                    if elem.strip():
                        tmp_lst.append(elem.strip())
                lst.append(tmp_lst)
            for i in range(0, self.skip_top):
                self.file.readline()
            for i in range(self.skip_top, count - self.skip_bottom):
                tmp_lst = []
                line = list(self.file.readline().split(','))
                for elem in line:
                    if elem.strip():
                        tmp_lst.append(elem.strip())
                lst.append(tmp_lst)
        else:
            self.__exit__(0, 0, 0)
            return None
        self.__exit__(0, 0, 0)
        return lst

    def getheader(self):
        if self.header and self.file is not None:
            self.__enter__()
            line = list(self.file.readline().split(','))
            lst = []
            for elem in line:
                lst.append(elem.strip())
            self.__exit__(0, 0, 0)
            return lst
        else:
            return None


if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
