A = [1, 3, 4, 7, 5, 4, 8]


def bubblesort(A):
    repeat = True
    while repeat:
        repeat = False
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                A[i - 1], A[i] = A[i], A[i - 1]
                repeat = True
            print(A)

        print("\nEnd of inner loop \n", A)


A = [5, 7, 8, 4, 9, 2]


def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(i - 1, -1, -1):
            print("i:{} j:{} {}".format(i, j, A))
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break


insertion_sort(A)
