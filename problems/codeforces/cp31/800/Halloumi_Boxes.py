test_case = int(input())

for _ in range(test_case):
    arr_length, sub_arr_length = list(map(int, input().split()))
    given_list = list(map(int, input().split()))
    given_list_original = given_list.copy()

    is_sorted = False

    given_list.sort()

    if given_list_original == given_list:
        is_sorted = True

    if is_sorted == True:
        print("YES")
        continue

    if sub_arr_length == 1:
        print("NO")
    else:
        print("YES")