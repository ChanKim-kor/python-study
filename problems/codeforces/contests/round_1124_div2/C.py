# failed to solve in time

''' code written during contest (totally wrong)
test_case = int(input())

for _ in range(test_case):
    n , k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    sum_list = list()
    if n != k:
        sum_list.append(sum(a[1 : k]))
        sum_list.append(sum(a[n  - k:n - 1]))

    print(max(sum_list) + max([a[0], a[-1]]))
'''

# After the contest

test_case = int(input())

for _ in range(test_case):
    answer = 0
    n , k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    list_must_add = list()
    list_selectional_add = list()

    if n >= 2 * k - 1:
        list_must_add = a[k - 1: n - k + 1] # len = n - 2k + 2
        answer += sum(list_must_add)
        list_selectional_add = a[0 : k - 1] + a[n - k + 1 : n] # len = (k-1) + (k-1) = 2k - 2
    else:
        list_selectional_add = a

    sel_len = len(list_selectional_add)

    if sel_len != 0:
        current_loc = k
        while current_loc <= sel_len:
            answer += max(list_selectional_add[current_loc - 1], list_selectional_add[sel_len - current_loc])
            current_loc += 1

    print(answer)

# If n >= 2k - 1, the middle n - 2k + 2 elements
# are guaranteed to be removed regardless of our choices.
#
# After removing them, 2(k - 1) elements remain.
# At each step, one fixed pair competes:
# inner pair -> next outer pair -> ... -> outermost pair.
# Therefore, take the larger value from every pair.
#
# If n < 2k - 1, there is no guaranteed middle segment.
# The same pairwise-choice logic applies directly to the whole array.