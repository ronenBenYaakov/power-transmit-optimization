# Solving the Power Control Problem Using the Lagrangian Method

## Problem Overview

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


![Image 1](https://github.com/user-attachments/assets/187ef753-51f6-446c-ba3e-8ab83ae296c7)
![Image 2](https://github.com/user-attachments/assets/eea8109d-f32e-460a-bf5f-c20b0c46c8cb)
![Image 3](https://github.com/user-attachments/assets/d53f313f-cc01-4c82-957a-e306fd047342)
![Image 4](https://github.com/user-attachments/assets/0f2e7846-7884-4e30-ac0e-0779d5382aee)
![Image 5](https://github.com/user-attachments/assets/18dbdd56-638d-4c34-80fb-373bff4c3702)
