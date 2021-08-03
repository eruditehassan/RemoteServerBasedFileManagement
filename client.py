from threading import Thread
import socket
import os

id = 1
port = 35000
server_host = "192.168.100.12"

class FileManagementClient(Thread):
    def __init__(self):
        global id
        Thread.__init__(self)
        self.id = id
        id += 1
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.input_file = "input_thread" + str(self.id) + ".txt"
        self.output_file = "Client_Output/client_output" + str(self.id) + ".txt"

    def run(self):
        print("Started Client No. ", self.id)
        if not(os.path.exists("Client_Output")):
            os.mkdir("Client_Output")
        self.sock.connect((server_host,port))
        id_message = str(self.id).encode('utf-8')
        self.sock.send(id_message)
        message = self.sock.recv(1024).decode('utf-8')
        f = open(self.input_file, 'rb')     
        self.sock.send(f.read())
        f.close()
        data = self.sock.recv(1024*1024)
        output = open(self.output_file, 'wb')
        output.write(data)
        output.close()
        

threads = []
for i in range(3):
    t = FileManagementClient()
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()