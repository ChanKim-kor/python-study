motors = {
    "Motor_A" : {
        "Power" : 15,
        "Voltage" : 380,
        "Efficiency" : 0.92
    },
    "Motor_B" : {
        "Power" : 22,
        "Voltage" : 380,
        "Efficiency" : 0.94
    }
}

print(f"Output voltage of Motor_A : {motors["Motor_A"]["Voltage"]}V")
print(f"Efficiency of Motor_B = {motors["Motor_B"]['Efficiency']}")

# 처음에 잘못 작성한 코드:
# for motor in motors:
#     print(f"{motor}, power = {motor['Power']}")
#
# for motor in motors 에서 motor에는 dictionary의 key가 들어간다.
# 즉 motor == "Motor_A" 또는 "Motor_B".
# 따라서 motor["Power"]는 문자열에 "Power"로 접근하려는 형태가 되어 잘못된 코드이다.

# .items()를 사용하면 key와 value를 동시에 받을 수 있다.
for motor_name, motor_info in motors.items():
    print(f"{motor_name}, power = {motor_info['Power']} kW")