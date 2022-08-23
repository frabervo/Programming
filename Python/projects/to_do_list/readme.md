# <p style="text-align:center">Developing a to-list application</p>
Source: [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-make-a-todo-list-cli-application-using-python/)
Last access: 08/16/2022

## Requirements 
+ The running operating system: Windows
+ Python3 is installed

## Functionalities of the application 
+ Add a new task
+ Delete a task 
+ Modify a task 
+ Display the to-do list 

## Tools 
The application was developed using the Python programming language. The Python script is in the file todolist.py and a script todolist.bat is needed to run the Python script.

### todolist.bat
```
@echo off
python3 todolist.py %1 %2
```
### create a symbolic link for executable file
```mklink todolist todolist.bat```

:memo: This command must be executed with administrative privileges.

### Detailed description of the source code
#### Modules
- sys module

This module provides access to some variables used or managed by the interpreter and to functions that interact strongly with the interpreter. It is always available.
To write or read data from/to the standard streams use the underlying buffer object. For example, to write bytes to stdout, vreuse: sys.stdout.buffer.write(b'abc').
