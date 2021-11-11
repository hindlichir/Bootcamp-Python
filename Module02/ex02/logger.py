import time
from random import randint
import logging
import functools
import getpass


logging.basicConfig(filename='machine.log', format='%(message)s')
logger = logging.getLogger('machine.log')
logger.setLevel(logging.DEBUG)


class LogDecorator(object):
    def __init__(self):
        self.logger = logging.getLogger('machine.log')

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            try:
                us = getpass.getuser()
                n = fn.__doc__.ljust(27)
                start = time.time()
                result = fn(*args, **kwargs)
                t = time.time() - start
                un = "s"
                if t < 0.001:
                    t = t * 1000
                    un = "ms"
                s = "({0}){1} [exec-time = {2:.3f} {3} ]".format(us, n, t, un)
                self.logger.info(s)
                return result
            except Exception as ex:
                self.logger.debug("Exception {0}".format(ex))
                raise ex
            return result
        return decorated


class CoffeeMachine():

    water_level = 100

    @LogDecorator()
    def start_machine(self):
        """Running: Start Machine"""
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @LogDecorator()
    def boil_water(self):
        """Running: Boil Water"""
        return "boiling..."

    @LogDecorator()
    def make_coffee(self):
        """Running: Make Coffee"""
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @LogDecorator()
    def add_water(self, water_level):
        """Running: Add Water"""
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
