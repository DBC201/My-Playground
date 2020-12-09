def insertion_sort(A):
    length = len(A)
    for c in range(length-1):
        d = c
        while d>=0 and A[d] > A[d+1]:
            temp = A[d+1]
            A[d+1] = A[d]
            A[d] = temp
            d -= 1
    return(A)

def return_duplicates(i):
    A = list(i)
    insertion_sort(A)
    duplicates = []
    length = len(A)
    for c in range(length):
        if A[c] in duplicates:
            continue
        duplicate = False
        for d in range(c+1,length):
            if A[c] == A[d]:
                duplicates.append(A[d])
                duplicate = True
        if duplicate:
            duplicates.append(A[c])
    return duplicates                
                
array = [1,1,2,2,234123,53,23,42134,3,52,3,542,323,]

print(return_duplicates(array))
