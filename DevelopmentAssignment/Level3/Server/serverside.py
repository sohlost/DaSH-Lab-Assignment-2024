import socket
import json
from datetime import datetime
from openai import OpenAI
import threading

aiclient = OpenAI()
mdl = "gpt-4o-mini"

def handle_client(client_socket, address, clients):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            promptobj = json.loads(data)
            ClientID = promptobj['client_id']
            prompt = promptobj['prompt']
            timesent = datetime.now().timestamp()
            response = aiclient.chat.completions.create(
                model=mdl,
                messages=[
                    {"role": "system", "content": "answer in 2-3 lines"},
                    {"role": "user", "content": prompt}
                ]
            )
            timereceived = datetime.now().timestamp()
            
            obj = {
                "ClientID": ClientID,
                "Prompt": data,
                "Response": response.choices[0].message.content,
                "TimeSent": timesent,
                "TimeRecvd": timereceived,
                "Source": mdl
            }
            
            response_data = json.dumps(obj)
            for client in clients:
                client.send(response_data.encode('utf-8'))
        except Exception as e:
            print(f"Error handling client {address}: {e}")
            break
    
    client_socket.close()
    clients.remove(client_socket)

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    clients = []
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"New connection from {address}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address, clients))
        client_thread.start()

if __name__ == "__main__":
    start_server('promptserver', 5000)




