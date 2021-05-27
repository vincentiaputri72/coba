def bubble2(A):
    tukar = True
    while tukar:
        tukar = False
        for j in range(len(A)-1):
            if A [j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                tukar=True
    return A

A = [2,6, 9, 4]
print("bubble ascending", bubble2(A))

def bubble2(A):
    tukar = True
    while tukar:
        tukar = False
        for j in range(len(A)-1):
            if A [j] < A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                tukar=True
    return A

A = [2,6, 9, 4]
print("bubble descending", bubble2(A))