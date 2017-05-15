import random


# have no idea what this will be used for, looks like colors for the RPG.
# TBD
class bcolors:
    HEADER: '\033[95m'
    OKBLUE: '\033[94m'
    OKGREEN: '\033[92m'
    WARNING: '\033[93m'
    FAIL: '\033[91m'
    ENDC: '\033[0m'
    BOLD: '\033[1m'
    UNDERLINE: '\033[4m'


# init the Person class
class Person:
    # annoying that we have to init all the items passed in, but normal to do so
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions =["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)