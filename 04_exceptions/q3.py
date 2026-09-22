while True:
    try:
        output_power = float(input("Please enter the output power in [kW]: "))
        if output_power <= 0:
            print("Output power must be greater than ZERO. Try again.")
            continue

        input_power = float(input("Please enter the input power in [kW]: "))
        if input_power <= 0:
            print("Input power must be greater than ZERO. Try again.")
            continue
        if input_power < output_power:
            print("Output power cannot exceed input power. Try again.")
            continue

        print(f"Efficiency: {output_power/input_power * 100:.2f}%")
        break
    
    except ValueError:
        print("Please enter a valid value. Try again.")



# [복습 포인트]
#
# 1. continue
# 현재 반복의 나머지 코드를 건너뛰고
# 다음 반복으로 즉시 이동한다.
#
# 2. break
# 반복문 자체를 완전히 종료한다.
#
# 3. validation은 Python 오류가 아니라
# 프로그램 규칙상 허용할 수 없는 값을 검사하는 과정이다.
#
# 예:
# output_power <= 0
# input_power <= 0
# output_power > input_power
#
# 4. 잘못된 값을 계산 전에 validation으로 막으면
# ZeroDivisionError 같은 일부 예외를 애초에 발생하지 않게 할 수 있다.
#
# 5. Exception과 invalid input은 다르다.
# float("abc") → ValueError
# output_power = -10 → 계산은 가능하지만 프로그램 규칙상 잘못된 값