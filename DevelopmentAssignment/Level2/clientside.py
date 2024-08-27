import socket
import json
import sys
import os

def start_client(host,port,input_file,output_file):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")
    with open(input_file, 'r') as file:
        input_lines = file.readlines()
    for line in input_lines:
        client_socket.send(line.encode('utf-8'))
        data = client_socket.recv(4096).decode('utf-8') 
        obj = json.loads(data)
        with open(output_file,'a') as file:
            json.dump(obj, file, indent=4)
    client_socket.close()    
    


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 clientside.py <host> <port>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    start_client("localhost", 5000, input_file, output_file)

   
