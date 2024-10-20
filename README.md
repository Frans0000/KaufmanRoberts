# Kaufman-Roberts Algorithm for Blocking Probability

## Overview
This project implements the Kaufman-Roberts algorithm for calculating the blocking probability in multi-class telecommunication systems. The algorithm computes the occupancy distribution and the probability that a request from a particular class is blocked, considering that different classes of users may require varying amounts of system resources.

The blocking probability is a critical measure in telecommunication networks to determine how often new calls or data sessions are blocked due to insufficient resources. The Kaufman-Roberts recursive method allows for efficient computation of blocking probabilities for systems with multiple traffic classes, where each class has different resource requirements.

## Formula (Kaufman-Roberts Recurrence)
The core of the algorithm is the recurrence relation:

$p[n] = \frac{1}{n} \sum_{i=1}^{m} a_i t_i p[n - t_i]$


Where:
- $p(n)$ is the probability that exactly $n$ units of resources are occupied.
- $a_i$ is the traffic offered by class $i$.
- $t_i$ is the number of resource units required by a class $i$ user.
- $m$ is the number of traffic classes.
- $C$ is the total system capacity (in resource units).

The initial condition is:


$P(0) = 1$

This means the system starts in the fully available state with zero resources in use.

### Blocking Probability
The blocking probability for class $i$ is calculated by summing the probabilities of all system states in which a new class $i$ request cannot be accommodated:


$E_i = \sum_{n = C - t_i + 1}^{C} p(n)$


Where:
- $E_i$ is the blocking probability for class $i$.
- $C$ is the total system capacity (in resource units).
- $P(n)$ is the probability that the system is in state $n$ (i.e., $n$ units are in use).

### Algorithm

$$
\begin{cases}
    s[0] = 1, \\
    s[n] = \frac{1}{n} \sum_{i=1}^{m} a_i t_i s[n - t_i], \quad \text{dla } 1 \leq n \leq C, \\
    \text{sum} = \sum_{n=0}^{C} s[n], \\
    p[n] = \frac{s[n]}{\text{sum}}.
\end{cases}
$$

### Read more
[IBM article](https://www.ibm.com/docs/en/tnpm/1.4.4?topic=functions-kaufman-roberts-based)

[A Recursive Formula for Estimating the Packet Loss Rate in IP Networks](https://eudl.eu/pdf/10.4108/ICST.VALUETOOLS2009.8015)

[Bounding the Blocking Probabilities in Multi-rate CDMA Networks Supporting Elastic Services](https://webspn.hit.bme.hu/~telek/cikkek/fodo06g.pdf)

[Modeling of systems with overflow multi-rate traffic](https://link.springer.com/content/pdf/10.1007/s11235-008-9070-8.pdf)

## Code
This code simulates a system to compute the blocking probability for multiple traffic streams and varying levels of offered traffic. It includes functionality to calculate the occupancy distribution, save the results, and plot the blocking probability.

### Functions:
#### 1. calculate_block_probability(C, m, t, a_range, a_step):

- Calculates the blocking probability for each traffic stream in a system with capacity C, for different values of offered traffic (a).
- Uses the Kaufman-Roberts recursive algorithm to compute the occupancy distribution.
- Returns a list of blocking probabilities for each traffic stream across a range of offered traffic values.

#### 2. save_results_to_file(filename, C, t, results):

- Saves the computed blocking probabilities to a file.
- Outputs the system's capacity, requested allocation units (t), and blocking probabilities for each offered traffic value.

#### 3. plot_block_probability(C, t, results, log_scale=False):

- Plots the blocking probability as a function of offered traffic for each traffic stream.
- Optionally allows for a logarithmic scale on the y-axis.

### Sample charts

![cap20](https://github.com/user-attachments/assets/bc57ef4e-d2bf-449d-9cf0-cc2ad3531186)

![cap40](https://github.com/user-attachments/assets/aee2de64-f111-4cf4-918b-af41078326e9)



## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/Frans0000/kaufman-roberts.git
    ```


## License
No license. Use it as you wish.




