#TLE. Solved with chatGPT after the contest

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    print_order = input()
    waiting_stack= list()
    i = 1
    printed = [False] * (n + 1)

    for s in print_order:
        if s == "1":
            waiting_stack.append(i)
        elif (len(waiting_stack) != 0) and s == "2":
            document = waiting_stack.pop()
            printed[document] = True
        else:
            printed[i] = True
        i += 1

    not_printed = [
        j for j in range(1, n + 1)
        if not printed[j]
    ]

    print(len(not_printed))
    print(*not_printed)


# ============================================================
# Codeforces 2275B - Did Not Go to Print
# Topics: Stack, Boolean Array, Time Complexity,
#         enumerate(), Truthiness
# ============================================================

# [1. Key Idea: Stack (LIFO)]
# A stack follows LIFO (Last In, First Out).
# The most recently added element is removed first.
#
# Command "1": Add the current document to the waiting stack.
# Command "2": Print and remove the top document if available.
#              Otherwise, print the current document.
# Command "3": Print the current document immediately.
#
# Python list supports stack operations:
#   stack.append(x)  -> Push x onto the stack. Amortized O(1).
#   stack.pop()      -> Remove and return the last element. O(1).
#   stack[-1]        -> Access the last element. O(1).
#
# Avoid list.pop(0), which requires O(n) element shifting.


# [2. Boolean Array: Mark Instead of Remove]
# We only need to know which documents have been printed.
# Physically removing documents from a list is unnecessary.
#
# printed = [False] * (n + 1)
#
# printed[i] = True   -> Document i has been printed. O(1).
# printed[i] = False  -> Document i has not been printed.
#
# Index 0 is unused because document numbers start from 1.
# Iterate through indices 1 to n to collect unprinted documents.
# This also guarantees that the output is in ascending order.


# [3. Lessons from TLE: Data Structure Complexity]
# First attempt:
#   waiting_set = set()
#   max(waiting_set)         -> O(m)
#   waiting_set.remove(x)   -> Average O(1)
#
# A set is not sorted, so max() must inspect all elements.
# Repeated max() calls can cause O(n^2) time complexity.
#
# Second attempt:
#   waiting_stack = []
#   answer_list.remove(x)   -> O(m)
#
# list.remove(x) searches for the value and shifts elements.
# Repeating this operation can also cause O(n^2) complexity.
#
# Final solution:
#   waiting_stack.pop()     -> O(1)
#   printed[x] = True       -> O(1)
#
# Important lesson:
# Choose data structures based on REQUIRED OPERATIONS,
# not simply because a particular structure seems fast.


# [4. enumerate(): Index + Value]
# enumerate(iterable, start=0) provides an index and value
# during iteration.
#
# Example:
#   a = [10, 20, 30]
#   for i, value in enumerate(a, start=1):
#       print(i, value)
#
# Output:
#   1 10
#   2 20
#   3 30
#
# Without enumerate(), we would need to manage i manually.
#
# In this problem:
#   for i, command in enumerate(print_order, start=1):
#
# i       -> Current document number (starting from 1).
# command -> Current command character.
#
# enumerate() is especially useful when both the index
# and the element value are needed.
# Iterating through all n elements takes O(n) total time.


# [5. Truthiness: Implicit Boolean Conversion]
# Python evaluates objects as True or False in conditions.
#
# Falsy examples:
#   0, 0.0, None, "", [], {}, set(), False
#
# Truthy examples:
#   5, -1, "hello", [0], {1}, True
#
# For a list:
#   bool([])       -> False
#   bool([1, 2])   -> True
#
# These conditions are equivalent:
#   if len(waiting_stack) != 0:
#   if bool(waiting_stack):
#   if waiting_stack:
#
# Prefer:
#   if waiting_stack:
#
# To check whether a stack is empty:
#   if not waiting_stack:
#
# Be careful: if value: tests truthiness, not specifically
# whether value is equal to True.


# [6. Output and Edge Cases]
# - Command "2" with an empty stack prints the current document.
# - Command "2" with a nonempty stack prints an older document.
# - Command "3" always prints the current document.
# - Documents left in the stack may remain unprinted.
# - All unprinted document numbers must be output in order.
# - If no documents remain, print 0 and an empty second line.
#
# Example:
#   not_printed = [
#       i for i in range(1, n + 1) if not printed[i]
#   ]
#   print(len(not_printed))
#   print(*not_printed)


# [7. Final Complexity]
# Let n be the number of documents.
#
# Processing all commands: O(n)
# Collecting unprinted documents: O(n)
#
# Total Time Complexity:  O(n)
# Total Space Complexity: O(n)
#
# Key takeaway:
# Even a single loop can become O(n^2) if it repeatedly
# calls O(n) operations such as max(set) or list.remove().
#
# Before coding:
# 1. Identify the operations required by the problem.
# 2. Choose suitable data structures.
# 3. Estimate the complexity of each operation.
# 4. Calculate the total worst-case time complexity.
