# The code I wrote first
#
# def calculate_efficiency(output_power, input_power):
#     if (output_power <= 0) or (input_power <= 0):
#         raise ValueError("input/ouput power must be a positive value. Try again")
#     elif (output_power > input_power):
#         raise ValueError("Output power must be less than input power. Try again.")
#     efficiency = output_power/input_power
#     return efficiency

# while True:
#     try:
#         output_power = float(input("Enter the output power in [kW]: "))
#         input_power = float(input("Enter the input power in [kW]: "))
#         efficiency = calculate_efficiency(output_power, input_power)

#         print(efficiency)

#     except ValueError as error:
#         print("Please enter a valid value. Try again.")


# ChatGPT's correction. (I did not know the mechanism of how 'raise' works)
def calculate_efficiency(output_power, input_power):
    if output_power <= 0 or input_power <= 0:
        raise ValueError(
            "Input/output power must be a positive value."
        )

    if output_power > input_power:
        raise ValueError(
            "Output power must not exceed input power."
        )

    efficiency = output_power / input_power
    return efficiency


try:
    output_power = float(input("Enter the output power in [kW]: "))
    input_power = float(input("Enter the input power in [kW]: "))

    efficiency = calculate_efficiency(output_power, input_power)

    print(f"Efficiency: {efficiency * 100:.2f}%")

except ValueError as error:
    print(error)


# [복습 포인트]
#
# 1. raise는 예외를 직접 발생시킨다.
# raise ValueError("message")
#
# 2. raise가 실행되면 현재 함수는 즉시 종료된다.
#
# 3. except ValueError as error:
# 발생한 ValueError 예외 객체를 error 변수에 저장한다.
#
# 4. print(error)
# → 예외에 포함된 메시지를 출력한다.
#
# 5. error라는 변수명은 임의로 정할 수 있다.
# except ValueError as e: 도 가능하다.
#
# 6. Python이 자동으로 발생시킨 ValueError와
# 직접 raise한 ValueError 모두 같은 except에서 잡을 수 있다.
#
# 7. 함수는 잘못된 값을 발견하면 raise하고,
# 호출하는 쪽에서 except로 처리하도록 역할을 나눌 수 있다.