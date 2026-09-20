try:
    output_power = float(input("Please enter the output power in [kW]: "))
    input_power = float(input("Please enter the input power in [kW]: "))

    print(f"Efficiency: {output_power/input_power * 100:.2f}%")

except ValueError:
    print("Please enter a valid value")

except ZeroDivisionError:
    print("Input power cannot be ZERO")


# [복습 포인트]
#
# 1. try 블록에서 발생한 예외는
#    일치하는 except 블록에서 처리할 수 있다.
#
# 2. ValueError
#    값의 형식이 변환할 수 없는 경우 발생한다.
#    예: float("abc")
#
# 3. ZeroDivisionError
#    0으로 나누려고 할 때 발생한다.
#
# 4. int("12")는 가능하지만 int("12.5")는 ValueError가 발생한다.
#    공학적 측정값처럼 소수가 들어올 수 있다면 float()가 더 적절하다.
#
# 5. try 안에는 실제로 예외가 발생할 가능성이 있는 코드를 둔다.
#
# 6. 가능하면 except: 로 모든 오류를 잡기보다
#    ValueError, ZeroDivisionError처럼 구체적인 예외를 처리한다.