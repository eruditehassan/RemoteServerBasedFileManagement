from threading import Thread
import socket
import os

id = 1
port = 35000
server_host = "127.0.0.1"
operation_status = {}
file_operations = {}

class FileManagementClient(Thread):
    def __init__(self):
        global id
        Thread.__init__(self)
        self.id = id
        id += 1
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.input_file = "input_thread" + str(self.id) + ".txt"
        self.output_file = "Client_Output/client_output" + str(self.id) + ".txt"
        self.files_set = set()
        self.stop_thread = False

    def run(self):
        global operation_status
        print("Started Client No. ", self.id)
        self.file_parser()
        self.file_operations_counter()
        if (self.stop_thread == True):
            raise SystemExit() 
        # 1 means operation is started but not yet completed
        if not(os.path.exists("Client_Output")):
            os.mkdir("Client_Output")
        if len(self.files_set) > 5:
            cond = all(x == 0 for x in operation_status.values())
            while (cond != True):
                cond = all(x == 0 for x in operation_status.values())
        operation_status[self.id] = 1
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
        operation_status[self.id] = 0

    def file_parser(self):
        f = open(self.input_file)
        commands = f.read().split('\n')
        f.close()
        for command in commands:
            com_split = command.split()
            if len(com_split) == 1:
                continue
            self.files_set.add(com_split[1])
            
    def file_operations_counter(self):
        f = open(self.input_file)
        commands = f.read().split('\n')
        for command in commands:
            com_split = command.split()
            if len(com_split) == 1:
                continue
            if (com_split[0]) in ["read_from_file","write_to_file"]:
                if (com_split[1] in file_operations):
                    if file_operations[com_split[1]] == 3:
                        self.stop_thread = True
                        break
                    file_operations[com_split[1]] += 1
                else:
                    file_operations[com_split[1]] = 1




        

threads = []
for i in range(3):
    t = FileManagementClient()
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()