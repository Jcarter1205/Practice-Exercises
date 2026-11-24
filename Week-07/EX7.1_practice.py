# Jada Carter
# Novemeber 24, 2026
# Practice Exercise 7.1

import numpy as np

# Create the 3D sales array
sales = np.array([
    [
        [1200, 1500, 1800],
        [2000, 2200, 2500]
    ],
    [
        [1400, 1600, 1900],
        [2100, 2300, 2600]
    ]
])

# Task 2: Display the sales array
print("Sales Array:")
print(sales)

# Task 3: Process the array using np.nditer()
print("\nSales Records Using np.nditer():")

for amount in np.nditer(sales):
    print(amount)

# Task 4: Process the array using three nested for loops
print("\nSales Records Using Nested For Loops:")

for store in range(2):
    for month in range(2):
        for record in range(3):
            print(sales[store][month][record])

# Task 5: Calculate total sales
total = 0

for amount in np.nditer(sales):
    total += amount

print("\nTotal Sales:", total)

# Task 6: Calculate average sales
count = 0
total = 0

for amount in np.nditer(sales):
    total += amount
    count += 1

average = total / count

print("\nNumber of Sales Records:", count)
print("Average Sales: $", format(average, ".2f"))

# Task 7: Identify the highest sales amount
highest = 0

for amount in np.nditer(sales):
    if amount > highest:
        highest = amount

print("\nHighest Sales Amount: $", highest)
