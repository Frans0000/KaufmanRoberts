import numpy as np
import matplotlib.pyplot as plt


# Function to calculate occupancy distribution and blocking probability
def calculate_block_probability(C, m, t, a_range, a_step):
    a_values = np.arange(a_range[0], a_range[1] + a_step, a_step)
    results = []

    for a in a_values:
        a_i = [(a * C) / (m * t_i) for t_i in t]  # Average traffic intensity for each class

        # Kaufman-Roberts algorithm (recursive formula)
        s = [0] * (C + 1)
        s[0] = 1

        for n in range(1, C + 1):
            sum_ = 0  # Variable to store the sum of contributions for the given value n
            for i in range(m):
                if n - t[i] >= 0:
                    sum_ += a_i[i] * t[i] * s[n - t[i]]
            s[n] = sum_ / n  # Assign the result of the sum divided by n

        sum_s = sum(s)
        p = [s[n] / sum_s for n in range(C + 1)]  # Occupancy probability

        E = []
        # Blocking probability for each class
        for i in range(m):
            sum_ = 0  # Variable to store the sum of blocking probabilities for class i
            for n in range(C - t[i] + 1, C + 1):
                sum_ += p[n]  # Summing occupancy probabilities in states where blocking is possible
            E.append(sum_)  # Add the result for class i to the list E
        results.append((a, E))

    return results


# Function to save results to a file
def save_results_to_file(filename, C, t, results):
    with open(filename, 'w') as f:
        # Header
        f.write(f"System capacity: {C}, Requested AU: {', '.join(map(str, t))}\n")
        f.write("Offered traffic per unit capacity, " + ", ".join(
            [f"Blocking probability for stream {i + 1}" for i in range(len(t))]) + "\n")

        # Main body of the file
        for a, E in results:
            f.write(f"{a:.2f}, " + ", ".join([f"{e:.6f}" for e in E]) + "\n")


# Function to create plots
def plot_block_probability(C, t, results, log_scale=False):
    a_values = [a for a, _ in results]
    for i in range(len(t)):
        E_values = [E[i] for _, E in results]
        plt.plot(a_values, E_values, label=f"Stream {i + 1}, t={t[i]}")

    plt.xlabel("Offered traffic per unit capacity")
    plt.ylabel("Blocking probability")
    plt.title(f"Blocking probability for a system with capacity {C}")
    plt.legend()

    if log_scale:
        plt.yscale('log')

    plt.grid(True)


# Example (C=20, t1=1 AU, t2=3 AU, amin=0.2, amax=1.3, astep=0.1)
C = 20
m = 2
t = [1, 3]
amin = 0.2
amax = 1.3
astep = 0.1

# Calculate blocking probability
results = calculate_block_probability(C, m, t, (amin, amax), astep)

# Save results to a file
save_results_to_file("probability_block_20.txt", C, t, results)

# Create the plot
plt.figure(1)  # Create the first figure
plot_block_probability(C, t, results)

# Another example (C=40, t1=1 AU, t2=3 AU, t3=4 AU, amin=0.2, amax=1.3, astep=0.1)
C = 40
m = 3
t = [1, 3, 4]

# Calculate blocking probability
results = calculate_block_probability(C, m, t, (amin, amax), astep)

# Save results to a file
save_results_to_file("probability_block_40.txt", C, t, results)

# Create a plot with logarithmic scale
plt.figure(2)  # Create the second figure
plot_block_probability(C, t, results, log_scale=True)

# Display both plots
plt.show()
