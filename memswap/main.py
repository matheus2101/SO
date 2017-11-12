from fifo import *
from otm import *
from lru import *

file = open("input.txt", "r")
arr = file.readlines()

x = arr[::]
arr = []

for element in x:
    arr.append(int(element))

fifo(arr[::])
otm(arr[::])
lru(arr[::])