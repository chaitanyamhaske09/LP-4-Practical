n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight = float(input("Enter weight: "))
    profit = float(input("Enter profit: "))
    ratio = profit / weight
    items.append((ratio, weight, profit))

capacity = float(input("Enter knapsack capacity: "))

items.sort(reverse=True)

total_profit = 0

for ratio, weight, profit in items:

    if capacity >= weight:
        total_profit += profit
        capacity -= weight

    else:
        total_profit += ratio * capacity
        break

print("Maximum Profit:", total_profit)

# Fractional Knapsack is a Greedy Algorithm used to maximize profit by selecting items based on their profit-to-weight ratio.
# - Calculate the profit/weight ratio of each item.
# - Sort items in descending order of ratio.
# - Select the item with the highest ratio first.
# - If the complete item cannot fit, take a fraction of it.
# - Continue until the knapsack is full.
# 5. Time and Space Complexity
# Let n = number of items.
# Complexity	Value
# Time Complexity	O(n log n)
# Space Complexity	O(n)