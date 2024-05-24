def find_sum(arr, total):
    mem = {}
    return find_sum_rec(arr, total, len(arr) - 1, mem)

def find_sum_rec(arr, total, i, mem):
    # print(arr, total, i, mem)
    key = f"{total}:{i}"
    if key in mem:
        return mem[key]
    if total == 0:
        result = 1
    elif total < 0:
        result = 0
    elif i < 0:
        result = 0
    elif total < arr[i]:
        result = find_sum_rec(arr, total, i-1, mem)
    else:
        result = (find_sum_rec(arr, total - arr[i], i-1, mem) +
                  find_sum_rec(arr, total, i-1, mem))
    mem[key] = result
    return result

arr = [2, 4, 6, 10]
print(find_sum(arr, 6))


def fib(i, arr=[]):
    print(i)
    if arr[i] != None:
        return arr[i]
    if i <= 2:
        result = 1
    else:
        result = fib(i-1, arr) + fib(i-2, arr)
    arr[i] = result
    return result

print(fib(35))

