currents = [12.5, 15.2, 9.8, 20.1, 18.4]
avg = sum(currents) / len(currents)
max_current = max(currents)
num_above_avg = 0

for i in range (len(currents)):
    if currents[i] > avg:
        num_above_avg += 1

print(f"Maximum current: {max_current}A")
print(f"Average current: {avg}A")
print(f"Number above average: {num_above_avg}")
