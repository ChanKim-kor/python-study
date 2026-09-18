# The code I wrote
int1 = int(input("Enter any integer: "))
isPositive = 0
isZero = 0
isEven = 0

if int1 > 0:
    isPositive = 1
elif int1 == 0:
    isZero = 1

if int1 % 2 == 0:
    isEven = 1

if isPositive:
    print("positive")
elif isZero:
    print("zero")
else:
    print("negative")

if isEven:
    print("even")
else:
    print("odd")

""" chatGPT's note
# Python Boolean
True
False

# 비교식 자체가 Boolean을 만든다.
is_even = number % 2 == 0

# Python 변수명 스타일
is_positive
power_factor
rated_voltage
"""