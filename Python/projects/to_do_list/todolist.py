"""Modules implementation for the todolist commando line interface
 """
# modules
import json
import datetime
import os
from pathlib import Path
import sys
from termcolor import colored
import click


# Function implementation
def create_lists_dir() -> str:
    """create the directory where the to-do lists will be stored.

    this function create in der Home directory of the current user a subdirectory named .todolists

    Returns
    -------
        str: the directory name where the lists are stored
    """
    todolist_dir = str(Path.home()) + "/.todolists"     # 1. define the path of the directory in the home directory
    todolist_dir = Path(todolist_dir)                   # 2. Initialise the Path object with the path
    if todolist_dir.exists() is not True:               # 3. check if the directory already exists
        todolist_dir.mkdir(parents=True)                # 4. create the directory with all subdirectory
        click.echo(f"directory: {todolist_dir} sucessfully created\n")
    return str(todolist_dir)


def create_file(lists_dir: str, filename: str) -> int:
    """
    this function creates a file in the home directory where the task will be added

    Parameters
    ----------
    lists_dir : str
            the name of the directory where the lists are stored
    filename : str
            the name of the to-do list

    Returns
    -------
    int : the return code. 0 if the file did not exist and -1 if the file already exists
    """
    # Variables
    fle = ""                # store the path name
    # define the path of the file in home/todolists directory of the user
    if filename == "LISTS" or filename.endswith("."):  # refuse "LISTS" as listename
        click.echo(colored("the given name is not allowed", "red"))
        return -1
    fle = Path(lists_dir + "/." + filename + ".json")
    if fle.exists() is True:
        click.echo(colored(f"the to-do list : {filename} exists already!", "red"))
        return -1
    try:
        fle.touch()
    except FileNotFoundError as error:
        click.echo(colored(error, "red"))
        return -1
    return 0


def add_task(lists_dir: str, task: str, list_name: str) -> None:
    """add task to the to-do list

    This function takes the given string and inserts it as a task in the list_name. The task is assigned a date
    and a number number

    Parameters
    ----------
    lists_dir: str
            the name of the directory where the lists are stored
    task: str
        the task to be add
    list_name: str:
            the name of the to-do list
    """
    # variables
    new_tasks = {"task_number": 0, "task": "", "date": ""}
    # find the path of the list
    file_path = lists_dir + "/." + list_name + ".json"
    if Path(file_path).exists() is True:
        with open(file_path, encoding="utf8", mode="r+") as file_obj:
            # Get the content of the current list
            try:
                list_content = json.load(file_obj)
                # define the number of the current task
                new_tasks["task_number"] = len(list_content) + 1
            except json.JSONDecodeError:
                # this means there are no elements in the lists
                new_tasks["task_number"] = 1
                list_content = []           # create the array for the json file

            new_tasks["date"] = str(datetime.datetime.now()) 	# define the time when the task was added
            new_tasks["task"] = task
            list_content.append(new_tasks)          # apppend the task to json file
            # save the list --> convert from python to JSON and store in the json file
            file_obj.truncate(0)             # delete the actuel content of the file
            file_obj.seek(0)
            json.dump(obj=list_content, fp=file_obj, indent=2)
            file_obj.close()
    else:
        click.echo(colored("the to-do list doesn't exist !", "red"))


def show_list(lists_dir: str) -> None:
    """show the to-do lists

    this function show all the lists stored

    Parameters:
    lists_dir :str
            the name of the directory where the lists are stored
    """
    file_path = Path(lists_dir)
    list_name = ""          # to store the to-do list name
    for file in file_path.iterdir():
        list_name = file.name[1:]
        list_name = list_name[:-5]
        click.echo(colored(list_name, "blue"))


def show_tasks(lists_dir: str, list_name: str) -> None:
    """show the tasks of a list

    the function show the tasks of the given list name

    Parameters
    ----------
        lists_dir : str
                the name of the directory where the lists are stored
        list_name : str
                the name of the to-do list
    """
    # variables
    list_content = []

    file_path = lists_dir + "/." + list_name + ".json"
    if Path(file_path).exists() is True:
        click.echo(f"Tasks of the to-list: {list_name}")
        with open(file_path, encoding="utf8", mode="r+") as file_obj:
            list_content = json.load(fp=file_obj)
            for task in list_content:
                num = task["task_number"]
                tsk = task["task"]
                dte = task["date"]
                click.echo(f"{num}. | {tsk} | added at {dte}")
    else:
        click.echo(colored(f"the to-list: {list_name} doesn't exists", "red"))


