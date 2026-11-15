
# Non-Recursive (Iterative) Method
def non_recursive(n):
    a, b = 0, 1

    print("Non-Recursive Fibonacci:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()


# Recursive Method
def recursive(n):
    if n <= 1:
        return n

    return recursive(n - 1) + recursive(n - 2)


# Main Program
n = int(input("Enter number of terms: "))

non_recursive(n)

print("Recursive Fibonacci:")
for i in range(n):
    print(recursive(i), end=" ")
    
    
    
# The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. It starts with 0 and 1.

# Example:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

# Formula:

# F(n) = F(n-1) + F(n-2)

# Where:
# - F(0) = 0
# - F(1) = 1
    
    
#   Explanation
# 1. Non-Recursive Method:
# - Uses a for loop.
# - Calculates the next number using the previous two numbers.
# - Time Complexity: O(n).
# - Space Complexity: O(1).

# 2. Recursive Method:
# - A function calls itself repeatedly.
# - Uses the formula F(n) = F(n-1) + F(n-2).
# - Time Complexity: O(2ⁿ).
# - Space Complexity: O(n).