# Remote Server Based File Management System
Remote Server Based Operating System Level Multi Threaded File Management System

## File Management System Description
The implemented system is a file management system. It uses a single data.dat file as a main directory which further consists of small files, which are created by user. For example, if Data.dat file is of 1000 bytes i.e. 1KB. The file is further divided into 10 tracks with size of 100 bytes each.
We implemented a tree data structure to keep records of files in a directory. Data.dat file will be parent node of the tree. This is done by using anytree library of python. When a file named file1.txt is created, it will be stored in first track which ranges from 1st byte to 100th byte (index position 0 to 99). If another file is created, it will be stored in succeeding track i.e. 2nd track. When more content is to be added into file1.txt, it will be look for next available track, for example the 3rd track.

## MultiThreaaded File Management System
The system was later modified to make it a multi-threaded file management system. This system works with the help of threading library of python for creating threads and executing commands from input files in parallel manner. It is based on the previously built File management system. It parses commands and values from the input files and executes those commands with the help of values accordingly. The major benefit in this improvement is that multiple operations are performed in parallel and better performance is achieved comparatively.

## Remote Server based File Management
The current modification is the implementation of a remote server-based file management where the commands can be sent to a remote server (following the same working as the previous version), then they are processed and executed, and the output generated is sent back to the client as a confirmation of the successful execution of the commands. This system now has two additional files, `server.py` and `client.py`. The main functionality would be paired with the server.py by importing the functionality from previously done work. The client.py would have client functionality to send the commands to the remote server and then receive the output from server and store it.
The server is multi-threaded and can handle any number of clients, although the number of clients must be known in advance so that a specified number of threads are executed. Client file is also designed such that multiple threads can be run on the client.py file, so that even if a single client is connected with the server, it would do the processing in parallel way to achieve maximum performance.

## Remote server improvement: Limiting User Access to files
In this part, some minor improvements were made. The overall specification of those improvements is:
1. If a user places request for more than 5 files, then that thread must wait for the execution of other threads.
2. Each file can only be accessed by 3 users


It was accomplished by writing a parser that initially parses the number of files to which a user is requesting access to, if it is more than 5 files in a single session, then that thread is made to wait, until all the other threads have completed their execution. It is accomplished by keeping track of the completion state of all the threads at all times during the execution of the program.

The second task was also done similarly, by keeping track of the number of accesses to each file, and if it becomes equal to 3, then no thread is allowed to access that file anymore.

## System Functions and User Guide
The details of all the functionality of the system and how the user must interact with the system is given below:
- Firstly, the server.py file is run. The previously implemented functionality must be kept in the same folder as the server.py file as its functionality is built on top of the previously implemented functionality.
- For the client side, the requirement is that the input files having commands must be kept in the same directory as the client.py file, and they must be named in the following format `input_thread[x]`, where x is 1,2,3 and so on.
- The server.py must be run first, then client.py would be run. The client would automatically connect with the server and start sending the commands and receiving the output.
- The first step would be to send the input command files from client to server, these command files are received by the server and are saved in a folder.
- These command files are then fed to the functionality implemented previously to process it and the corresponding output files are generated.
- These output files are then sent to the client, which receives them and saves them.
- The output files received by clients show the output at each step of the processing and act as a log to confirm that the specified tasks were in fact performed.

## Dependencies and Libraries used
Following python libraries were used along with the purpose of use:
1. Math library was used briefly to handle a trivial calculation
2. Anytree library was obtained from pypi and a custom tree data structure was built after inheriting from the Anytree base NodeMixin class, and that tree data structure was used to keep track of the files and the memory storage locations and also for creating and visualizing a memory map.
3. Threading library used for creating threads

## Limitations of the system
The system is performing its job as desired, although there is still some room for improvement.
- The major limitation in the system is that it only works for devices working in a closed network environment, like a private network connecting various computers by LAN.
- The system can be improved to show the console output, in addition to the output file so that the client gets better insights of the working of the system.
- One more improvement could be to build a Graphical User Interface (GUI) for the client side so that the interaction is smoother.
- The system can also be improved by deploying it on some cloud platform like AWS or Azure and allowing clients from anywhere to connect to it and perform operations.


