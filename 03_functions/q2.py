def calculate_three_phase_power(voltage, current, power_factor = 1.0, efficiency = 1.0):
    input_power = 3 ** 0.5 * voltage * current * power_factor / 1000    # kW
    output_power = input_power * efficiency

    return input_power, output_power

print("input power [kW] | output power [kW]")

input_power, output_power = calculate_three_phase_power(voltage = 380, current = 100)
print(f"     {input_power:.2f},           {output_power:.2f}")

input_power, output_power = calculate_three_phase_power(voltage = 380, current = 100, power_factor=0.9)
print(f"     {input_power:.2f},           {output_power:.2f}")

input_power, output_power = calculate_three_phase_power(voltage = 380, current = 100, power_factor=0.9, efficiency=0.92)
print(f"     {input_power:.2f},           {output_power:.2f}") 

# [복습 포인트]
#
# 1. parameter와 argument
# def func(x):   → x는 parameter
# func(10)       → 10은 argument
#
# 2. positional argument
# func(380, 100)
# → parameter의 위치(순서)에 따라 값이 전달된다.
#
# 3. keyword argument
# func(voltage=380, current=100)
# → parameter 이름을 직접 지정해서 값을 전달한다.
# → 숫자가 많은 함수에서는 의미가 명확해진다는 장점이 있다.
#
# 4. default parameter
# def func(power_factor=1.0):
# → argument를 생략하면 1.0을 사용한다.
# → 값을 전달하면 default 대신 전달된 값을 사용한다.
#
# 5. 함수 정의 시 일반적으로
# 필수 parameter를 먼저 쓰고 default parameter를 뒤에 쓴다.
#
# 6. positional argument와 keyword argument를 같이 사용할 경우
# positional argument가 먼저 와야 한다.
#
# 7. return a, b는 실제로 (a, b) tuple을 반환하며
# x, y = func() 형태로 unpacking할 수 있다.
#
# 8. f-string
# {value:.2f}     → 소수점 아래 2자리
# {value:10.2f}   → 전체 폭 10칸 + 소수점 아래 2자리