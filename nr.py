import numpy as np
from scipy.optimize import fsolve

# Example data for g, gamma, lambda, and sigma^2
N = 3  # Length of the vector
g = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])  # Example g matrix (N x N)
gamma = np.array([1, 1, 1])  # Example gamma values
lambd = np.array([1, 1, 1])  # Example lambda values
sigma2 = 1  # Example sigma^2 value


# Define the system of equations for F(p, mu) where mu is a vector
def equations(vars):
    p = vars[:N]  # p is a vector of length N
    mu = vars[N:]  # mu is a vector of length N
    eqs = []

    # Add more equations for the other elements of p and mu
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

# Print p[i]^2 + p[i] for each index i
print("\np[i]^2 + p[i] for each index i:")
for i in range(N):
    print(f"p[{i}]^2 + lambda[{i}] * p[{i}] = {p_sol_rounded[i]**2 + lambd[i] * p_sol_rounded[i]:.3f}")
