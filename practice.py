


# ---------------------------------------
# Quick Sort
# ---------------------------------------

def quick_sort(A):
    length = len(A)
    if length <=1:
        return A

    pivot = A[length - 1]
    del A[length - 1]
    items_left = []
    items_right = []

    for item in A:
        if item <= pivot:
            items_left.append(item)
        else:
            items_right.append(item)

    return quick_sort(items_left) + [pivot] + quick_sort(items_right)


# A = [5, 9, 1, 2, 4, 8, 6, 3, 7]
A = [17, 6, 5, 3, 22, 41, 54, 29, 13]
print(A)
A = quick_sort(A)
print(A)


def binary_search(A, val):
    start_index = 0
    end_index = len(A) - 1

    while start_index <= end_index:
        mid_index = end_index // 2
        mid = A[mid_index]
        if val == mid:
            return mid_index
        elif val < mid:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    return None


binary_search(A, 23)