# Failed to solve in time.

def factors(num):
    original_num = num
    factors = set()
    current_factor = 2

    while num != 1 and current_factor <= original_num ** 0.5 :
        if num % current_factor == 0:
            factors.add(current_factor)
            num //= current_factor
        else:
            current_factor += 1

    if num != 1: factors.add(num)
    
    return factors

test = int(input())

for _ in range(test):
    piles, x = list(map(int,input().split()))
    coins = list(map(int, input().split()))
    possible_answer_list = [0]

    prime_x = factors(x)

    for i in prime_x:
        possible_answer = 0
        for j in coins:
            if j % i == 0: possible_answer += j
        possible_answer_list.append(possible_answer)

    print(max(possible_answer_list))


# [Key Idea]
# x is updated as gcd(x, a[i]), so x can only become a divisor of its previous value.
# Therefore, any prime factor that survives until the end must have been contained
# in every pile we chose.
#
# Instead of simulating how x changes, choose a prime factor p of the initial x
# that will survive until the end.
#
# If a[i] is divisible by p, we can eventually take all coins from that pile
# while keeping p as a factor of x.
# Therefore:
#
# answer = max(
#     sum of a[i] divisible by p
#     for each distinct prime factor p of x
# )
#
# Important perspective:
# Don't simulate states from top to bottom.
# Think backward from the final invariant:
# "Which prime factor must survive until the end?"


# [Prime Factorization]
# Naive trial division up to num can take O(num) time and cause TLE,
# especially when num itself is a large prime.
#
# To factor num efficiently, we only need to test divisors up to sqrt(num).
# If num is composite, at least one of its factors must be <= sqrt(num).
# After checking up to sqrt(num), if num > 1, the remaining num is itself prime.
#
# Use // instead of /:
#   /  -> floating-point division
#   // -> integer division
#
# Only DISTINCT prime factors are needed, so use a set.


# [Complexity]
# Let k = number of distinct prime factors of x.
#
# Prime factorization: O(sqrt(x))
# Checking all piles for every prime factor: O(n * k)
#
# Total: O(sqrt(x) + n * k)
# k is very small in practice.


# Optimization note:
# Prefer:
#     current_factor * current_factor <= num
# over:
#     current_factor <= original_num ** 0.5
#
# Because num becomes smaller as factors are removed.
# Using the current num lets the factorization terminate earlier.
# Also, integer multiplication avoids unnecessary floating-point sqrt calculations.