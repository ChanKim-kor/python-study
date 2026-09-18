itr = int(input("To what number do you want to sum from 1?: "))
sum = 0
for i in range (1, itr + 1):
    sum += i

print(f"The sum from 1 to {itr} is {sum}.")