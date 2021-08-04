from lab_9 import *
from threading import Thread
import socket
import os

id = 1
port = 35000
server_host = "127.0.0.1"

class FileManagementServer(Thread):
    def __init__(self):
        global id
        Thread.__init__(self)
        self.id = id
        id += 1
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.input_file = ""
        self.output_file = ""
        self.input_client_id = 0


    def run(self):
        print("Started Server No. ", self.id)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((server_host, port))
        
        if not(os.path.exists("Server_Input")):
            os.mkdir("Server_Input")
        while True:
            self.sock.listen(5)
            self.clientsocket, self.client_addr = self.sock.accept()
            client_id = self.clientsocket.recv(1024).decode('utf-8')
            self.input_client_id = client_id
            self.clientsocket.send("ID Received".encode('utf-8'))
            self.input_file = "Server_Input/input_thread" + self.input_client_id + ".txt"
            self.output_file = "Output/output_thread" + self.input_client_id + ".txt"
            data = self.clientsocket.recv(1024*1024)
            f = open(self.input_file,'wb')
            f.write(data)
            f.close()
            file_t = FileThread(self.input_client_id)
            file_t.daemon = True
            file_t.start()
            file_t.join()
            output = open(self.output_file, 'rb')
            self.clientsocket.send(output.read())
            output.close()

    
    



threads = []
for i in range(3):
    t = FileManagementServer()
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()
        
