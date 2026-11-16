n = int(input("Enter number of items: "))

w = []
p = []

for i in range(n):
    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))
    w.append(weight)
    p.append(profit)

capacity = int(input("Enter knapsack capacity: "))

dp = [[0] * (capacity + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, capacity + 1):

        if w[i-1] <= j:
            dp[i][j] = max(p[i-1] + dp[i-1][j-w[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print("Maximum Profit:", dp[n][capacity])

# 4. Short Explanation
# 0/1 Knapsack is a problem in which we select items to maximize profit without exceeding the given capacity.
# - Each item has a weight and profit.
# - We can either take the complete item (1) or leave it (0).
# - We cannot divide an item.
# - Dynamic Programming stores previously calculated results in a table.
# - It selects the combination that gives maximum profit.
# 5. Time and Space Complexity
# Let:
# - n = Number of items
# - W = Knapsack capacity
# Complexity	Value
# Time Complexity	O(n × W)
# Space Complexity	O(n × W)


# 6. Short Viva Questions
# Q1. What is 0/1 Knapsack?
# It is an optimization problem where each item is either selected or rejected.