import random, merge_sort, quick_sort
def selection_sort(L):
    A = list(L)
    for picked_index in range(len(A)):
        for testing_index in range(picked_index+1,len(A)):
            if A[testing_index] < A[picked_index]:
                A[testing_index],A[picked_index] = A[picked_index],A[testing_index]
    return A

def bubble_sort(L):
    A = L[:]
    length = len(A)
    while True:
        swaps = 0
        for index in range(length-1):
            if A[index] > A[index+1]:
                A[index],A[index+1] = A[index+1],A[index]
                swaps += 1
        if swaps == 0:
            break
    return A

def insertion_sort(L):
    A = L[:]
    length = len(A)
    for index in range(1,length):
        while index >= 1  and A[index-1] > A[index]:
            A[index-1], A[index] = A[index], A[index-1]
            index -= 1
    return A

if __name__ == "__main__":
    array = [random.randint(0,100) for x in range(10)]
    A = array[:]
    quick_sort.main(A,0, len(A)-1)
    print(A)
    print(array)