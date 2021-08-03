# Remote Server Based File Management System
Remote Server Based Operating System Level File Management System

## File Management System Description
The implemented system is a file management system. It uses a single data.dat file as a main directory which further consists of small files, which are created by user. For example, if Data.dat file is of 1000 bytes i.e. 1KB. The file is further divided into 10 tracks with size of 100 bytes each.
We implemented a tree data structure to keep records of files in a directory. Data.dat file will be parent node of the tree. This is done by using anytree library of python. When a file named file1.txt is created, it will be stored in first track which ranges from 1st byte to 100th byte (index position 0 to 99). If another file is created, it will be stored in succeeding track i.e. 2nd track. When more content is to be added into file1.txt, it will be look for next available track, for example the 3rd track.
