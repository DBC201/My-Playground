def main(A, start, stop):
    if start < stop:
        pivot_index = partition(A, start, stop)
        main(A, start, pivot_index-1)
        main(A ,pivot_index+1, stop)

def partition(A, start, stop):
    pivot = A[stop]
    partitioned_index = start
    for picked_index in range(start, stop):
        if A[picked_index] <= pivot:
            A[picked_index], A[partitioned_index] = A[partitioned_index], A[picked_index]
            partitioned_index += 1
    A[stop], A[partitioned_index] = A[partitioned_index], A[stop]
    return partitioned_index

