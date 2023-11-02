#!/usr/bin/python3
"""The programm that contains the entry
point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
   """class that difine the console behavior"""
    prompt = "(hbnb)"
    print("{}{}".format('Documented commands (type help <topic>):\n', ('=' * 40)))

    def do_EOF(self, arg):
	    """EOF to exit the program"""
        return True

    def quit(self, line)
	""" 'quit' command to exit the program"""
        return True

    def emptyline(self):
        """do nothing when we have empty line, or space"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
