import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    lis = []
    for item in range(10):
        rand_num = random.random()*5 + 30
        lis.append(rand_num)
        item += 1
    print(lis)