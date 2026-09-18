currents = [12.5, 15.2, 9.8, 20.1, 18.4]
avg = sum(currents) / len(currents)
max_current = max(currents)
num_above_avg = 0

for i in range (len(currents)):
    if currents[i] > avg:
        num_above_avg += 1

print(f"Maximum current: {max_current}A")
print(f"Average current: {avg}A")

"""chatGPT's note
for current in currents:
    if current > avg:
        num_above_avg += 1

in Python, you can iterate directly over the elements of a list without needing to use an **index**. This makes the code cleaner and more readable.

num_above_avg = sum(1 for current in currents if current > average_current)
The code above is a more Pythonic way to count but for now it is not essential.
"""