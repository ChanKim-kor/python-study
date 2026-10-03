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


# Review
# - Result: AC
# - Solve time: 10m
# - Attempts: 1
#
# What was good:
# - 문제의 핵심 조건을 정확히 분리했다.
#
# Things to improve:
# - `if is_sorted == True:` 보다 `if is_sorted:`가 더 Pythonic하다.
# - 원본 보존이 목적이면 `copy() + sort()` 대신 `sorted()`도 고려할 수 있다.
#
# Key takeaway:
# - k == 1이면 배열을 실질적으로 바꿀 수 없으므로 원래 정렬 여부가 답을 결정한다.
# - k >= 2이면 필요한 정렬을 만들 수 있다.