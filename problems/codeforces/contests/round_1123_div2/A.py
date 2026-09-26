test_case = int(input())

for i in range(test_case):
    answer = 0

    length, char_c = list(map(str, input().split()))
    length = int(length)
    word = list(input())

    for j in range(len(word)):
        if word[j] != word[len(word) - j - 1]:
            if word[j] == char_c or word[len(word) - j - 1] == char_c:
                answer += 1
                word[j] = char_c
                word[len(word) - j - 1] = char_c
            else:
                answer += 2
                word[j] = char_c
                word[len(word) - j - 1] = char_c

    print(answer)