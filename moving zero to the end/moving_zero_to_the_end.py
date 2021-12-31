def move_zeros(array):
    a=array
    count = 0
    for i in a:
        if i == 0:
            count += 1
    for i in range(count):
        a.remove(0)
        a.append(0)
    return a

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
