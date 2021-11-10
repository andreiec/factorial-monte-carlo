import math
import random

# Constants
e = 2.718281828
iterations = 100000
mean_iterations = 30

# Number to calculate the factorial for
n = math.sqrt(2)


# Gamma function
def f(t, x):
    return pow(e, -x) * pow(x, t - 1)


# Count how many numbers below and above
points_under = 0
points_above = 0

# Define values (used for square)
max_x = (n + 1) * 3.4
max_y = f(n + 1, n) + 0.1

# Total Square area to calculate ratio
total_area = max_x * max_y

# Store value for each set of iteration to calculate their average
values = []

# Do Monte Carlo multiple times and compute the average value
for mean_iteration in range(0, mean_iterations):
    # Monte Carlo iteration
    for iteration in range(0, iterations):
        # Get random value inside the defined square and check if it is under or above the curve
        rand_x, rand_y = random.uniform(0, max_x), random.uniform(0, max_y)
        if rand_y < f(n + 1, rand_x):
            points_under += 1
        else:
            points_above += 1

    # Calculate surface area under the curve from the total area and add it to the values array
    ans = points_under / iterations * total_area
    values.append(ans)

    # Reset the count
    points_under = 0
    points_above = 0

# Calculate the average value from the iterations
s = sum(values)
ans = s / mean_iterations

# Print answer
print(ans)
