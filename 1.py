def linear_search(length, number):
    import time
    start_time = time.time()
    print('length=', length)
    from random import randint
    list = [randint(0, 2000) for i in range(length)]
    list.sort()
    print(list)
    check = 1
    for i in range(0, length):
        if list[i] == number:
            check = 1 - 1
            print('number ', number, ' is on position ', i)
    if check == 1:
        print('number ', number, ' is not exists')
    print('time of execution', time.time() - start_time)
    return '_________________________'


print(linear_search(1, 7))
print(linear_search(1000, 99))
print(linear_search(1000000, 77))
