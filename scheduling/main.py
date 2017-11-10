from fcfs import *
from sjf import *
from rr import *

file = open("teste.txt", "r")
arr = file.readlines()
x = []
for element in arr:
    x.append(element.split(" "))
arr = []
for element in x:
    dupla = [int(element[0]), int(element[1])] 
    arr.append(dupla)

fcfs(arr[:])
sjf(arr[:])
rr(arr[:], 2)