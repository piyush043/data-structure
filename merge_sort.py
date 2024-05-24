def merge_sort(A):
  merge_sort_f(A, 0, len(A) - 1)

def merge_sort_f(A, first, last):
    print ("Calling merge_sort_f(A, {}, {})".format(first, last))
    if first< last:
        middle = (first+last)//2
        merge_sort_f(A, first, middle)
        merge_sort_f(A, middle+1, last)
        merge(A, first, middle, last)

def merge(A, first, middle, last):
    print ("Calling merge(A, {}, {}, {})".format(first, middle, last))
    L = A[first: middle+1]
    R = A[middle+1: last+1]
    L.append(123123123123)
    R.append(123123123123)
    i=j=0
    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1


A = [17, 87, 6, 22, 41, 3, 13, 54]
merge_sort(A)
print (A)