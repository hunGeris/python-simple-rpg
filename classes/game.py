import random


# Commandline colors for the RPG.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# init the Person class
class Person:
    # annoying that we have to init all the items passed in, but normal to do so
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + bcolors.OKBLUE + "ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ". " + item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + "MAGIC:" + bcolors.ENDC)
        print("    0. Go Back")
        for spell in self.magic:
            print("    " + str(i) + ". " + spell.name + " - cost: " + str(spell.cost))
            i += 1

    def choose_items(self):
        i = 1
        print("\n" + bcolors.OKGREEN + "ITEMS:" + bcolors.ENDC)
        print("    0. Go Back")
        for item in self.items:
            print("    " + str(i) + ". " + item["item"].name + " - description: " + item["item"].description + " (x" + str(item["quantity"]) + ")")
            i += 1