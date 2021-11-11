class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank:
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    @staticmethod
    def check_corrupt(account):
        list_attr = dir(account)
        if len(list_attr) % 2 == 0:
            return 1
        if sum(elem[0] == 'b' for elem in list_attr):
            return 2
        check = sum(elem[:3] == "zip" for elem in list_attr if len(elem) >= 3)
        if check == 0:
            return 3
        check = sum(elem[:4] == "addr" for elem in list_attr if len(elem) >= 4)
        if check == 0:
            return 4
        if sum(elem == "name" for elem in list_attr) == 0:
            return 5
        if sum(elem == "id" for elem in list_attr) == 0:
            return 6
        if sum(elem == "value" for elem in list_attr) == 0:
            return 7
        return 0

    def find_account(self, id):
        if isinstance(id, int):
            for elem in self.account:
                if elem.id == id:
                    if isinstance(elem, Account):
                        return elem
                    else:
                        print('Account was wrongly inputed!')
                        return None
        elif isinstance(id, str):
            for elem in self.account:
                if elem.name == id:
                    if isinstance(elem, Account):
                        return elem
                    else:
                        print('Account was wrongly inputed!')
                        return None
            print("Account not found in the bank servers.")
            return None
        else:
            print("Wrong identification for the account")
            return None

    def transfer(self, origin, dest, amount):
        acc_origin = self.find_account(origin)
        acc_dest = self.find_account(dest)
        if acc_origin is None or acc_dest is None:
            return False
        if (self.check_corrupt(acc_origin) or self.check_corrupt(acc_dest)):
            print("The account is corrupted!")
            return False
        if isinstance(amount, str) and not amount.isdigit():
            return False
        n_check = not isinstance(amount, int) and not isinstance(amount, float)
        if not isinstance(amount, str) and n_check:
            return False
        if amount < 0 or acc_origin.value < float(amount):
            return False
        return True

    def fix_account(self, account):
        acc = self.find_account(account)
        if acc is None:
            return False
        list_attr = dir(acc)
        check = self.check_corrupt(acc)
        while (check):
            if check == 1:
                if hasattr(acc, "to_uncorrupt"):
                    delattr(acc, "to_uncorrupt")
                else:
                    setattr(acc, "to_uncorrupt", 1)
            elif check == 2:
                for elem in list_attr:
                    if elem[0] == "b":
                        delattr(acc, elem)
            elif check == 3:
                setattr(acc, "zip", "to_define")
            elif check == 4:
                setattr(acc, "addr", "to_define")
            if check == 5:
                setattr(acc, "name", "to_define")
            if check == 6:
                setattr(acc, "id", acc.ID_COUNT)
                acc.ID_COUNT += 1
            if check == 7:
                setattr(acc, "value", 0)
            check = self.check_corrupt(acc)
        return True
