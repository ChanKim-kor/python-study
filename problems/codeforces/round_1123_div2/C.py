# Failed to solve in time.

def factors(num):
    original_num = num
    factors = set()
    current_factor = 2

    while num != 1 and current_factor <= original_num ** 0.5 :
        if num % current_factor == 0:
            factors.add(current_factor)
            num //= current_factor
        else:
            current_factor += 1

    if num != 1: factors.add(num)
    
    return factors

test = int(input())

for _ in range(test):
    piles, x = list(map(int,input().split()))
    coins = list(map(int, input().split()))
    possible_answer_list = [0]

    prime_x = factors(x)

    for i in prime_x:
        possible_answer = 0
        for j in coins:
            if j % i == 0: possible_answer += j
        possible_answer_list.append(possible_answer)

    print(max(possible_answer_list))