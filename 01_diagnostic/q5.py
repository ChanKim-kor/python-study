equipment = {
    "Motor_A": 15,
    "Motor_B": 22,
    "Pump": 7.5,
    "Fan": 5.5
}

for i in equipment:
    print(f"{i} : {equipment[i]} kW")

print(f"total rated power: {sum(equipment.values())} kW")