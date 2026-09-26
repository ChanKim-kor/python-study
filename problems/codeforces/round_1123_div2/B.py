test = int(input())

for _ in range(test):
    size_array = int(input())
    array = list(map(int, input().split()))
    answer = list()
    num_of_num = list()

    num_max = max(array)

    for i in range(1, num_max + 1):
        num_of_num.append(array.count(i))

    pt = num_max
    num_of_try = 0
    while num_of_try < size_array:
        if num_of_num[pt - 1] == 0:
            pt -= 1
            if pt == 0: pt = num_max
        else:
            answer.append(pt)
            num_of_num[pt-1] -= 1
            pt -= 1
            if pt == 0: pt = num_max
            num_of_try += 1

    print(*answer)