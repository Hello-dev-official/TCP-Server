import socket
import threading

IP = '10.0.2.15'
PORT = 9998


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT)) # We tell the server which port and IP we want the server to listen on
    server.listen(5) # We tell the start to start listening with a que time of 5seconds
    print(f'[*] Listening on {IP}:{PORT}') # Tells you the server IP and port number that the server is listening on

    while True:
        client, address = server.accept() #We are telling the server to accept all clients. We receive the client socket in the client variable and the remote connection details on the address variable
        print(f"[*] Established connection from {address[0]}:{address[1]}") # If the connections a sucess we get this message.
        client_handle = threading.Thread(target=handle_client, args = (client,)) # We do this to handle the clients connection
        client_handle.start() # We then execute it


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'You have successfully connected to the server')#Sends a message to the client


if __name__ == '__main__':
    main()
