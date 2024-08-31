import socket
import json
import sys
import os
host = os.environ.get('HOSTNAME')
client_id = os.environ.get('CLIENT_ID')
input_dir=os.environ.get('INPUT_DIR')
input_file = 'input.txt'

def start_client(host, port, client_id, input_file):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    with open(input_file, 'r') as file:
        input_lines = file.readlines()

    line = input_lines[client_id-1]
    data = {
        'client_id': client_id,
        'prompt': line.strip()
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode('utf-8'))
    output_file = f"output_{client_id}.json"

    with open(output_file, 'a') as file:
        while True:
            response = client_socket.recv(1024).decode('utf-8')
            if not response:
                break
            obj = json.loads(response)
            if (obj['ClientID'] != client_id):
                obj['Source'] = "user"
            json.dump(obj, file, indent=4)
            file.write('\n')  # Add a newline after each JSON object
            print(f"Received and saved response for prompt: {line.strip()}")
            file.flush()  # Flush the file buffer to ensure data is written immediately
    
    client_socket.close()

if __name__ == "__main__":
 #   if len(sys.argv) != 3:
 #       print("Usage: python client.py <client_id> <input_file> ")
 #       sys.exit(1)
    client_id = int(client_id)
    start_client(host, 5000, client_id, input_file)
    