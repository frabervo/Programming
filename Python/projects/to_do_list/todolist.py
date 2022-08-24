# modules
from fileinput import filename
import sys
import datetime
from pathlib import Path
from termcolor import colored
import click


# Function implementation
def create_lists_dir() -> str:
    """create the directory where the to-do lists will be stored.

    this function create in der Home directory of the current user a subdirectory named .todolists

    Returns
    -------
        str: the directory name
    """
    todolist_dir = str(Path.home()) + "/.todolists"     # 1. define the path of the directory in the home directory
    todolist_dir = Path(todolist_dir)                   # 2. Initialise the Path object with the path
    if todolist_dir.exists() is not True:               # 3. check if the directory already exists
        todolist_dir.mkdir(parents=True)                # 4. create the directory with all subdirectory
        click.echo(f"directory: {todolist_dir} sucessfully created\n")
    return str(todolist_dir)


def create_file(lists_dir: str, filename: str) -> None:
    """
    this function creates a file in the home directory where the task will be added

    Parameters
    ----------
    lists_dir : str
            the name of the directory where the lists are stored
    filename : str
            the name of the to-do list
    """
    # define the path of the file in home/todolists directory of the user
    fle = Path(lists_dir + "/." + filename + ".txt")
    if fle.exists() is True:
        click.echo(colored("The to-do list was already created! \n", "red"))

    fle.touch(exist_ok=True)                                # create the file it doesn't exit
    # abort the execution if the file was not created
    if fle.exists() is not True:
        sys.stderr.buffer.write("The to-do list was not created\n".encode("utf8"))
        sys.exit(1)


def add_task() -> None:
    """add task to the to-do list

    This function takes the given string and inserts it as a task in the todolist.txt file. The task is assigned a date
    and a number number
    """


@click.command()
@click.option("--delete", default=0, help="delete a task --del=TASK_NUMBER")
@click.option("--add", help='to add "new task" to the task list')
@click.option("--update", help="to update the task --update=TASK_NUMBER in the task list.")
@click.option("--show", help="Display the to-do list.")
@click.option("--create", help='create a todolist')
@click.argument('listname', required=False)
def main(delete, add, update, show, create, listname):
    """A todolist programm as command line
    """
    # the user want to create a to do list
    dir_name = create_lists_dir()
    if create:
        create_file(lists_dir=dir_name, filename=create)
        click.echo(colored(f"the to-do list: {create} is created", "green"))

    if add:
        if listname:
            fle_name = dir_name + "/." + listname + ".txt"
            # 1. check if the to-do list was already created
            if Path(fle_name).exists() is True:
                # 2. open the file /home/username/.todolists/.listname.txt with mode = a to add text
                fle_name = dir_name + "/." + listname + ".txt"
                fle_object = open(file=fle_name, encoding="utf8", mode="a")
                # 3. add the task with a number  ************** To do: with number*****************
                fle_object.write(add + "\n")
                click.echo("The task was successfully added")
                # 4. close the file
                fle_object.close()
            else:
                click.echo(colored(f"The to-do list {listname} was not created. Please create it first.", "red"))
        else:
            click.echo(colored("indicate the to-do list!", "red"))


if __name__ == "__main__":
    main()
