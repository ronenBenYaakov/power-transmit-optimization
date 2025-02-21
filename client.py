import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 65432)
client_socket.connect(server_address)

try:
    while True:
        message = input("Client: ")  # Prompt client for a message
        if message.lower() == 'exit':
            print("Closing connection.")
            break
        client_socket.sendall(message.encode())  # Send message to server

        # Receive server's response
        data = client_socket.recv(1024)
        print(f"Server: {data.decode()}")

finally:
    client_socket.close()
    print('Connection closed.')
