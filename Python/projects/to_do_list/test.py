import json
from pathlib import Path
import sys
from termcolor import colored

# Globale Variables
list_names = ["uni", "einkauf", "arbeit", "alltag"]


def create_lists():
    exists_yes = False
    for listname in list_names:
        path_dir_name = str(Path.home()) + "/.todolists/" + "." + listname + ".json"
        path_dir = Path(path_dir_name)
        if path_dir.exists() is not True:
            path_dir.touch(exist_ok=False)
        else:
            exists_yes = True
    if exists_yes is not True:
        print(colored("Files are successfully created", "green"))
    else:
        print(colored("Files already exist", "green"))


def add_content_first_list():
    number = 1
    total_task = 20
    list_content = []
    # prepare the  list content
    for task_number in range(1, 20):
        task = {
            "task_number": task_number,
            "task": "Vorlesung besuchen",
            "date": "20.08.2022"
        }
        list_content.append(task)
    # write list_content in the json_file ( the first one)
    list_path = str(Path.home()) + "/.todolists/" + "." + list_names[0] + ".json"
    if Path(list_path).exists() is True:
        with open(file=list_path, encoding="utf8", mode="r+") as file_obj:
            file_obj.truncate(0)
            file_obj.seek(0)
            json.dump(obj=list_content, fp=file_obj, indent=2)
    else:
        print(colored("File doesn't exist", "red"))
        sys.exit(1)


def main():
    create_lists()
    add_content_first_list()


if __name__ == "__main__":
    main()
