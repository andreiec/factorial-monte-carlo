import math
import random
import matplotlib.pyplot as plt

# Constants
e = 2.718281828
iterations = 100000
mean_iterations = 30

# Number to calculate the factorial for
n = math.pi


# Gamma function
def f(t, x):
    return pow(e, -x) * pow(x, t - 1)


# Count how many numbers below and above
points_under = 0
points_above = 0

# Define values (used for square) - See function graph to check values
max_x = (n + 1) * 3.4
max_y = f(n + 1, n) + 0.1

# Total Square area to calculate ratio
total_area = max_x * max_y

# Store value for each set of iteration to calculate their average
values = []

# Save each iteration values for plotting purposes
iteration_values = []

# Do Monte Carlo multiple times and compute the average value
for mean_iteration in range(1, mean_iterations + 1):
    # Monte Carlo iteration
    for iteration in range(1, iterations + 1):
        # Get random value inside the defined square and check if it is under or above the curve
        rand_x, rand_y = random.uniform(0, max_x), random.uniform(0, max_y)
        if rand_y <= f(n + 1, rand_x):
            points_under += 1
        else:
            points_above += 1

        # Append to iteration value array current values
        iteration_values.append((points_under, iteration))

    # Calculate surface area under the curve from the total area and add it to the values array
    ans = points_under / iterations * total_area
    values.append(ans)

    # Calculate and show last iteration plot
    if mean_iteration == mean_iterations:
        fig, ax = plt.subplots()
        ax.plot(list(map(lambda x: x[1], iteration_values)),
                list(map(lambda x: x[0] / x[1] * total_area, iteration_values)))
        ax.set(xlabel='Points', ylabel='Value', title='Approximation of ' + str(n)[:6] + " factorial")
        ax.grid()

        plt.ylim([0, 8])
        plt.show()

    # Reset the count
    points_under = 0
    points_above = 0

    # Reset plot value array
    iteration_values.clear()

# Calculate the average value from the iterations
s = sum(values)
ans = s / mean_iterations

# Print answer
print(ans)
