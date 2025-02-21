# Solving the Power Control Problem Using the Lagrangian Method
L= 
i=1
∑
N
​
 p 
i
​
 + 
i=1
∑
N
​
 λ 
i
​
 ( 
∑ 
j

=i
​
 g 
ij
​
 p 
j
​
 +σ 
2
 
g 
ii
​
 p 
i
​
 
​
 −γ 
i
​
 )## Problem Overview

The **Power Control Problem** is a well-known problem in wireless communication systems, where the objective is to optimize the transmission power levels for each user in a network. The goal is to ensure efficient use of power while meeting specific performance requirements, such as Signal-to-Interference Ratio (SIR) and quality of service (QoS) constraints. The problem is commonly encountered in systems like cellular networks, where users' transmissions interfere with one another.

We can solve this optimization problem using the **Lagrangian Method**, a mathematical optimization technique that allows us to incorporate constraints (such as the minimum SIR for each user) into the objective function.

## Problem Setup

Consider a wireless communication network with \( N \) users. Each user transmits with power \( p_i \) where \( i \in \{1, 2, \dots, N\} \). The objective is to determine the optimal values of \( p_1, p_2, \dots, p_N \) that maximize network performance, while minimizing interference.

### Given Parameters:
- **Channel Gain Matrix**: \( g_{ii} \), representing the gain between user \( i \) and itself (the direct link), and \( g_{ij} \), the interference between user \( i \) and user \( j \).
- **Target Signal-to-Interference Ratio (SIR)**: \( \gamma_i \) for each user \( i \).
- **Noise Power**: \( \sigma^2 \).
- **Power Control Constraints**: Each user’s power \( p_i \) must be greater than zero, i.e., \( p_i \geq 0 \).

## Lagrangian Formulation

The Lagrangian \( \mathcal{L} \) for this problem is defined as:

\[
\mathcal{L} = \sum_{i=1}^{N} p_i + \sum_{i=1}^{N} \lambda_i \left( \frac{g_{ii} p_i}{\sum_{j \neq i} g_{ij} p_j + \sigma^2} - \gamma_i \right)
\]

Where:
- \( p_i \) is the power for user \( i \).
- \( \lambda_i \) is the Lagrange multiplier associated with the SIR constraint for user \( i \).
- The term inside the parentheses represents the difference between the desired and actual SIR for user \( i \).

## Objective

The objective is to minimize the total power:

\[
\min_{p_1, p_2, \dots, p_N} \sum_{i=1}^{N} p_i
\]

### Constraints
1. **SIR Constraint**: For each user \( i \), the SIR must be greater than or equal to the target value \( \gamma_i \).

\[
\frac{g_{ii} p_i}{\sum_{j \neq i} g_{ij} p_j + \sigma^2} \geq \gamma_i
\]

2. **Power Non-Negativity**: The power for each user must be non-negative:

\[
p_i \geq 0, \quad \forall i
\]

## Solving the Problem Using Newton's Method

The optimization problem can be solved iteratively using methods like **Newton-Raphson** or **Gradient Descent**. The basic steps are:
1. **Construct the Lagrangian**: Combine the objective function and constraints.
2. **Take Partial Derivatives**: Derive the first-order conditions for optimality.
3. **Solve the System of Equations**: Use numerical methods such as **fsolve** (from `scipy.optimize`) to find the optimal power values.

## Code Implementation

### Python Code

```python
import numpy as np
from scipy.optimize import fsolve

# Example data for g_ij, gamma_i, lambda_i, and sigma^2
N = 3  # Length of the vector
g = np.array([[2, 1, 0.5], [1, 2, 1], [0.5, 1, 2]])  # Example g_ij matrix (N x N)
gamma = np.array([1.5, 1.5, 1.5])  # Example gamma_i values
lambd = np.array([1, 1, 1])  # Example lambda_i values
sigma2 = 0.1  # Example sigma^2 value

# Define the system of equations for F(p, mu) where mu is a vector
def equations(vars):
    p = vars[:N]  # p is a vector of length N
    mu = vars[N:]  # mu is a vector of length N
    eqs = []

    # Add equations for the other elements of p and mu
    for i in range(N):
        eq1 = 2 * p[i] + lambd[i] - mu[i] * g[i, i] + np.sum(mu * gamma * g[i, :])  # F1(p, mu)
        eq2 = mu[i] * (g[i, i] * p[i] - gamma[i] * np.sum(g[i, :] * p) - gamma[i] * sigma2)  # F2(p, mu)
        eqs.append(eq1)
        eqs.append(eq2)

    return eqs

# Initial guesses for p and mu (ensuring p starts positive)
initial_guess = np.ones(2 * N)  # Initial guess with length 2*N (N for p and N for mu)

# Solve the system using fsolve
solution = fsolve(equations, initial_guess)
p_sol = solution[:N]
mu_sol = solution[N:]

# Ensure that p is positive
p_sol = np.maximum(p_sol, 0.001)  # Ensure p > 0, setting a minimum value for p

# Round the solution values to 3 digits after the decimal
p_sol_rounded = np.round(p_sol, 3)
mu_sol_rounded = np.round(mu_sol, 3)

# Print the rounded values of p and mu
print("p (rounded to 3 digits, p > 0):", p_sol_rounded)
print("mu (rounded to 3 digits):", mu_sol_rounded)

# Print the values of F1 and F2 at the rounded solution
eqs_values = equations(solution)
for i, eq_value in enumerate(eqs_values):
    print(f"Equation {i + 1} value:", eq_value)



![Image 1](https://github.com/user-attachments/assets/187ef753-51f6-446c-ba3e-8ab83ae296c7)
![Image 2](https://github.com/user-attachments/assets/eea8109d-f32e-460a-bf5f-c20b0c46c8cb)
![Image 3](https://github.com/user-attachments/assets/d53f313f-cc01-4c82-957a-e306fd047342)
![Image 4](https://github.com/user-attachments/assets/0f2e7846-7884-4e30-ac0e-0779d5382aee)
![Image 5](https://github.com/user-attachments/assets/18dbdd56-638d-4c34-80fb-373bff4c3702)
