def binary_search(length, x):
    import time
    start_time = time.time()
    print('length=', length)
    from random import randint
    list = [randint(0, 100) for i in range(length)]
    list.sort()
    print(list)
    left = 0
    right = len(list) - 1
    while left <= right:
        m = (left + right) // 2
        if list[m] == x:
            return m + 1, time.time() - start_time
        if list[m] < x:
            left = m + 1
        elif list[m] > x:
            right = m - 1
    return False
    print('time of execution', time.time() - start_time)


print(binary_search(100, 7))
print(binary_search(1000, 7))
print(binary_search(1000000, 7))
