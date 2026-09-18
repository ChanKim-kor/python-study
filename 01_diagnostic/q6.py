def three_phase_power(voltage, current, power_factor):
    return 3 ** (1/2) * voltage * current * power_factor / 1000

voltage = 380
current = 100
power_factor = 0.9

print(f"{three_phase_power(voltage, current, power_factor)} kW")