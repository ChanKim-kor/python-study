test_case = int(input())

for _ in range(test_case):
    num_of_keys = int(input())
    aud_love = list(map(int, input().split()))
    answer = 0
    triad = []
    triad_dict = {}

    for i in range(0, num_of_keys - 4):
        added = aud_love[i] + aud_love[i + 2] - aud_love[i + 4]
        triad.append(added)
        triad_dict[added] = triad_dict.get(added, 0) + 1

    for i in triad_dict.values():
        answer += i * (i - 1) //2

    for i in range(0, len(triad) - 2):
        if triad[i] == triad[i + 2]:
            answer -= 1
    for i in range(0, len(triad) - 4):
        if triad[i] == triad[i + 4]:
            answer -= 1

    print(answer)


# ============================================================
# Codeforces 2275C - Unrequited Love
# Topics: Frequency Map, Dictionary, Combinations,
#         Time Complexity, Index Boundaries
# ============================================================

# [1. Key Idea: Count Equal Pairs Efficiently]
# For each starting index i, calculate:
#   triad[i] = a[i] + a[i+2] - a[i+4]
#
# We need to count pairs of equal triad values,
# excluding pairs that share an array element.
#
# Instead of comparing every pair with nested loops,
# count the frequency of each triad value.
#
# If a value appears f times, the number of unordered
# pairs formed by those occurrences is:
#   C(f, 2) = f * (f - 1) // 2
#
# Sum C(f, 2) over all distinct values.
# Then subtract equal-value pairs whose indices
# differ by 2 or 4, because their triads overlap.


# [2. Frequency Map: Dictionary / Hash Table]
# A frequency map stores how often each value appears.
#
# Example:
#   triad = [5, 3, 5, 7, 3, 5]
#   freq = {5: 3, 3: 2, 7: 1}
#
# Use a dictionary to count frequencies:
#   freq[value] = freq.get(value, 0) + 1
#
# dict.get(key, default):
#   Returns the stored value if the key exists.
#   Otherwise, returns the specified default.
#
# Python dictionaries use hash tables.
# Lookup and update take O(1) time on average.
#
# We can calculate frequencies while building triad,
# avoiding a separate traversal.
#
# To iterate through stored frequencies:
#   for count in freq.values():
#       answer += count * (count - 1) // 2


# [3. Why set() + list.count() Caused TLE]
# Attempt 1: Compare every pair using nested loops.
#   for i in range(m):
#       for j in range(i + 1, m):
#           ...
#   Time Complexity: O(m^2)
#
# Attempt 2: Build a set and count each unique value.
#   unique_values = set(triad)
#   for value in unique_values:
#       count = triad.count(value)
#
# set(triad) takes O(m) time on average.
# list.count(value) takes O(m) time because it scans
# the entire list.
#
# If there are d distinct values:
#   Total complexity = O(m + m*d)
#   Worst case (d = m): O(m^2)
#
# Also, building set(triad) inside a growing loop
# repeatedly copies all accumulated elements,
# causing O(m^2) total work.
#
# Important:
# A set supports fast membership checks,
# but it does NOT store the frequency of each element.
#
# A dictionary stores frequencies directly and avoids
# repeated full-list scans.


# [4. Overlapping Triads: Index Differences]
# Each triad starting at i uses indices:
#   {i, i+2, i+4}
#
# Two distinct triads share an array element only
# when their starting indices differ by 2 or 4.
#
# Therefore, equal-value pairs with these offsets
# must be subtracted from the combination count.
#
# Check offset 2:
#   for i in range(m - 2):
#       if triad[i] == triad[i + 2]:
#           answer -= 1
#
# Check offset 4:
#   for i in range(m - 4):
#       if triad[i] == triad[i + 4]:
#           answer -= 1
#
# Each invalid pair is subtracted exactly once.
# No nested loop is necessary.
#
# Index boundary reminder:
# Python range(stop) excludes stop.
# Accessing triad[i+d] requires i+d < m.
# Therefore, the valid range is range(m-d).


# [5. Python Concepts]
# dict.get(key, 0) -> Read a value with a default of 0.
# dict.values()     -> Iterate over dictionary values.
# x // y            -> Integer floor division.
# x / y             -> True division (returns float).
# len(triad)        -> Number of triad values, O(1).
#
# Use // when calculating integer combinations.
# Store counts as integers, not floating-point values.


# [6. Complexity Analysis]
# Let m = n - 4, where n is the number of keys.
#
# Building triad and frequency dictionary:
#   O(n) average time
#
# Counting equal-value combinations:
#   O(d), where d <= m
#
# Subtracting overlapping pairs:
#   O(n)
#
# Total Time Complexity:  O(n) on average
# Total Space Complexity: O(n)
#
# The hash table provides average-case O(1)
# dictionary operations, not a strict worst-case guarantee.


# [7. Key Lessons]
# 1. Identify the repeated operation before choosing
#    a data structure.
#
# 2. When counting equal-value pairs, consider using
#    frequencies and C(f, 2) instead of nested loops.
#
# 3. If the problem excludes specific pairs, count
#    all candidate pairs first and subtract invalid ones.
#
# 4. A loop may become O(n^2) even without nested loops
#    if it repeatedly calls O(n) operations.
#
# 5. Check index boundaries independently when using
#    multiple offsets (such as +2 and +4).
#
# 6. Analyze time complexity BEFORE implementation:
#    constraints -> operations -> complexity -> code.
#
# 7. Test small edge cases and compare against
#    a brute-force solution when possible.
#
# Most important takeaway:
# Replace repeated searches with accumulated information
# whenever the problem allows it.
