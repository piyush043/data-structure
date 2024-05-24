def quick_sort(A):
  length = len(A)
  if length <= 1:
    return A

  pivot = A.pop()

  items_left, items_right = [], []

  for item in A:
    if item > pivot:
      items_right.append(item)
    else:
      items_left.append(item)

  return quick_sort(items_left) + [pivot] + quick_sort(items_right)

A = [17, 6, 5, 3, 22, 41, 54, 29, 13]

print (A)

A = quick_sort(A)

print (A)
