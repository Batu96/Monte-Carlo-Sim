import numpy as np
from numpy import random


def sim():
    counter = 0
    boxes = np.full((100, 2), 0, dtype=np.int32)
    # boxes = [ [black, white], ... ]
    flag = False
    for i in range(100):
        boxes[i] = [i + 1, i + 2]
    # first part
    for i in range(99):
        r = random.randint(0, boxes[i][0] + boxes[i][1])
        if 0 <= r < boxes[i][0]:
            r = 0
        else:
            r = 1
        if r:
            flag = True
        boxes[i][r] -= 1
        boxes[i + 1][r] += 1
    # second part
    for i in range(99, 0, -1):
        r = random.randint(0, boxes[i][0] + boxes[i][1])
        if 0 <= r < boxes[i][0]:
            r = 0
        else:
            r = 1
        boxes[i][r] -= 1
        boxes[i - 1][r] += 1
    # final draw
    r = random.randint(0, boxes[0][0] + boxes[0][1])
    if 0 <= r < boxes[0][0]:
        r = True
    else:
        r = False

    if flag and r:
        counter = 1

    return counter


def main():
    counter = 0
    for i in range(10000):
        counter += sim()
    print(counter / 10000)


main()
