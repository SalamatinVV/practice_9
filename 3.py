from random import randint

list = [randint(0, 100) for i in range(100)]
list.sort()
print(list)


def binary_search_recursion(lst, val):
    import time
    start_time = time.time()
    left = 0
    right = len(lst) - 1
    m = (left + right) // 2
    if (val == lst[m]):
        return m + 1
    if (val > lst[m]):
        return binary_search_recursion(lst[m + 1:], val) + (m + 1)
    return binary_search_recursion(lst[:m], val)


print(binary_search_recursion(list, 7))
