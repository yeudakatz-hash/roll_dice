

def str_to_int(num):
    try:
        return int(num)
    except:
        return 0


def get_num():
    num = input("enter a number of rounds you want to play: ")
    while not 0 < str_to_int(num) <= 10:
        num = input("error \n enter a number of rounds you want to play: ")
    return str_to_int(num)


def get_name():
    name = input("enter your name: ")
    while len(name.strip()) == 0:
        name = input("enter your name: ")
    return name




def details():
    return get_num(), get_name()
