import socket
import threading
import random
import time

import numpy as np
from scipy.optimize import fsolve

clients = []
lambd = {}
gamma = {}
g = {}


def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 65432)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('Waiting for a connection...')

    while True:
        # Accept a connection
        connection, client_address = server_socket.accept()
        recalc_graph_power_transmits()
        threading.Thread(target=handle_client, args=(connection, client_address)).start()
        print('Connected to', client_address)


def handle_client(connection, client_address):
    # Store client information with timestamp and other data
    clients.append({'address': client_address, 'connection': connection, 'join_time': time.time()})
    print(f"New client joined from {client_address}.")


    # Handle receiving and sending messages
    try:
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Received from {client_address}: {data.decode()}")
                message = input("Server: ")  # Prompt server for a reply
                connection.sendall(message.encode())  # Send server's reply
            else:
                print(f"Connection closed by {client_address}.")
                break
    finally:
        connection.close()
        print(f'Connection closed with {client_address}.')
        remove_client(client_address)
        recalc_graph_power_transmits()


def recalc_graph_power_transmits():
    # For each pair of connected clients, calculate a random "channel gain"
    if len(clients) < 2:
        return  # No pairs to calculate

    print("Calculating channel gains between connected clients:")
    for i in range(len(clients)):
        lambd[i] = 1
        gamma[i] = 1
        for j in range(i + 1, len(clients)):
            client1 = clients[i]
            client2 = clients[j]
            # Calculate a simple "channel gain" based on random values or any other metric
            gain = random.uniform(0, 1)  # Simulated channel gain between 0 and 1
            g[i, j] = gain
            print(f"Channel gain between {client1['address']} and {client2['address']}: {gain:.3f}")

    N = len(clients)
    sigma2 = 1
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
        print(f"p[{i}]^2 + lambda[{i}] * p[{i}] = {p_sol_rounded[i] ** 2 + lambd[i] * p_sol_rounded[i]:.3f}")


def remove_client(client_address):
    # Remove a client when disconnected
    global clients
    clients = [client for client in clients if client['address'] != client_address]


start_server()
