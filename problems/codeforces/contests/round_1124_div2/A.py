test_case = int(input())

for _ in range(test_case):
    day, withdraw = list(map(int, input().split()))

    print(2 ** (day - withdraw + 1) + 2 * (withdraw - 1))