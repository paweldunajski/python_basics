import random

def get_file_txt(ext):
    return ext[ext.index(".") +1:]
def roll_dice(num):
    return random.randint(0, num)