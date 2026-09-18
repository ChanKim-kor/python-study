itr = int(input("To what number do you want to sum from 1?: "))
sum = 0
for i in range (1, itr + 1):
    sum += i

print(f"The sum from 1 to {itr} is {sum}.")

"""chatGPT's note
sum is a built-in function in Python, so it's not recommended to use it as a variable name. You can use a different name like total or result to avoid confusion and potential issues with the built-in function.
"""
