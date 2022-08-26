"""this script generate the docstring of a module and store it to the file: code_doc.txt
"""
# Modules
import sys
import todolist
from pathlib import Path

if __name__ == "__main__":
    # create the file code_doc.txt in the project directory
    file_name = str(Path.cwd()) + "/code_doc.txt"
    with open(file=str(file_name), encoding="utf8", mode="w") as file_obj:
        # the open function will create the file if it not exists and the file always rewrite in w mode
        help(todolist)
    sys.exit(0)
