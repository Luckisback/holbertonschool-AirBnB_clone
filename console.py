#!/usr/bin/python3
"""The program that contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class that defines the console behavior"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def do_quit(self, arg):
        """'quit' command to exit the program"""
        return True

    def emptyline(self):
        """"Documented commands (type help <topic>):
            =======================================
            EOF    help    quit
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
