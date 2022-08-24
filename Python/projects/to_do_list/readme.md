# <p style="text-align:center">Developing a to-list application</p>
Source: [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-make-a-todo-list-cli-application-using-python/)
Last access: 08/16/2022

## Requirements 
+ The running operating system: Linux
+ Python3 is installed

## Functionalities of the application 
+ Add a new task
+ Delete a task 
+ Modify a task 
+ Display the to-do list 

## Tools 
The application was developed using the Python programming language. The Python script is in the file todolist.py and a script todolist.bat is needed to run the Python script.

### todolist.sh
```
python todolist.py "$@"
```
### create a symbolic link for executable file
```ln -s todolist.sh todolist```

:memo: This command must be executed with administrative privileges.
## Python development environment
to create a virtual environment run this command in the directory where the code is stored.
```
python3 -m venv .todolist_env
```
this command will create a directory named ".todolist_env". This folder is hidden and can be shown with ```ls -la```. 

**activate the virtual environment**:
run this command in the directory where the code is stored:
```source .todolist_env/bin/activate```
To shorten the command, an alias can be used: ```alias activate="source ./.todolist_env/bin/activate"```
**deactivate the virtual environment**
```deactivate```

### Detailed description of the source code
#### Modules
- sys module

This module provides access to some variables used or managed by the interpreter and to functions that interact strongly with the interpreter. It is always available.
