# Developing a to-list application
The purpose of this project is to create a todolist application that will run as CLI (Command Line Interface)
## Technical requirements
+ OS : Linux
+ Python3 installed
+ a Bash Shell

## Functionalities of the application
+ create a to-do list 
+ Add a new task to a given list
+ Delete a task in a given list
+ Delete a to-do list 
+ update a task in a list 
+ Display the to-do lists
+ Display task of a given to-do list 

# run the app locally
The application was developed using the Python programming language. The Python script [todolist.py](./todolist.py) content the programm code and a script [setup.py](./setup.py) (for the setuptool environment) is needed to setup the virtual environment for the application command line.

## Steps
1. define a working directory 
2. install the python virtual environment: ```python3 -m venv .todolist_env```
3. Make sure to have the following scripts:  
  + [setup.py](./setup.py)
  + [todolist.py](./todolist.py)
  + [test.py](./test.py)
   
  Just run the scripts: [pull_files.sh](./pull_files.sh). 
  Run these commands for that: 
  + ```wget -L https://raw.githubusercontent.com/frabervo/Programming/main/Python/projects/to_do_list/pull_files.sh```
  + ```bash ./pull_files.sh```
  
4. activate the python virtual environment: ```source .todolist_env/bin/activate ``` from the working directory
5. run the setup script: ```pip install --editable .```

Yet you can run the command lines of the to-do list app like ```todolist --help``` 

**uninstall the app**

steps: run all commands from the working directory 
1. deactivate the python virtual environment: ```deactivate```
2. delete files of the virtual environment: ```rm -dr ./.todolist_env```
3. delete all packages: ```rm -dr __pycache__ todolist_package.egg-info```
4. delete data: ```rm -dr ~/.todolists```

## Tools
### Python virtual environment
to create a virtual environment run this command in the directory where the code is stored.
```
python3 -m venv .todolist_env
```
this command will create a directory named ".todolist_env". This folder is hidden and can be shown with ```ls -la```. 

To shorten the command, an alias can be used: ```alias activate="source ./.todolist_env/bin/activate"```. 

write this codeline in the file .bashrc if you want to make it permanent.
#### deactivate the virtual environment
command: ```deactivate```

### Setuptools Integration
#### why the setuptools Integration?
[Setuptools](https://en.wikipedia.org/wiki/Setuptools) is a package development process library designed to facilitate packaging Python projects by enhancing the Python standard library distutils (distribution utilities). 

# Run the app in a docker container
steps: 
1. definir a working directory
2. copy the following files in the working directory
  + [setup.py](./setup.py)
  + [todolist.py](./todolist.py)
  + [test.py](./test.py)
  + [start_container.sh](./start_container.sh) in excecutable mode
  + [uninstall_docker.sh](./uninstall_docker.sh) in excecutable mode

  Just run the scripts: [pull_files.sh](./pull_files.sh). 
  Run these commands for that: 
  + ```wget -L https://raw.githubusercontent.com/frabervo/Programming/main/Python/projects/to_do_list/pull_files_docker.sh```
  + ```bash ./pull_files.sh```
  
3. pull the container image

    run the following command: ```docker pull bervo/todolist:latest```

    More informations to the image here: https://hub.docker.com/repository/docker/bervo/todolist/general

4. run the script start_container from the working directory 
    
    run the following command: ```bash ./start_container.sh```

**If you want to delete the containe**r, run the following command from the working directory: ```bash ./uninstall_docker.sh```

The previous command just delete the container but the volume and persistant data are still there. **To delete the volume and data(to-do lists)**, run the command: ```bash ./uninstall_docker.sh vol```

# Detailed description of the source code
Because a docstring was included by programming. The documentation of the can be generate automaticaly by runing the follow command in the project directory: 
```python3 ./doc_generatotor.py >> code_doc.txt``` 

This command is also in the shell script: ```./doc_generator.sh```

So the documentation of the code: ./doc_code.txt