def del_task(number: int, lists_dir: str, list_name: str) -> None:
    """delete  task

    the function delete the tasks with the number of the list: list_name

    Parameters
    ----------
        number : int
            the number of the task to be delete
        lists_dir : str
                the name of the directory where the lists are stored
        list_name : str
                the name of the to-do list
    """
    # variables
    list_content = []
    num = -1

    file_path = lists_dir + "/." + list_name + ".json"
    if Path(file_path).exists() is True:   # check if the list exits
        with open(file_path, encoding="utf8", mode="r+") as file_obj:
            list_content = json.load(fp=file_obj)           # get the array from the json file
            for task in list_content:   # go through the list
                if task["task_number"] == number:
                    num = task["task_number"]
            if num == -1:
                click.echo(f"Task: {num}  doesn't exist")
                sys.exit(1)
            list_content.pop(num - 1)
            # reorder the list
            for index, task in enumerate(list_content):
                task["task_number"] = index + 1
            # clear the to-do list
            file_obj.truncate(0)
            file_obj.seek(0)
            json.dump(list_content, fp=file_obj, indent=2)
            file_obj.close()
            click.echo(f"Task: {number}  deleted")

    else:
        click.echo(colored(f"the to-list: {list_name} doesn't exists", "red"))


def delete_list(lists_dir: str, list_name: str) -> None:
    """delete  list

    the function delete the given list

    Parameters
    ----------
        lists_dir : str
                the name of the directory where the lists are stored
        list_name : str
                the name of the to-do list
    """
    path_list = Path(lists_dir + "/." + list_name + ".json")

    if path_list.exists() is True:
        print(path_list)
        os.system(f"rm {path_list}")
        click.echo(colored(f"The to-do list: {list_name} was deleted successfully!", "green"))
    else:
        click.echo(colored(f"The to-do list: {list_name} doesn't exists", "red"))


def update_task(lists_dir: str, listname: str) -> None:
    """update a to-do list

    this function update a task in the given to-do list

    Parameters
    ----------
    lists_dir : str
            the name of the directory where the lists are stored
    listname :
            the name of the list to be update
    """
    # variable
    number = 0              # The number of the task to be update
    new_task = ""           # To store the new task
    list_path = ""           # to store the path of the list
    list_content = []        # take the content of a list with the type <list>

    list_path = Path(lists_dir + "/." + listname + ".json")
    if list_path.exists() is True:
        show_tasks(lists_dir=lists_dir, list_name=listname)
        click.echo("\n")
        try:
            # ask for the number of the task
            number = int(input("Number of the task to be updated:"))
            # check if the number exists
            with open(file=list_path, encoding="utf8", mode="r+") as file_obj:
                list_content = json.load(fp=file_obj)
                if number > len(list_content):
                    click.echo(colored(f"The number: {number} doesn't exists in the given list\n", "red"))
                    sys.exit(1)
                # The number exists
                # ask for the new message
                new_task = input(colored("Task: ", "yellow"))
                # find the element in the list
                list_content[number - 1]["task"] = new_task
                click.echo("\n")
                click.echo(colored("updated list", "blue"))
                # rewrite the to-do list (json file)
                file_obj.truncate(0)
                file_obj.seek(0)
                json.dump(obj=list_content, fp=file_obj, indent=2)
                # print the updated list
        except ValueError as error:
            click.echo(colored(error, "red"))
            sys.exit(1)
        show_tasks(lists_dir=lists_dir, list_name=listname)
    else:
        click.echo(colored(f"The to-do list: {listname} doesn't exists!"))


@click.command()
@click.option("--delete", default=0, help="delete a task --del=TASK_NUMBER")
@click.option("--add", help='to add "new task" to the task list')
@click.option("--update", help="to update a task in the given list.")
@click.option("--show", help="Display the to-do list. --show LISTS display all stored lists")
@click.option("--create", help='create a todolist')
@click.option("--del_list", help="Delete the given to-do list")
@click.argument('listname', required=False)
def main(delete, add, update, show, create, listname, del_list):
    """A todolist programm as command line
    """
    # Variables
    status = 0      # store the status code of the called functions
    # the user want to create a to do list
    dir_name = create_lists_dir()
    if create:
        status = create_file(dir_name, create)
        if status == -1:
            sys.exit(1)
    if add and listname:
        add_task(lists_dir=dir_name, task=add, list_name=listname)
    elif add and listname is not True:
        click.echo("please give the name of the list: run 'todolist --help' to get help")
    if show and show != "LISTS":
        show_tasks(lists_dir=dir_name, list_name=show)
    elif show == "LISTS":
        show_list(lists_dir=dir_name)
    if delete != 0 and listname:
        del_task(number=delete, lists_dir=dir_name, list_name=listname)
    if del_list:
        delete_list(lists_dir=dir_name, list_name=del_list)
    if update:
        update_task(lists_dir=dir_name, listname=update)


if __name__ == "__main__":
    # pylint: disable= no-value-for-parameter
    main()
