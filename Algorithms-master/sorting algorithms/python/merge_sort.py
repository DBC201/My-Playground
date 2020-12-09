def main(L):
    if len(L) > 1:
        middle = len(L)//2
        A = L[:middle]
        B = L[middle:]
        main(A)
        main(B)
        merge(L ,A, B)


def merge(L, A, B):
    index_l = 0
    index_a = 0
    index_b = 0
    while index_a < len(A) and index_b < len(B):
        if A[index_a] > B[index_b]:
            L[index_l] = B[index_b]
            index_b += 1
        else:
            L[index_l] = A[index_a]
            index_a += 1
        index_l += 1
    while index_a < len(A):
        L[index_l] = A[index_a]
        index_a += 1
        index_l += 1
    while index_b < len(B):
        L[index_l] = B[index_b]
        index_b += 1
        index_l += 1

