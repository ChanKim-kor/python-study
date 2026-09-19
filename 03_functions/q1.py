def calculate_motor_load(rated_power, load_factor, efficiency) :
    output_power = rated_power * load_factor
    input_power = output_power / efficiency

    return output_power, input_power

rated_power = 15     # kW
load_factor = 0.8
efficiency = 0.92

output_power, input_power = calculate_motor_load(rated_power, load_factor, efficiency)

print(f"Output power: {output_power:.2f} kW \nInput power: {input_power:.2f} kW")

# [복습 포인트]
#
# 1. 함수는 여러 값을 반환할 수 있다.
# return a, b
# → 실제로는 (a, b) 형태의 tuple을 반환한다.
#
# 2. 반환된 tuple은 unpacking할 수 있다.
# x, y = function()
#
# 3. float는 이진 부동소수점으로 저장되므로
# 일부 소수는 긴 자릿수로 표시될 수 있다.
#
# 4. 출력할 소수 자릿수는 f-string으로 조절 가능하다.
# f"{value:.2f}" → 소수점 아래 2자리
# f"{value:.3f}" → 소수점 아래 3자리
#
# 5. round(value, 2)는 실제 숫자를 반올림하고,
# f"{value:.2f}"는 출력 형식만 바꾼다.