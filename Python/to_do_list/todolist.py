# Module required
import sys
import datetime


# Funktionsimplementierung


# help function
def help_1():
    """Funktionalitäten der Anwendung anzeigen
    """
    sa = """Usage :-
$ ./todolist add "todo item"  # Add a new todo
$ ./todolist ls               # Show remaining todos
$ ./todolist del NUMBER       # Delete a todo
$ ./todolist done NUMBER      # Complete a todo
$ ./todolist help             # Show usage"""
    sys.stdout.buffer.write(sa.encode('utf8'))


def main():
    """
    To do list - Anwendung
    """
    help_1()


if __name__ == '__main__':
    main()