equipment = {
    "Motor_A": 15,
    "Motor_B": 22,
    "Pump": 7.5,
    "Fan": 5.5
}

for i in equipment:
    print(f"{i} : {equipment[i]} kW")

print(f"total rated power: {sum(equipment.values())} kW")

"""chatGPT's note
for name, power in equipment.items(): #In this way, you can iterate over both the keys and values of the dictionary at the same time.
    print(f"{name}: {power} kW")


print(f"Total rated power: {sum(equipment.values())} kW")
"""