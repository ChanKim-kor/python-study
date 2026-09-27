# a bit hard so kept.

def next_loop(n):
    next = 0
    while n != 0:
        next += (n % 10) ** 2
        n = n // 10

    return next



test_case = int(input())


for _ in range(test_case):
    answer = 0
    num_lighthouse = int(input())
    a = list(map(int, input().split()))
    loop_list = list()

    for a_i in a:
        loop_list.append([[a_i], False])

    while True:
        flag = True

        for i in range(num_lighthouse):
            loop_list[i][0].append(next_loop(loop_list[i][0][-1]))
            if loop_list[i][0].index(loop_list[i][0][-1]) != len(loop_list[i][0]) - 1:
                loop_list[i][1] = True

        for real in range(num_lighthouse):
            if loop_list[real][1] != True:
                flag = False
                break

        if flag == True:
            break

    loop_end_list = list()

    for k in range(num_lighthouse):
        loop_end_list.append(loop_list[k][0][-1])

    loop_end_set = set(loop_end_list)

    answer_list = list()

    for loop_end in loop_end_set:
        answer_list.append(loop_end_list.count(loop_end))

    for loop_num in answer_list:
        answer += int(loop_num * (loop_num - 1) / 2)

    print(answer)