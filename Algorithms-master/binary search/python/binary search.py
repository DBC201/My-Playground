import random
def binary_search(array,target):
    array.sort()
    start = 0
    stop = len(array)-1
    while stop >= start:
        middle = start+((stop-start)//2)#we add start because it returns middle of n values
        if target == array[middle]:
            return middle
        elif target > array[middle]:
            start = middle + 1
        else:
            stop = middle - 1
    return -1
            
l = []
r = int(input("range of random numbers:"))
number = int(input("size of list:"))
for c in range(number):
    l.append(random.randint(0,r))
l.sort()
print(l)
t = int(input("what you want to search:"))
print(binary_search(l, t))